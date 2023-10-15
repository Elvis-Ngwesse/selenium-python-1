

### Start Selenium Grid
 docker-compose -f docker-compose.grid.yaml up -d
 docker-compose -f docker-compose.grid.yaml up -d --scale chrome=4
 docker-compose -f docker-compose.grid.yaml up -d --scale firefox=4

### Setup Virtual Environment



Brew install python
- brew install python 
- export PATH="/opt/homebrew/opt/python/libexec/bin:$PATH"

docker build
docker build --tag 'image_name' .
docker build --tag 'pytest_container' .
docker run --env-file .env image-name
docker run --net=host pytest_container

































# Selenium-Python
Selenium Python framework

**********************
Installing virtual env 
**********************
- pip install virtualenv
- virtualenv venv
- source venv/bin/activate


**********************
Install requirements.txt
**********************
- pip3 install -r requirements.txt
- pip3 freeze > requirements.txt

**********************
Run Tests
**********************
- cd testCases
- cd tests
- pytest

****************************
Run Tests with allure report
****************************
- cd testCases
- cd tests
- pytest --alluredir=reports test_deals.py
- allure serve reports