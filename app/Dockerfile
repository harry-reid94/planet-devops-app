FROM ubuntu:18.04
#install packages

#RUN apt-get install software-properties-common
#RUN apt-add-repository universe
RUN apt-get update
RUN apt-get install -y python3.6 && apt-get install -y python3-pip
RUN apt-get install -y vim
RUN apt-get install -y git

RUN mkdir planet-devops-app
RUN git clone https://github.com/harry-reid94/planet-devops-app.git ./planet-devops-app
EXPOSE 5000
EXPOSE 5001
RUN pip3 install -r ./planet-devops-app/app/requirements.txt

#To Push to Docker Hub
#docker login --username username
#docker tag my-image username/my-repo
#docker push username/my-repo
