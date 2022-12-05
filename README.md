
# Описание
Проект управления записями в БД через API.

Позволяет работать с моделями:
Post - публикации
Comment - комментарии
Group - группы пользователей
Follow - подписчики

# Технологии
Python 3.7, Django 3.2, DRF, JWT + Djoser

# Расширенная документация по API доступен после установки:

Документация к API проекта Yatube (v1)
./redoc/

# Установка

Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/MishaButters/api_final_yatube.git
cd api_final_yatube

Cоздать и активировать виртуальное окружение:
python3 -m venv env
source env/bin/activate

Установить зависимости из файла requirements.txt:
python -m pip install --upgrade pip
pip install -r requirements.txt

Выполнить миграции:
python manage.py migrate

Запустить проект:
python manage.py runserver
