# Телеграм Бот для Блокировки Экрана

Этот проект демонстрирует код Телеграм бота, который позволяет удаленно блокировать экран вашего компьютера.<br>
[![YouTube](https://img.shields.io/badge/YouTube-Video-red?logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

## Телеграм Боты

- [BotFather](https://t.me/botfather) - Для создания и управления Телеграм ботами.
- [userinfobot](https://t.me/userinfobot) - Для получения вашего Телеграм ID.

## Требования

Убедитесь, что у вас установлен Python. Вы можете скачать его с [python.org](https://www.python.org/downloads/).

## Устан

1. **Клонируйте репозиторий:**

   Скопируйте URL репозитория и выполните команду:

   ```bash
   git clone https://github.com/ozzy404/pc-screen-lock-bot.git
   ```
   
2. **Перейдите в директорию проекта:**

   ```bash
   cd pc-screen-lock-bot
   ```

3. **Установите необходимые библиотеки:**

   Убедитесь, что у вас установлен Python. Для установки необходимых библиотек используйте файл `requirements.txt`. Выполните следующую команду:

   ```bash
   pip install -r requirements.txt
   ```

## Настройка

1. **Создание Телеграм Бота:**

   - Откройте Телеграм и найдите [BotFather](https://t.me/botfather).
   - Отправьте команду `/start`, чтобы начать.
   - Создайте нового бота с помощью команды `/newbot` и следуйте инструкциям.
   - Скопируйте токен, который вы получите, и вставьте его в файл `bot_script.py`.

2. **Получение Вашего Телеграм ID:**

   - Найдите [userinfobot](https://t.me/userinfobot) в Телеграме.
   - Отправьте команду `/start`, чтобы получить ваш ID.
   - Скопируйте ID и вставьте его в файл `bot_script.py`.

3. **Настройка Автозапуска:**

   - Укажите правильный путь к вашему скрипту в предоставленном `.bat` файле.
   - Поместите `.bat` файл в папку автозапуска Windows, чтобы он запускался при старте:

     - Нажмите Win + R, введите `shell:startup` и нажмите Enter.
     - Скопируйте ваш `.bat` файл в эту папку.

## Доступные версии документации

- [Английская версия](README.en.md)
- [Русская версия](README.md)

## Лицензия

Этот проект лицензирован на условиях лицензии MIT - смотрите файл [LICENSE](LICENSE) для получения подробной информации.