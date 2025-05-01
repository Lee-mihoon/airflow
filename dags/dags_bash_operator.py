from airflow.sdk import DAG
import datetime
import pendulum
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator", #dag파일명과 아이디명 일치시키는 것이 좋음음
    schedule="0 0 * * *", #매일마다 0시0분에 도는 작업
    start_date=pendulum.datetime(2025, 4, 1, tz="Asia/Seoul"),
    catchup=False, #True일 경우, 누락된 과거 날짜들도 모두 반영해버림림
    # dagrun_timeout=datetime.timedelta(minutes=60), #60분 이상 돌면 타임아웃되도록 설정정
    # tags=["example", "example2"],
    # params={"example_key": "example_value"}, # task들에 공통적으로 넘겨줄 파라미터가 있을 경우
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami", #whoami라는 텍스트를 출력해준다는 의미
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME", 
    )

    bash_t1 >> bash_t2 #수행순서