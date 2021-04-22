Тестовое задание Traffic Light CPA.

Backend сервис управляющий деревом отделов и списком сотрудников.

Переменные окружения для локального запуска в файле .env.

Линтеры: `./lint`

Локальный запуск:
```sh
export $(cat .env)
python src/manage.py runserver
```

Для деплоя необходимо сгенерировать SECRET_KEY случаный образом:
```python
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```
