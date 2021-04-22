Тестовое задание Traffic Light CPA.

Локальный запуск:

Подготовить статику для nginx:
```
cd backend
pip install --requirement requirements.txt
export $(cat .env)
python src/manage.py collectstatic

cd ..
cp --recursive frontend/* nginx/static/
```
Запустить сервисы:
```
docker-compose up mariadb
docker-compose up backend
docker-compose up nginx
```
