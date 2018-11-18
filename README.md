
# django-multi-tenancy

djangothon 2018 submission to enable multi-tenancy in django

We will follow this pattern of supporting isolated databases http://books.agiliq.com/projects/django-multi-tenant/en/latest/isolated-database.html


## Usage:
Start multiple databases using `make start`. Wait for 1min to get the DB up and running.


Run migrations for all databases using following
```
python manage.py migrate --database=default
python manage.py migrate --database=db1
python manage.py migrate --database=db2
```

Add hosts using `sudo make hosts`

Load test data using `make load_base_test_data`

Now, start server `python manage.py runserver` and visit `http://user1.app.com:8000/login/` in the browser.
You should see the object printed on the page. This user object is fetched from the database of that user.

Visit `http://user2.app.com:8000/login/` in the browser.
You should see the `user2` object printed on the page. This is different user object than previous and it is loaded from different database.

Use `make stop` to stop all containers of this app.

Watch the demo
[![Watch the demo](https://img.youtube.com/vi/Q0ihUxLz9Ks/maxresdefault.jpg)](https://youtu.be/Q0ihUxLz9Ks)



Presentation: https://docs.google.com/presentation/d/1bLRYOUR302Hrq-1VyrlvamBtvUBfc1d3zYigw_rOxeo/edit?usp=sharing

