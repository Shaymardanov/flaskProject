# Тестовый пример сервиса на Flask

## Что делает сервис?

Сервис расчитывает депозит по заданному алгоритму.

## Команды для Docker
```
docker build -t myflaskproject .
docker run -d -p 8080:8080 myflaskproject
```
---
Вызов сервиса [GET | POST]

```
http://localhost:8080/
```

Пример входящего сообщения [JSON]

```
{"date": "31.01.2021",
"periods": 7,
"amount": 10000,
"rate": 6}
```
---