from sqlalchemy import create_engine
import pandas as pd
import os


csv_data = pd.read_csv('./assets/ks-projects-201801.csv')
df = pd.DataFrame(csv_data)
print("read dataframe...")
# Adjust NaN values in each column, and generally clean data set
df = df.drop(['ID'], 1)
df.columns = df.columns.str.replace('usd pledged', 'usd_pledged')
df['country'] = df['country'].apply(lambda x: x.replace('N,0"', "NO"))
print("processing")
df['deadline'] = pd.to_datetime(df['deadline'])
df['launched'] = pd.to_datetime(df['launched'])
df['name'] = df['name'].fillna('unknown')
df = df.dropna(how='any')


if 'RDS_DB_NAME' in os.environ:
    db_protocol = 'postgresql+psycopg2'
    db_host = os.environ.get('RDS_HOSTNAME', '')
    db_name = os.environ.get('RDS_DB_NAME', '')
    db_password = os.environ.get('RDS_PASSWORD', '')
    db_user = os.environ.get('RDS_USERNAME', '')
else:
    # db_protocol = 'postgresql'
    db_protocol = 'postgresql+psycopg2'
    db_host = os.environ.get('DB_HOST', '')
    db_user = os.environ.get('DB_USER', '')
    db_password = os.environ.get('DB_PASSWORD', '')
    db_name = os.environ.get('DB_NAME', '')


engine = create_engine('{}://{}:{}@{}:5432/{}'.format(
    db_protocol, db_user, db_password, db_host, db_name
))

df.to_sql("project_data_project", engine, if_exists='append', index=False)
