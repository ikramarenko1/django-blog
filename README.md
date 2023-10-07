# Blog (Django)

Курсовой проект **"Blog (Django)"** для IT академии **Main Academy**.

## Установка

1. Клонируйте репозиторий:
```bash
git clone <url репозитория>
```

2. Перейдите в директорию проекта:
```bash
cd django-blog/myblog
```

3. Создайте и активируйте виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate  # на Linux/Mac
venv\Scripts\activate  # на Windows
```

4. Установите необходимые зависимости:
```bash
pip install -r requirements.txt
```

5. Примените миграции:
```bash
python manage.py migrate
```

## Запуск сервера

```bash
python manage.py runserver
```

Откройте [http://localhost:8000](http://localhost:8000) в вашем браузере.

<!-- ## Функционал -->

<!-- Опишите основные возможности и функции вашего Django-проекта. -->

<!-- ## Лицензия -->

<!-- Данный проект распространяется под лицензией MIT. Смотрите файл `LICENSE` для деталей. -->
