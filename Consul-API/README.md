
# API service for Hashicorp Consul cluster

## Introduction
This task will include a combined environment of a Consul server running on virtaul machine and API service running as a docker

#### File tree
```
├── app           
│ ├── app.py
│ ├── consul_members.py
│ ├── consul_status.py
│ ├── consul_summary.py
│ └── system_info.py
├── ConsulServer
│ ├── 0_server-base.hcl
│ ├── consul.service
│ ├── provision.sh
│ └── Vagrantfile
├── Dockerfile
├── README.md
└── testAPI.sh
```
## Environment


There are 2 main components on this environmet
1. WSL Ubuntu that will run the container (Python app) - this will be the API server
2. Vagrant & VirtaulBox installed on my PC (Windows 11) - vagrant will launch a new VM with hasicorp Consul installed and exposing port 8500.



This is a diagram of the environment:

![App Screenshot](https://i.postimg.cc/nzdk63yk/drawio-2.png)

## Requirements

WSL Ubuntu v22.04 w/ Docker v20.10.21

Vagrant for Windows - v2.2.19

VirtualBox for Windows - v6.1

Consul v1.9.1 (insalled by Vagrant)

#### Nice to have:
Postman - For sending the GET requests for the API server.

## Consul Server
To install the Consul server we will use vagrant and virtualbox.

#### Download vagrant and virtualbox:

vagrant setup file:

https://releases.hashicorp.com/vagrant/2.2.19/vagrant_2.2.19_x86_64.msi

VirtaulBox:

https://download.virtualbox.org/virtualbox/6.1.50/VirtualBox-6.1.50-161033-Win.exe


Using windows command line navigate to the folder where vagrantfile is located:


```bash
C:\Users\Kobi\consul-api-serv\Consul-API\ConsulServer>
```

Now run:

```bash
vagrant up
```

It will launch new VM and install ubuntu 20.10, also Consul as a service.

After the installation has finished, logint to the VM using:

```bash
vagrant ssh
```
Check the service status by running:
```bash
service consul status
```

![App Screenshot](https://i.postimg.cc/nLwrg5FT/consul.png)

Consule UI is also available, you can browse to:
```bash
http://127.0.0.1:8500/
```

## API-server

For the API server, first, we need to build an image from the docker file, and run it.

* #### Make sure Dockerfile and app folder are on the same path.




#### Build

First, build the docker image:

```bash
docker build -t consul-api-serv .
```

#### Run

To create communication between the API and Consul, we'll pass the Consul IP to the container using an environment variable.

To get the Consul IP, use this command on the Consul VM:

```bash
ifconfig eth1 | grep -oP 'inet \K\S+'
```
Lets say Consul server IP is 192.168.5.235.

We will run the docker and send the `IP_ADDRESS` variable for the API Endpoint.



#### To view logs on shell, please make sure you are NOT running detached (-d)

```bash
docker run -p 5000:5000 -e IP_ADDRESS=192.168.5.235 consul-api-serv
```

this way the API server will know to send to requests to that IP.


## Testing

Using Postman we can send GET request and test the API server.

![App Screenshot](https://i.postimg.cc/3wHWTpm0/postman.png)

```bash
http://localhost:5000/v1/api/consulCluster/members

http://localhost:5000/v1/api/consulCluster/status

http://localhost:5000/v1/api/consulCluster/systemInfo

http://localhost:5000/v1/api/consulCluster/summary
```

