from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import joblib
import os

from src.pyodbcfile1 import get_connection
from src.pandasfile1 import load_and_prepare_data

query, conn = get_connection()
X, y = load_and_prepare_data(query, conn)

# scaling
X_train, X_test, y_train, y_test = train_test_split(
  X, y, test_size = 0.2, random_state=50, stratify=y
)

num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
#scaler = StandardScaler()
#X_train.loc[:, num_cols] = scaler.fit_transform(X_train[num_cols])
#X_test.loc[:, num_cols] = scaler.transform(X_test[num_cols])
numeric_transformer = Pipeline(steps=[
  ("scaler", StandardScaler())
])
preprocessor = ColumnTransformer(
  transformers=[
    ("num", numeric_transformer, num_cols)
  ],
  remainder="passthrough"
)


# regression

#model = LogisticRegression(max_iter=1000)
#model.fit(X_train, y_train)
clf = Pipeline(steps=[
  ("preprocess", preprocessor),
  ("model", LogisticRegression(max_iter=1000))
])
clf.fit(X_train, y_train)

# save
os.makedirs("artifacts", exist_ok=True)
joblib.dump(clf, "artifacts/churn_pipeline.joblib")