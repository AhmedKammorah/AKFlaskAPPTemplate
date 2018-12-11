
# Build by   build_dev_image.sh

docker stop flask_api-dev_1
docker rm flask_api-dev_1
# Run
# docker run -ti -d -p 8000:8000 --name admin -v "$PWD":/app  kammorah/django-dev
docker run -ti --rm -p 5000:5000 --name flask_api-dev_1 -e AK_APP_ENV="dev" -v "$PWD":/app -v /ak:/ak  ahmedkammorah/flask_api-dev
 
# docker exec -it tsusers-dev bash

# Run Server
# python manage.py runserver 0.0.0.0:8000


 