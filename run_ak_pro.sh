
# stop and remove tscore containers 
docker stop flask_api_1
docker rm flask_api_1

# Run tsusers Container
docker run -ti -d -p 5005:5005  --name flask_api_1 -e AK_APP_ENV="pro" -v "$PWD":/app -v /ak:/ak ahmedkammorah/flask_api