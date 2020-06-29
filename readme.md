## Start
### Run app
```
docker-compose up
```

### Generate some test data
```
cd data
python generate_test_data.py -n 10000 test_data.csv
```

### Upload test data to the app via Django management command

```
docker-compose exec app python3.7 manage.py upload -v 1 data/works_metadata.csv
docker-compose exec app python3.7 manage.py upload -v 1 data/test_data.csv
```

## Usage
1. Postgres is exposed at `localhost:5432`, credentials can be found in `docker-compose.yml:postgres` env variables
2. Django app is exposed at `localhost:8000`
2.1. Django admin page: [`http://localhost:8000/admin`](http://localhost:8000/admin), credentials can be found in `docker-compose.yml:app` env variables
2.2. REST endpoints, no authorization:
    list all works, with pagination:
    ```
    curl -X GET http://localhost:8000/works/all -H "Accept: application/json"
    ```
   
    select work by ISWC:
    
    ```
    curl -X GET http://localhost:8000/works/work/T9204649558 -H "Accept: application/json"
    ``` 

## Remove & restart from scratch
1. Stop docker-compose (or `docker-compose down` if you run in detached mode)
2. `docker-compose rm -f app postgres`