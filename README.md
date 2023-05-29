# API для меню
### Чтобы развернуть приложение выполните следующие действия:
1. Клонируйте проект, откатитесь до работающего коммита (проект развивается) и переименуйте файл ```.env.example``` в ```.env```, используя команды:
```commandline
git clone https://github.com/bimka/menu_catalog.git
cd menu_catalog
git checkout 498ec18037fe0bf2d8d0b502a7fbbef604b072c9
mv .env.example .env
```
2. Выполните команду:
```
docker compose up -d
```
3. Enjoy :sunglasses:

### Работа с API:
После запуска проекта можно посмотреть его структуру и поиграться с ним по адресу:
http://127.0.0.1:8000/docs

### Тестирование API:
Для проверки работоспособности проекта выполните команду:
```commandline

docker compose -f "docker-compose.tests.yaml" up
```
