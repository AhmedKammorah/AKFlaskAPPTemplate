# Build Dev Image 
docker build -f Dockerfile-Dev -t ahmedkammorah/flask_api-dev .


# Build django image
docker build -t ahmedkammorah/flask_api .
