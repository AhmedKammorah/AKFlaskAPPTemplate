# inheret from ahmedkammorah/django
FROM ahmedkammorah/django
# author
MAINTAINER Ahmed Kammorah

ONBUILD COPY . /app
ONBUILD RUN pip install -r requirements.txt
COPY . /app
RUN pip install -r requirements.txt

EXPOSE 80 8000
# cd on this dir 
WORKDIR /app
COPY . /app

# main command when Run new container from The Image
# CMD ["/bin/bash"]

# Start With etryPoint 
COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]




##Build
#  docker build -t ahmedkammorah/tsusers .

##Run
# docker run -ti --rm -p 8000:8000 --name tsuser -v "$PWD":/app -v /ts/workarea:/ts  ahmedkammorah/tsusers

# Run with deatach mode  -d 
#  docker run -ti -p 8000:8000 --name tsuser -v "$PWD":/app -v /ts/workarea:/ts -d ahmedkammorah/tsusers

## attach to container  
# docker attach tsuser

#docker exec -it ts userbash

