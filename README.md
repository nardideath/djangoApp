# djangoApp

A simple django project (django | python3 | postgres)

# Version

- 0.0.1

# Requirements

- Docker and docker compose v2

# init dev app

- Create storage paths:
- - mkdir -p ./storage/db_storage01 && mkdir -p ./storage/app_storage01
- - docker compose -f docker-compose.dev.yml up --build
- - - AAA: sometimes db init is not working at first time, please stop and do docker compose

# reinit all (IT DELETES EVERYTHING ON DB & STORAGE)

- rm -rf storage/db_storage01 && rm -rf storage/app_storages01
- rm -rf app/base/migrations
- docker compose -f docker-compose.dev.yml up --build
