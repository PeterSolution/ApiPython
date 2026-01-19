import urllib

# parametry połączenia
SERVER = "(localdb)\MSSQLLocalDB"          
DATABASE = "zpiDB"
#PORT = 1433                   # domyślny port SQL Server

# dla Windows Authentication używamy Trusted_Connection=yes
params = urllib.parse.quote_plus(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    f"Trusted_Connection=yes;"
)

SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc:///?odbc_connect={params}"
SQLALCHEMY_TRACK_MODIFICATIONS = False