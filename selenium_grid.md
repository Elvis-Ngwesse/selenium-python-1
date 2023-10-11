

### Setup Virtual Environment

docker-compose up -d --scale chrome=4

https://gdcgroup.atlassian.net/browse/GC-936


Brew install python
- brew install python 
- export PATH="/opt/homebrew/opt/python/libexec/bin:$PATH"

docker build
docker build --tag 'image_name' .
docker build --tag 'pytest_container' .
docker run --env-file .env image-name
docker run pytest_container