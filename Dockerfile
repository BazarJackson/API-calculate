FROM python:3.12.5

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл calculate.py в рабочую директорию контейнера
COPY calculate.py /app

# Устанавливаем Flask (если он используется в calculate.py)
RUN pip install flask

# Указываем, что Flask будет работать на 5000 порту
EXPOSE 5000

# Запускаем скрипт calculate.py
CMD ["python", "calculate.py"]