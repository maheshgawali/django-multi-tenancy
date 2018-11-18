
# django-multi-tenancy

djangothon 2018 submission to enable multi-tenancy in django

We will follow this pattern of supporting isolated databases http://books.agiliq.com/projects/django-multi-tenant/en/latest/isolated-database.html


## Usage:
Start multiple databases using `make start`

Run migrations for all databases using `make migrate`

For testing purpose, Run project setup for testing using `sudo make test-setup`. This updates your /etc/hosts. Hence `sudo`.


Now, start server `python manage.py runserver` and visit `user1.app.com:8000` in the browser.
You should see the object printed on the page. This user object is fetched from the database of that user.

Visit `user2.app.com:8000` in the browser.
You should see the `user2` object printed on the page. This is different user object than previous and it is loaded from different database.
