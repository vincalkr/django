docker build . --tag python3.11-django4x
docker run -d  --name python-django --publish 8000:8000 python3.11-django4x