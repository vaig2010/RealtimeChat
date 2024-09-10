## Setup

## Generate Secret Key
```
python manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
exit()
```

## Create .env
#### ALL VARS
```
SECRET_KEY=
ENVIRONMENT=prod
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
ALLOWED_HOSTS=
CSRF_TRUSTED_ORIGINS=
POSTGRES_USER=
POSTGRES_PASSWORD=
```

## Build
```sh
docker-compose build
```
## Run
```sh
docker-compose up -d
```

## Create superuser
```sh
docker exec -it chat python3 manage.py createsuperuser
```

## Create lobby
```sh
docker exec -it chat_db psql -h db -U postgres -d rtchat -c "INSERT INTO a_rtchat_chatgroup (group_name, is_private, admin_id, groupchat_name) VALUES ('Lobby', '0', NULL, NULL);"
```
