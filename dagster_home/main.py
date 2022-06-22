from extract.read import get_data
# from dagster import  op, get_dagster_logger

# @op
def main():
  return get_data()
  

if __name__ == '__main__':
  main()

