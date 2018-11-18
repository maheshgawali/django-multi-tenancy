.PHONY: start
start:
	docker-compose up -d

.PHONY: stop
stop:
	docker-compose down

.PHONY: dev
dev:
	python manage.py runserver


.PHONY: test
test:
	python manage.py test

.PHONY: hosts
hosts:
	- sed -i.bak '/127.0.0.1 user1.app.com/d' /etc/hosts
	- sed -i.bak '/127.0.0.1 user2.app.com/d' /etc/hosts
	echo '127.0.0.1 user1.app.com' >> /etc/hosts
	echo '127.0.0.1 user2.app.com' >> /etc/hosts


.PHONY: migrate
migrate:
	python manage.py migrate --database=default
	python manage.py migrate --database=db1
	python manage.py migrate --database=db2


.PHONY: load_base_test_data
load_base_test_data:
	python manage.py loaddata django_mt/mt_core/test_data_db_default --database=default
	python manage.py loaddata django_mt/mt_core/test_data_db1 --database=db1
	python manage.py loaddata django_mt/mt_core/test_data_db2 --database=db2

