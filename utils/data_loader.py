import os
import json

from constants import DESIRED_PROJECT_TYPES, PROJECTS_TYPES, CARD_PACKAGES_TYPES, CMS_PAGE_TYPES
from package_data import PackageData


def load_service_data():
    # Загрузка данных из JSON-файла
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '..', 'service_pages_data.json')
    try:
        with open(file_path, encoding='utf-8') as f:  # кодировка UTF-8 при открытии файла
            test_data = json.load(f)
    except FileNotFoundError as e:
        raise RuntimeError('Файл service_pages_data.json не найден: ' + str(e))
    except json.JSONDecodeError as e:
        raise RuntimeError('Ошибка при разборе JSON в service_pages_data.json: ' + str(e))
    except Exception as e:  # Ловим все остальные ошибки
        raise RuntimeError('Неизвестная ошибка при загрузке данных: ' + str(e))
    return test_data



def load_service_data_review():
    # Загрузка данных из JSON-файла
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '..', 'service_pages_data.json')
    try:
        with open(file_path, encoding='utf-8') as f:
            test_data = json.load(f)
    except FileNotFoundError as e:
        raise RuntimeError('Файл service_pages_data.json не найден: ' + str(e))
    except json.JSONDecodeError as e:
        raise RuntimeError('Ошибка при разборе JSON в service_pages_data.json: ' + str(e))
    except Exception as e:  # Ловим все остальные ошибки
        raise RuntimeError('Неизвестная ошибка при загрузке данных: ' + str(e))
    # Фильтрация данных по конкретным project_type
    filtered_data = [
            (d['card_type'], d['expected_url'], d['expected_title'])
            for d in test_data
            if d['card_type'] in PROJECTS_TYPES]
    return filtered_data


def load_package_data():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '..', 'package_card_data.json')
    try:
        with open(file_path, encoding='utf-8') as f:
            package_data_list = json.load(f)
    except FileNotFoundError as e:
        raise RuntimeError('Файл package_card_data.json не найден: ' + str(e))
    except json.JSONDecodeError as e:
        raise RuntimeError('Ошибка при разборе JSON в package_card_data.json: ' + str(e))
    except Exception as e:  # Ловим все остальные ошибки
        raise RuntimeError('Неизвестная ошибка при загрузке данных: ' + str(e))
    # Фильтрация данных по конкретным project_type
    return [
        PackageData(**data) for data in package_data_list
        if data['project_type'] in DESIRED_PROJECT_TYPES
    ]

def load_package_data_b2b():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '..', 'package_card_data.json')
    try:
        with open(file_path, encoding='utf-8') as f:
            package_data_list = json.load(f)
    except FileNotFoundError as e:
        raise RuntimeError('Файл package_card_data.json не найден: ' + str(e))
    except json.JSONDecodeError as e:
        raise RuntimeError('Ошибка при разборе JSON в package_card_data.json: ' + str(e))
    except Exception as e:  # Ловим все остальные ошибки
        raise RuntimeError('Неизвестная ошибка при загрузке данных: ' + str(e))
    # Фильтрация данных по конкретным project_type
    return [
        PackageData(**data) for data in package_data_list
        if data['project_type'] in CARD_PACKAGES_TYPES
    ]

def load_package_data_cms():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '..', 'package_card_data.json')
    try:
        with open(file_path, encoding='utf-8') as f:
            package_data_list = json.load(f)
    except FileNotFoundError as e:
        raise RuntimeError('Файл package_card_data.json не найден: ' + str(e))
    except json.JSONDecodeError as e:
        raise RuntimeError('Ошибка при разборе JSON в package_card_data.json: ' + str(e))
    except Exception as e:  # Ловим все остальные ошибки
        raise RuntimeError('Неизвестная ошибка при загрузке данных: ' + str(e))
    # Фильтрация данных по конкретным project_type
    return [
        PackageData(**data) for data in package_data_list
        if data['project_type'] in CMS_PAGE_TYPES
    ]
