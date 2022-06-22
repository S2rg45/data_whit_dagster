from database.db_con import connection

def load_data(data, name_table):
  engine = connection()
  dataframe_sql = data.to_sql(f'{name_table}', engine[1], if_exists='replace', index=False, schema="public" )
  connection_postgres = connection()      
  connection_postgres[0].autocommit = True
  cursor = connection_postgres[0].cursor()
  sql1 = 'select * from {};'.format(name_table)
  cursor.execute(sql1)
  for i in cursor.fetchall():
      print(i)
  # connection_postgres[0].commit()
  connection_postgres[0].close()