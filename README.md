## Test runner web application
This is a web application that provides a central place to run Python-based tests.
These tests run in a shared environment.



## How to Run the current project locally
```
cd ionos
cp .env.dist .env
cd ..
docker-compose build
docker-compose up
docker-compose run web pytest -vv api
```
You should now be able to go to http://127.0.0.1:8081/ to see the FE.


## How it works
When creating a new test run request, it triggers a celery task to execute it on the selected env. If the env is busy, we wait for some time (or give up after some retries) and when it's done, we change the status of the request and save the logs.
in the frontend, we call the listing api every one second to get a live updates (also the details api).

In the project we have sample-tests directory to save all the sample tests that can be run. Also, you can choose the actual test files from api.tests dir. The test path is a multi-select, you can choose one or more file to test at a time and these paths are created automatically in a migration file api/migrations/0002_auto_20200706_1208.py
