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
	- sed -i.bak '/127.0.0.1 mahesh.app.com/d' /etc/hosts
	- sed -i.bak '/127.0.0.1 pranav.app.com/d' /etc/hosts
	echo '127.0.0.1 mahesh.app.com' >> /etc/hosts
	echo '127.0.0.1 pranav.app.com' >> /etc/hosts
