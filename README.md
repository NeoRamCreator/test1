QuerySet+Form (работает)

1. скачать проект
2. создать виртуальную среду
(2.1) возможно для создания окружения потребуется установить(если не установленно) virtualenv — это инструмент, позволяющий создавать виртуальные окружения с пакетами. для этого воспользуемся командой "pip install virtualenv"
(2.2) для создания виртуального окружения воспользуемся командой "python3 -m venv env", где env-имя(можно задать любое)
(2.3 )для активации среды используем команду "source env/bin/activate"
3. установить библиотеки из файла "requirements.txt" (проще всего воспользоваться командой "pip install -r requirements.txt" в терминале/cmd, запустив команду из директории с данным файлом)
4. для запуска локального сервера используем команду "python3 manage.py runserver"
