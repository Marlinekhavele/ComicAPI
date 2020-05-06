COMIC API
=========================
Developer Setup
-------------------------------

Follow the following steps to setup your  dev environment

Get started with virtual env
----------------------------

Run the following commands to get started using virtualenv

``` shell
# once - create virtual environment
virtualenv env -p python3.6
```

# activate it
source env/bin/activate

# install deps
```
pip install -r requirements.txt
python manage.py createsuperuser
python manage.py migrate
python manage.py runserver

```
Visit List all the APIs documentation
[http://localhost:8080/docs/](http://localhost:8080/docs/)

Visit List all the APIs on localhost
[http://localhost:8080/api/](http://localhost:8080/api/)


Visit List all the APIs on the server
[http://52.49.227.229/api/](http://localhost:8080/api/)


API docs that shows API documentation
[http://52.49.227.229/docs/](http://localhost:8080/docs/)
```

## Project setup Frontend
npm install

### Compiles and hot-reloads for development

npm run serve
This screenshots are here due to Netlify not accepting my APIs which are http
they only accept https.

```
![alt text](img/1.png "Description goes here")
![alt text](img/2.png "Description goes here")
![alt text](img/3.png "Description goes here")

### Compiles and minifies for production

npm run build


### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

# ERD diagram
![alt text](img/comic.png "ERD Diagram")





 
