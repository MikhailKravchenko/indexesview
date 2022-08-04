# Indexesview
indexesview

Веб-сервис, который:
- получает курсы криптовалют с coingecko
- сохраняет их адрес, имя, цену в БД
- апи-точка отдает эти данные, с параметрами фильтрации по имени, по маркету, по имени и маркету
- подключен сваггер
Данное решение упаковвано в докер компоуз
Предпочтительный стек:
- django-rest-framework
- postgres



# Documentation


# Get Started:

Для запуска понадобится сформировать докер контейнеры и запустить их. 
Если на сервере не установлен Docker, то самое время его установить:

https://docs.docker.com/engine/install/ubuntu/
https://docs.docker.com/compose/install/compose-plugin/#installing-compose-on-linux-systems

Клонировать репозиторий в удобное место:

    git@github.com:MikhailKravchenko/indexesview.git

 Собираем образы:

    docker-compose -f docker-compose.yml up -d --build

# Information
Для парсинга/обновления данных дернуть ручку : api/v1/refresh/
