# Customer_Churn_Prediction
Creates a logistic regression model that predicts customer churn for a telecommunications company using an SQL-backed database. The pipeline intakes data from a local SQL Server instance, performs preprocessing with scikit-learn, and trains a classification model. The resultant model achieves 79% accuracy and 83% ROC AUC score. Feature importance analysis is used to guide reccomendations for improving customer retention.<br>
## Results ##
Accuracy: 0.79<br>
ROC AUC 0.83<br>
Features positively correlating with churn were the number of total charges, the number of monthly charges, and using fiber optic internet service. Features negatively correlating with churn were number of months of tenure, having two-year or one-year contracts, using phone service, recieving tech support, not receiving internet service, and receiving online security.
## Reccomendations ##
Suggested reccomendations include focusing on retaining short-term customers and those using fiber-optic internet service. Short-term customers should be incentivized to enter long-term contracts and service quality for fiber-optic customers should be improved. Encouraging tech support and online security packages is also reccomended.
## Notes ##
Relies on the IBM Telco Customer Churn dataset available at https://www.kaggle.com/datasets/blastchar/telco-customer-churn.
