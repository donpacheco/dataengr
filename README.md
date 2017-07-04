Dataengr
===============================
This is a simple News Crawler built with scrapy and Django Rest Framework. 

Current test deployment on AWS EC2 elasticbeanstalk with mongodb hosted at compose.io

http://dataengr-dev.ap-southeast-1.elasticbeanstalk.com/api/

# Requirements
* Scrapy==1.4
* Django==1.9
* mongoengine
* readability-lxml==0.6.2


# Build Setup
Local Deployment as development server
``` 
# Setup virtualenv and switch to it
# install dependencies
pip install -r requirements.txt

#Set the following as your environment variables to run the system
MONGODB_SERVER=''
MONGODB_USERNAME=''
MONGODB_PASSWORD=''
DEBUG=True
SECRET_KEY=''
ALLOWED_HOSTS='*'

# run tests
python manage.py test

# crawl news sites manually
scrapy crawl news

# run development server
python manage.py runserver
```

ElasticBeanstalk AWS deployment
```
#install and configure awsebcli
pip install awsebcli

#switch to working project directory and initialize elasticbeanstalk account config
eb init

#create environment to deploy
eb create

#Set the following as your environment variables in AWS elasticbeanstalk console
MONGODB_SERVER=''
MONGODB_USERNAME=''
MONGODB_PASSWORD=''
DEBUG=True
SECRET_KEY=''
ALLOWED_HOSTS='*'

#deploy!
eb deploy

#open in browser
eb open

```
