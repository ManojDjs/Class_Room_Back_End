# Class_Room_Back_End
class room, learning management system for the Univeristy

Checking on .env file

# Docker Hub image for future scaling and maintainance
Here we have created Docker image with .env file 
This .env will have AWS logins, AWS RDS database credentials, and AWS s3 Detials
Now for building with .env use these commands

<li> For Building Base image >> docker build . -t cbe:1</li>
<li> For migrations >> docker run --env-file .env cbe:1 sh -c "python manage.py makemigrations && python manage.py migrate"</li>
<li> For Building container >> docker run -p 8000:8000 --env-file .env --name cbeapp cbe:1</li>


# git hub actions will build docker image and push to docker hub

look out for https://github.com/ManojDjs/Class_Room_Back_End/blob/main/.github/workflows/docker-image.yml
