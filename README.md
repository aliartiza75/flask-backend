# HT Backend Repository

This repository contains backend logic and kubernetes manifests. I have used `minikube` for this project.

# Guidelines for containerizing backend 

* To build image
```bash
sudo docker run -t ht-be:0.0.1 -f Dockerfile .
```

* To run docker container on host machine
```bash
sudo docker run -e FLASK_ENV=development -e FLASK_HOST_IP=0.0.0.0 -e=FLASK_HOST_PORT=5001 -e Name=Irtiza -p 1001:5001 ht-be:0.0.1
```

# Guidelines for kubernetes deployment

* Deployment creation
```bash
sudo kubectl apply -f deployment.yaml
```

* Service creation
```bash
sudo kubectl apply -f htbe_service.yaml 
```

* Validating whether application is running or not. Use the command given below from host machine on which kubernetes is running
```
curl -X GET "http://<ip>:<port>/datetime"
```
