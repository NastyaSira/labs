My laboratory work #1
https://lab1-qqgb.onrender.com

Для запуску у себе на пк

Потрібно клонувати проект в свою робочу директорію:

git clone https://github.com/NastyaSira/labs.git
Створити віртуальне середовище за допомогою venv:

python3 -m venv env
Активувати віртуальне середовище:

source ./env/bin/activate
Встановити flask допомогою команди:

pip install flask
Тут є .flaskenv файл, тому потрібно поставити python-dotenv:

pip install python-dotenv
Далі потрібно збілдити image такою командою:

docker build --build-arg PORT=<your port> . -t <image_name>:latest
Якщо image упішно збілдився, то його можна запустити і перевірити:

docker run -it --rm --network=host -e PORT=<your port> <image_name>:latest

Оскільки були проблеми з запуском, було використано
docker run -p 127.0.0.1:8888:80 nginx

Збілдити контейнер:

docker-compose build
Запустити контейнер:

docker-compose up
