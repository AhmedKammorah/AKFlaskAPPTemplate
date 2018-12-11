# Flask App Template with docker 
* including 
	* docker
	* flask
	* django
	* JWT auth
	* RPC 

## Init
My docker project template for Python Backend Service/app 
including my Full enverironment for dev and production mode 

## Code Dir Tree
	./
		MainApp/    <Your main Flask  code dir> 
		Readme.md
		docker-entrypoint.sh
		..
## Getting Start
* clone this repo
	
* Build The images
```
    cd $PWD
    
	sh build_docker_image.sh 

```

* Start Container On Dev Mode 
```
	sh run_ak_dev.sh
```
#### After that you will be inside the container 
so start generate the porject and work with it 

* Run The flask app

```
	python MainApp/AKAppMain.py  
```


#### Start Container On Pro Mode 
```
	sh run_ak_pro.sh
```

