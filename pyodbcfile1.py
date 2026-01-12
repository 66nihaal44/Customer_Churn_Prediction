import pyodbc

def get_connection():
  query = "SELECT * FROM dbo.[Telco-Customer-Churn]"
  conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=TelcoCustomerChurn;"
    "Trusted_Connection=yes;"
    "ApplicationIntent=ReadOnly;"
  )
  return query, conn