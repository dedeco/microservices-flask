# Microservice-flask

### Run

```
docker-compose up --build
```
Console
```
Creating microservices-flask_producer_1 ... done
Creating microservices-flask_costumer_1 ... done
Attaching to microservices-flask_producer_1, microservices-flask_costumer_1
producer_1  | [2020-04-22 04:41:52 +0000] [1] [INFO] Starting gunicorn 20.0.4
producer_1  | [2020-04-22 04:41:52 +0000] [1] [INFO] Listening at: http://0.0.0.0:8081 (1)
producer_1  | [2020-04-22 04:41:52 +0000] [1] [INFO] Using worker: sync
producer_1  | [2020-04-22 04:41:52 +0000] [8] [INFO] Booting worker with pid: 8
costumer_1  | [2020-04-22 04:41:52 +0000] [1] [INFO] Starting gunicorn 20.0.4
costumer_1  | [2020-04-22 04:41:52 +0000] [1] [INFO] Listening at: http://0.0.0.0:8080 (1)
costumer_1  | [2020-04-22 04:41:52 +0000] [1] [INFO] Using worker: sync
costumer_1  | [2020-04-22 04:41:52 +0000] [9] [INFO] Booting worker with pid: 9
```

#Example microservices:
Service Costumer
<ul>
<li>http://0.0.0.0:8080/health/status</li>
<li>http://0.0.0.0:8080/health/ping</li>
<li>http://0.0.0.0:8080/api/v1/costumers</li>
</ul>

Service Producer
<ul>
<li>http://0.0.0.0:8081/health/status</li>
<li>http://0.0.0.0:8081/health/ping</li>
<li>http://0.0.0.0:8081/api/v1/producers</li>
</ul>