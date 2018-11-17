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
