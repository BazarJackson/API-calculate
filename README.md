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





