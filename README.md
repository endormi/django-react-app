# Django-React-App

**Backend**: Django (**2.1.9**)

**Frontend**: React (**16.8.6**)

**NGINX**: NGINX-proxy with Docker

## Running the server

You must have [docker](https://www.docker.com/) and [docker compose](https://docs.docker.com/compose/) installed.

```
docker-compose up
```

Build:

```
docker-compose build
```

### Other option (for running the server)

If `docker-compose up` doesn't work for some reason, this is an additional way you can get this project to work.

The [backend](https://github.com/endormi/django-react-app/tree/master/backend) and the [frontend](https://github.com/endormi/django-react-app/tree/master/frontend) have simple instructions to get the server up and running. Remember that you have to have both running, so you will have to use two terminals.
