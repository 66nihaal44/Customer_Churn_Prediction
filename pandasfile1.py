import pandas as pd
def load_and_prepare_data(query, conn):
  df = pd.read_sql(query, conn)
  df = df.drop(columns=['customerID'])
  df['TotalCharges'] = df['TotalCharges'].fillna(0) # fill null rows
  X = df.drop(columns=['Churn'])
  y = df['Churn']
  X = pd.get_dummies(X, drop_first=True) # avoid multicolinearity
  return X, y