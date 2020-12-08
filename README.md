COMIC API
=========================
###### Developer Setup
-------------------------------
Follow the following steps to setup your  dev environment
Get started with virtual env
----------------------------
Run the following commands to get started using virtualenv
``` shell
# once - create virtual environment
virtualenv env -p python3.6
```

###### activate it
source env/bin/activate

###### install deps
```
pip install -r requirements.txt
python manage.py createsuperuser
python manage.py migrate
python manage.py runserver

```
###### Project setup Frontend
npm install

###### Compiles and hot-reloads for development

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





 
