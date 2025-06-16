#!/bin/bash

cd ~/engineering_exam
source .venv/bin/activate
export AIRFLOW_HOME=~/engineering_exam/airflow_home

echo "Copying latest files from Windows..."
cp -ru /mnt/c/Users/olgap/OneDrive/MIPT_Master/Engineering_exam/* ~/engineering_exam/

airflow db migrate

echo "Starting Airflow webserver..."
nohup airflow webserver > ~/engineering_exam/webserver.log 2>&1 &

sleep 5

echo "Starting Airflow scheduler..."
nohup airflow scheduler > ~/engineering_exam/scheduler.log 2>&1 &

echo "Syncing results back to Windows folder..."
cp -ru ~/engineering_exam/results/* /mnt/c/Users/olgap/OneDrive/MIPT_Master/Engineering_exam/results/

echo "Airflow should now be running!"
echo "Web UI: http://localhost:8080 (user: admin, password: admin)"
echo "To stop all Airflow processes, run: pkill -f airflow"
