# API-calculate

Команда - Каримов Дмитрий Вадимович, Кузьмин Михаил Дмитриевич, Серебренников Александр Владимирович, Тельнов Степан Юрьевич все из группы РИ-411003.

# 1 Этап.

В качестве функций калькулятор поддерживает сложение, вычитание, умножение и деление. При делении на 0 будет ошибка.
Мы создали докер файл, потом собрали образ контейнера и запустили локально. Далее через postman отправили http запрос для проверки и все работает.
Через postman проверяли командой - curl -X POST http://localhost:5000/calculate -H "Content-Type: application/json" -d '{"operation":"add", "num1":10, "num2":5}'

