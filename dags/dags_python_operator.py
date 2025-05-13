from airflow import DAG
import datetime
import pendulum
from airflow.operators.python import PythonOperator
import random

with DAG(
    dag_id="dags_python_operator", #dag파일명과 아이디명 일치시키는 것이 좋음음
    schedule="30 6 * * *", #매일마다 X시 X분에 도는 작업
    start_date=pendulum.datetime(2025, 4, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    def select_fruit():
        fruit = ['APPLE', 'BANANA', 'ORANGE', 'AVOCADO']
        rand_int = random.randint(0,3) #0에서3까지 임의의 int값 리턴
        print(fruit[rand_int])

    py_t1 = PythonOperator(
        task_id='py_t1',
        python_callable=select_fruit
    )

    py_t1
