# Задание E2.9

   Проект каталог автомобилей на Django

   ТехЗадание:
В данном задании нужно реализовать сервис, который будет отправлять email через заданное количество секунд. Для этого мы делаем две страницы. На первой странице вводим параметры (текст email и через какое количество секунд его отправить). На второй странице показываем последние десять писем, которые мы поставили в план (и те, что должны отправиться в будущем, и уже отправленные).
Данный сервис должен быть реализован с применением многопоточности: после того, как письмо создано, должен создаться тред, который должен быть закрыт в какой-то момент.
Сервис должен быть задеплоен на heroku, код задания должен быть на GitHub. Используйте сторонние библиотеки и фреймворки по своему усмотрению.

Для того, чтобы запустить локальный сервер необходимо:
1) Распакуйте проект в папку C:\my_site
2) Откройте командную строку и зайдите в директорию проекта:
   - cd C:\my_site
3) Создате виртуальное окружение:
   - python -m venv django
4) Активируйте виртуальное окружение:
   - django\Scripts\activate.bat
5) Установите все необходимые пакеты:
   - pip install -r requirements.txt
6) Выполнить следующую команду:
   - python manage.py runserver

Для того, чтобы сделать деплой на heroku необходимо:
1) Перейти в каталог с проектом:
   - cd C:\my_site
2) Выпонить следующий команды:
   - git init
   - git add .
   - git commit -m "initial commit"
   - heroku login
   - heroku create
   - heroku addons:create heroku-postgresql --as DATABASE
   - heroku config:set SECRET_KEY=Ваш_секретный_код
   - heroku config:set DISABLE_COLLECTSTATIC=1 (опционально)
   - git push heroku master
   - heroku config:unset DISABLE_COLLECTSTATIC (опционально)
   - heroku run python manage.py collectstatic --noinput (опционально)
   - heroku run python manage.py makemigrations
   - heroku run python manage.py migrate
   - heroku run python manage.py createsuperuser
3) Если необходимо переименовываем приложение:
   - heroku rename -a oldname newname
4) Запускаем приложение:
   - heroku open

Данный проект находится на https://emailmessenger-skillfactory.herokuapp.com/
По умолчанию логин и пароль для пользователя-администратора в проекте:
- Логин: pws_admin
- Пароль: sf_password
