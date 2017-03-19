# RoboSim
This is Team 1's Assignment 6 for ECE 4574 at Virginia Tech

## Accessing the Website/Server ui

**Go to this link** [**Database Server Link**](<http://ec2-54-202-25-115.us-west-2.compute.amazonaws.com:8080/v1/ui/>)

### What is this repository for? ###

* This project is to provide a Database and API for storage and retrieval of information needed in Robot Simulation.
* Version 1.0

## Prerequisites to Run ##
* Docker is installed
* Your device is connected to the internet (to clone the repository and download required libraries)

## How to Generate the Docker container ##
1. go ahead and gitclone this repo
`git clone https://github.com/ldevr2t1/docker_pathfind.git`
2. navigate into the web directory (i.e. cd web)
3. run docker commands to get server running
    * `docker-compose build`
    * `docker-compose run`

## How to Stop the Docker Container ##
Run the command `docker stop [id]`, where `[id]` is the generated id number of your container. If you do not know what your container id is, use the command `docker ps` to view all running containers.

## To configure host/ui address
1. To change the server's IP-address edit the **'host'** parameter in main.
    * `File: web/swagger_server/__main__.py`
        - `app.run(host='<your_address>', port=<port_number>)`
    
2. Change the host parameter in the **swagger.yaml** file for the UI to work
    * `web/swagger_server/server/swagger.yaml`
        - `host: "<your_address>:<port_number>"`

## Changing the port number
1. Change the *<port_number>* in the same files for configuring the host/ui address
2. Go into the base directory /docker_pathfind and edit the **docker-compose.yml**
    * `ports: ` 
        `- "<port_number>:<port_number>"`
3. Change the **Dockerfile** (i.e. change the EXPOSE #)
    * `#Expose port # for testing`
    -`    EXPOSE <port_number>`

## NOTE
### If you want to test locally (i.e. localhost)
1. Set **__main__.py** **'host'** parameter to **'0.0.0.0'**
	- **In __main__.py:** `app.run(host='<your_address>', port=<port_number>)`

2. Set **swagger.yaml** file's **host:** to your docker-machine's IP-Address
	- `Run **Docker-machine ip** to get Ip-Address`
	- **In swagger.yaml:** `host: "<your_address>:<port_number>"`
3. Set your port_numbers accordingly (i.e. follow instructions for port number [above])


### Authors ###

* Joshua Chung
* David Gwizdala
