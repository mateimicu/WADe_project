rm ./app/db.sqlite3
source ./app/.venv/bin/activate
python3 app/manage.py makemigrations
python3 app/manage.py migrate

python3 app/manage.py runserver &


cd ~/Apps/apache-jena-fuseki-3.10.0/
./fuseki-server --update --debug --mem /disyo &

