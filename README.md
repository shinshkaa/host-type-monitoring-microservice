# Prometheus microservice

## Описание
Данный проект представляет собой микросервис, написанный на Python с использованием библиотеки prometheus_client, который:
- определяет тип хоста (vm, container или physical)
- поднимает http-сервер на 8080 порту

Развёртывание производится:
- через службу systemd
- в контейнере Podman

Параметры:
- `deploy_mode` - выбор режима развёртывания
	- `systemd`
	- `container`
- `stand` - имя группы серверов в inventory

---

## Требования
- Linux (RedHat-подобный дистрибутив)
- Python 3
- Ansible
- Podman

---

## Как раскатить микросервис

Изменить файл `inventory.ini` и подставить IP-адрес виртуальной машины и имя пользователя:
```ini
[my_server]
server01 ansible_host=<IP_ВИРТУАЛЬНОЙ_МАШИНЫ> ansible_user=<ИМЯ_ПОЛЬЗОВАТЕЛЯ>
```

Запустить Ansible-playbook
```bash
ansible-playbook deploy.yaml --ask-become-password -e "stand=<НАЗВАНИЕ_ГРУППЫ_СЕРВЕРОВ> deploy_mode=<РЕЖИМ_РАЗВËРТЫВАНИЯ>"
```

Проверка работоспособности:
- через curl
```bash
curl http://localhost:8080
```
- через браузер
```
http://localhost:8080
```

# Сборка контейнера вручную

- Перейти в основную директорию проекта

- Собрать образ
```bash
podman build -t microservice .
```

- Запустить контейнер
```bash
podman run -d --name microservice -p 8080:8080 microservice
```

- Остановка и удаление микросервиса
```bash
podman stop microservice && \
podman rm microservice
```
