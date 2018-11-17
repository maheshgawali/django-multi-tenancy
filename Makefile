.PHONY: start
start:
	docker-compose up -d

.PHONY: stop
stop:
	docker-compose down

.PHONY: dev
dev:
	python manage.py migrate
	python manage.py runserver
