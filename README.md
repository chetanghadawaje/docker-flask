# docker-flask
Demo project for flask run on docker.

# Flask Docker

Docker simple flask project.

  - Create flask app
  - Add requirements.txt file
  - Create DockerFile

### Installation

Docker download link: [Docker](https://www.docker.com/products/docker-desktop).

Following step for docker.

- Goto location where DockerFile is located.
```sh
$ docker build -t flask-sample:1 .
```
- Run docker container
```sh
$ docker run -d -p 5000:5000 flask-sample:1
```
