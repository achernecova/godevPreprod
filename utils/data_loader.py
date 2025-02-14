import os
import json

from constants import DESIRED_PROJECT_TYPES, PROJECTS_TYPES, CARD_PACKAGES_TYPES, CMS_PAGE_TYPES, \
    SUPPORT_PROJECTS_TYPES, PROJECTS_TYPES_ECOM, ECOM_PAGE_TYPES, PROJECTS_TYPES_FRAMEWORK, CARD_B2B_TYPES, \
    OUTSTAFF_PROJECT_TYPES
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
    return [
        (d['card_type'], d['expected_url'], d['expected_title'])
        for d in load_service()
        if d['card_type'] in PROJECTS_TYPES]


def load_service_data_project():
    return [
        (d['card_type'], d['expected_url'], d['expected_title'])
        for d in load_service()
        if d['card_type'] in PROJECTS_TYPES]


def load_service_data_support():
    return [
        (d['card_type'], d['expected_url'], d['expected_title'])
        for d in load_service()
        if d['card_type'] in SUPPORT_PROJECTS_TYPES]


def load_service_data_services():
    return [
        (d['card_type'], d['expected_url'], d['expected_title'])
        for d in load_service()
        if d['card_type'] in CARD_B2B_TYPES]


def load_service_data_framework():
    return [
        (d['card_type'], d['expected_url'], d['expected_title'])
        for d in load_service()
        if d['card_type'] in PROJECTS_TYPES_FRAMEWORK]


def load_service_data_web_dev():
    return [
        (d['card_type'], d['expected_url'], d['expected_title'])
        for d in load_service()
        if d['card_type'] in SUPPORT_PROJECTS_TYPES]


def load_service_data_e_com():
    # Фильтрация данных по card_type
    return [
        (d['card_type'], d['expected_url'], d['expected_title'])
        for d in load_service()
        if d['card_type'] in PROJECTS_TYPES_ECOM]


def load_service():
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
    return test_data


def load_package_data_main():
    return [
        PackageData(**data) for data in load_package()
        if data['project_type'] in DESIRED_PROJECT_TYPES
    ]


def load_package_data_b2b():
    return [
        PackageData(**data) for data in load_package()
        if data['project_type'] in CARD_PACKAGES_TYPES
    ]


def load_package_data_cms():
    return [
        PackageData(**data) for data in load_package()
        if data['project_type'] in CMS_PAGE_TYPES
    ]


def load_package_data_e_com():
    return [
        item for item in load_package()
        if item['project_type'] in ECOM_PAGE_TYPES
    ]


def load_package_data_outstaff():
    return [
        item for item in load_package()
        if item['project_type'] in OUTSTAFF_PROJECT_TYPES
    ]


def load_package():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '..', 'package_card_data.json')
    try:
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError as e:
        raise RuntimeError('Файл package_card_data.json не найден: ' + str(e))
    except json.JSONDecodeError as e:
        raise RuntimeError('Ошибка при разборе JSON в package_card_data.json: ' + str(e))
    except Exception as e:  # Ловим все остальные ошибки
        raise RuntimeError('Неизвестная ошибка при загрузке данных: ' + str(e))
    return data
