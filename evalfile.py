from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib

from src.pyodbcfile1 import get_connection
from src.pandasfile1 import load_and_prepare_data

query, conn = get_connection()
X, y = load_and_prepare_data(query, conn)

X_train, X_test, y_train, y_test = train_test_split(
  X, y, test_size = 0.2, random_state=50, stratify=y
)
clf = joblib.load("artifacts/churn_pipeline.joblib")


y_pred = clf.predict(X_test)
y_prob = clf.predict_proba(X_test)[:, 1]

featureNames = clf.named_steps["preprocess"].get_feature_names_out()
coefs = clf.named_steps["model"].coef_[0]

importanceDf = pd.DataFrame({
  "feature": featureNames,
  "coefficient": coefs,
  "abs_coefficient": abs(coefs)
}).sort_values("abs_coefficient", ascending=False)

print("Accuracy: ", accuracy_score(y_test, y_pred))
print("ROC AUC: ", roc_auc_score(y_test, y_prob))
print("classification_report: ", classification_report(y_test, y_pred))
print("Feature Importance: ", importanceDf.head(10))