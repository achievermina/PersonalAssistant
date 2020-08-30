## Personal Assistant 

The web application is customized assistant for schedule management, job search and YouTube search.
* [Live demo](https://personalassistant.achieverminalee.ga/)

## General info
Using three different micro services with different programming languages, explore different functionalities.
* [Frontend Repo](https://github.com/achievermina/PersonalAssistant-Frontend)
* [Indeed Webscrapping](https://github.com/achievermina/IndeedWebScrapping-API)

## Architecture
 ![architecture](/../connectingFE/personalAssistantImg/architecture.jpg)


## Screenshot
 ![Main1](/../connectingFE/personalAssistantImg/main-beforeLogin.png)
 ![Main2](/../connectingFE/personalAssistantImg/main-afterLogin.png)
 ![Main3](/../connectingFE/personalAssistantImg/main-activeChatbot.png)

## Technologies
Project is created with:
* Frontend - React.js, HTTP API, Dialogflow
* Backend - Python, Flask, Docker, AWS ( ELS, ELB, EC2, Cloud Watch, DynamoDB), OAUTH2.0
* MicroService - Go, gRPC

## API Doc
* [Google Calender](https://developers.google.com/calendar/v3/reference/events/list)
* [Youtube API](https://developers.google.com/youtube/v3/docs)
* [DialogFlow](https://cloud.google.com/dialogflow/docs/)

## Setup
```
$ cd ../PersonalAssistant

(Using Docker setup - including local Dynamo DB)
$ docker compose-up

(Running flask app only)
$ python app.py
```


