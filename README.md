# Инструкция #

1. Клонирование проекта:
	
	```bash
	git clone https://github.com/privetiGang/moreBack.git
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
	password: 123	
	```

6. URLS:

	```python
	127.0.0.1:8000/metafields/
	127.0.0.1:8000/mts/
	127.0.0.1:8000/adidas/
	127.0.0.1:8000/magazine/
	129.0.0.1:8000/metafields-filter/?name={название}&type={Открытый}
	130.0.0.1:8000/buy-dataset/?id={id}
	131.0.0.1:8000/favourite-dataset/?id={id}
	132.0.0.1:8000/favourite-list/
	133.0.0.1:8000/save-json/ (POST запрос)
	134.0.0.1:8000/select-datasets/?id={id}
	```
