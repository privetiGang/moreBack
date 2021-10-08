# Инструкция #

1. Клонирование проекта:
	
	```bash
	git clone https://github.com/privetiGang/moreBack.git
	cd datasets
	```

2. Создание нового virtualenv:

	```bash
	pip install virtualenv
	virtualenv venv
	source venv/bin/activate
	```
	
3. Установка пакетов:

	```bash
	pip install -r requirements.txt
	```

4. Запуск:

	```bash
	python manage.py runserver
	```
	
5. Доступ в админку:

	```bash
	127.0.0.1:8000/admin
	login: admin
	password: admin	
	```

6. URLS:

	```python
	127.0.0.1:8000/api/create
	127.0.0.1:8000/api/delete/<int:pk>
	127.0.0.1:8000/api/get/?id=<id>
	```
