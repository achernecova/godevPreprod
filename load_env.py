from dotenv import load_dotenv
import os
import sys

# Определяем, какой файл .env загружать.
env_file = "prod.env" if len(sys.argv) > 1 and sys.argv[1] == 'prod' else "myenv.env"

# Вывод информации о текущей директории
print("Current directory:", os.getcwd())

# Путь к файлу .env
file_path = env_file

# Проверка пути к файлу
print("Loading .env file from:", file_path)

# Загружаем переменные окружения из файла
load_dotenv(file_path)

# Теперь вы можете использовать переменные окружения
main_page = os.getenv('MAIN_PAGE')
print("Main Page:", main_page)  # Для проверки, что переменная загружена