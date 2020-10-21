FROM ubuntu:18.04
#install packages

#RUN apt-get install software-properties-common
#RUN apt-add-repository universe
RUN apt-get update --fix-missing
RUN apt-get install -y python3.6 && apt-get install -y python3-pip
RUN apt-get install -y git
RUN apt-get install -y vim
RUN mkdir planet-devops-app
EXPOSE 5000
EXPOSE 5001

#Ensure no cache on git clone
ADD http://worldtimeapi.org/api/ip /time.tmp
RUN git clone https://github.com/harry-reid94/planet-devops-app.git ./planet-devops-app
RUN pip3 install -r ./planet-devops-app/app/requirements.txt

WORKDIR /planet-devops-app/app
CMD python3 app.py

#To Push to Docker Hub
#docker login --username username
#docker tag my-image username/my-repo
#docker push username/my-repo
