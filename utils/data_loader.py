import os
import json

from constants import DESIRED_PROJECT_TYPES, PROJECTS_TYPES, \
    SUPPORT_PROJECTS_TYPES, PROJECTS_TYPES_ECOM, ECOM_PAGE_TYPES, PROJECTS_TYPES_FRAMEWORK, \
    OUTSTAFF_PROJECT_TYPES
from package_data import PackageData


def load_service_data_review():
    base_url = put_a_secret_loader()
    # Загружаем данные из JSON файла и заменяем только общую часть URL
    return [
        (d['card_type'], d['expected_url'].replace('https://dev.godev.agency/', base_url), d['expected_title'])
        for d in load_file('service_pages_data.json')
        if d['card_type'] in PROJECTS_TYPES
    ]


def load_service_data_web_dev():
    base_url = put_a_secret_loader()
    # Загружаем данные из JSON файла и заменяем только общую часть URL
    return [
        (d['card_type'], d['expected_url'].replace('https://dev.godev.agency/', base_url), d['expected_title'])
        for d in load_file('service_pages_data.json')
        if d['card_type'] in SUPPORT_PROJECTS_TYPES
    ]


def load_service_data_support():
    base_url = put_a_secret_loader()
    return [
        (d['card_type'], d['expected_url'].replace('https://dev.godev.agency/', base_url), d['expected_title'])
        for d in load_file('service_pages_data.json')
        if d['card_type'] in SUPPORT_PROJECTS_TYPES]


def load_service_data_framework():
    base_url = put_a_secret_loader()
    return [
        (d['card_type'], d['expected_url'].replace('https://dev.godev.agency/', base_url), d['expected_title'])
        for d in load_file('service_pages_data.json')
        if d['card_type'] in PROJECTS_TYPES_FRAMEWORK]


def load_service_data_e_com():
    base_url = put_a_secret_loader()
    return [
        (d['card_type'], d['expected_url'].replace('https://dev.godev.agency/', base_url), d['expected_title'])
        for d in load_file('service_pages_data.json')
        if d['card_type'] in PROJECTS_TYPES_ECOM]


def load_package_data_main():
    return [
        PackageData(**data) for data in load_file('package_card_data.json')
        if data['project_type'] in DESIRED_PROJECT_TYPES
    ]


def load_package_data_e_com():
    return [
        item for item in load_file('package_card_data.json')
        if item['project_type'] in ECOM_PAGE_TYPES
    ]


def load_package_data_outstaff():
    return [
        item for item in load_file('package_card_data.json')
        if item['project_type'] in OUTSTAFF_PROJECT_TYPES
    ]

# передаем название json-а
def load_file(file_name: str):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '..', file_name)
    try:
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError as e:
        raise RuntimeError(f'Файл {file_name} не найден: {e}')
    except json.JSONDecodeError as e:
        raise RuntimeError(f'Ошибка при разборе JSON в {file_name} : {e}' )
    except Exception as e:  # Ловим все остальные ошибки
        raise RuntimeError(f'Неизвестная ошибка при загрузке данных: {e}')
    return data


def put_a_secret_loader():
    # Получаем значение окружения
    environment = os.getenv('ENVIRONMENT', 'development')  # Значение по умолчанию - 'development'
    # Определяем базовый URL в зависимости от окружения
    if environment == 'production':
        base_url = os.getenv('PROD_PAGE', 'https://godev.agency/')  # Значение по умолчанию для прод окружения
    else:
        base_url = os.getenv('MAIN_PAGE', 'https://dev.godev.agency/')  # Значение по умолчанию для дев окружения
    return base_url