# Install docker
#### https://www.docker.com/products/docker-desktop

## docker-compose up --build

###### API localhost:8001
###### UI localhost:3001


### If you need to execute a specific command in a container:
* docker-compose ps -a
* docker-compose exec container_name sh
### Example command:
* python manage.py migrate
* python manage.py createsuperuser
* exit