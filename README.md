# Тестовое задание для к-телеком

Я не успел доделать валидацию серийного номера по маске, хотел спросить у более опытных разработчиков как разобраться с задачей (к сожалению никто не ответил), но закомментил моменты в коде, чтобыразработчик, что это проверяет, мог увидеть к чему я шел и о чем думал, пока это писал, остальные обязательные пункты выполнены, надеюсь на адекватную критику.

**Перед запуском сервера, нужно поменять логин и пароль в папке telecom_web_service/setting.py, в databases на свои данные**
```
pip install -r requirement.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 127.0.0.1:8000
```