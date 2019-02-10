# ht-be

HT Back-end repository

# To build image
sudo docker run -t datetime_api:0.0.1 -f Dockerfile .

# To run docker container

sudo docker run -e FLASK_ENV=development -e FLASK_HOST_IP=0.0.0.0 -e=FLASK_HOST_PORT=5001 -e Name=Irtiza -p 1001:5001 datetime_api:0.0.1

# To expose applicaiton
sudo kubectl expose deployment/htbackendapi --type="NodePort" --port 5001
