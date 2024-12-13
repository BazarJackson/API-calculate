# API-calculate

Команда - Каримов Дмитрий Вадимович, Кузьмин Михаил Дмитриевич, Серебренников Александр Владимирович, Тельнов Степан Юрьевич все из группы РИ-411003.

# Docker

В качестве функций калькулятор поддерживает сложение, вычитание, умножение и деление. При делении на 0 будет ошибка.
Мы создали докер файл, потом собрали образ контейнера и запустили локально. 
![image](https://github.com/user-attachments/assets/bd9e8e1d-2bf8-4c85-b880-125698ca61ac)

Запустили контейнер:
![image](https://github.com/user-attachments/assets/33b09225-56b8-4c2b-af82-40f00894ce43)

Проверка работы:
![image](https://github.com/user-attachments/assets/3fa0e3dc-0c1f-4d12-bdd5-f5e9b2b91ee4)

# GitLab
Создаём docker-compose.yml для запуска контейнеров с gitlab и gitlab-runner. Далее запускаем контейнеры командой docker compose up -d.
Переходим в локальный GitLab:
![image](https://github.com/user-attachments/assets/cff1f35c-8c69-4fc6-a103-05b2e1aba368)

Далее поменяли пароль от root (docker exec -it gitlab /bin/bash ; cd /etc/gitlab ; gitlab-rake "gitlab:password:reset[root]"). 
В Admin Area создали пользователя и потом создали группу и проект:
![image](https://github.com/user-attachments/assets/340fd35d-b788-4a13-bd24-49b5b8e86a9e)
![image](https://github.com/user-attachments/assets/9c9b888e-2063-441e-819d-82c738886da6)

Создали ключи и сертификаты:
![image](https://github.com/user-attachments/assets/e4f45da8-cf02-47b2-9bb1-884ff6fb0cf9)

Также копируем ca.crt в /srv/gitlab-runner/ca.crt

После данного шага нужно зарегать раннера:
docker exec -it gitlab-runner /bin/bash
gitlab-runner register --url "https://gitlab.example.com" --tls-ca-file=/etc/gitlab-runner/ca.crt --registration-token "<token>"
![токен гит лаб раннер](https://github.com/user-attachments/assets/e6edb9e2-7b34-44e9-baf9-e0e95b7e3b87)
![image](https://github.com/user-attachments/assets/54d62d2a-dabe-43a8-9799-82ae8467f5f9)

# Pipeline

В рамках проекта создаём файл `.gitlab-ci.yml`, который будет содержать инструкции для выполнения задач раннером. В репозиторий также добавим файлы `Dockerfile`, `calc.py` и `requirements.txt`. С помощью Trivy будет выполнено сканирование собранного образа, Semgrep просканирует всю директорию проекта, а Bandit проверит только Python-скрипт калькулятора.
![image](https://github.com/user-attachments/assets/594591e5-ae3c-461d-b251-97c462ebdff6)

Переменные для пайплайна были добавлены:
![image](https://github.com/user-attachments/assets/bc33793c-5b51-4932-bf01-f9bca431316c)

Запускаем пайплайн:
![image](https://github.com/user-attachments/assets/78d7b050-8402-4802-8ba4-b03a794ea850)

Разбор отчетов:
bandit:
![image](https://github.com/user-attachments/assets/328d4c2c-bbc7-4942-87db-504e4250efc3)

trivy:
![image](https://github.com/user-attachments/assets/4f0d6536-005b-4f8f-b15b-4ced3463ced6)







