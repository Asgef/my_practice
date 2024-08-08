import os
import json
import random
from datetime import datetime, timedelta


def load_data(file_path):
    """Load data from the given file path."""
    try:
        with open(file_path, 'r+') as file:
            cycles = file.read()
            return json.loads(cycles) if cycles else {}
    except FileNotFoundError:
        return {}


def save_data(file_path, data):
    """Save data to the given file path."""
    with open(file_path, 'w+') as file:
        json.dump(data, file)


def get_files(dir):
    """Get list of files in the directory and the latest file."""
    list_files = [
        f for f in os.listdir(dir)
        if os.path.isfile(os.path.join(dir, f))
        and os.path.join(dir, f) not in [
               os.path.join(dir, '__init__.py'),
               os.path.join(dir, '__pycache__'),
               os.path.join(dir, 'random_problem_script.py')
           ]
    ]

    latest_file = max(
        list_files, key=lambda x: os.path.getctime(os.path.join(dir, x))
    )
    return list_files, latest_file


def update_intervals(file_data, file_name, success):
    """Update the intervals for the given file based on success."""
    if file_name not in file_data:
        file_data[file_name] = {
            'interval': 1, 'last_reviewed': str(datetime.now())
        }
    else:
        interval = file_data[file_name]['interval']
        if success:
            file_data[file_name]['interval'] = interval * 2
        else:
            file_data[file_name]['interval'] = max(1, interval // 2)
        file_data[file_name]['last_reviewed'] = str(datetime.now())
    return file_data


def select_file_for_review(file_data):
    """Select a file for review based on the intervals."""
    now = datetime.now()
    due_files = [
        file for file, data in file_data.items()
        if datetime.fromisoformat(data['last_reviewed']) + timedelta(
            days=data['interval']
        ) <= now
    ]
    if due_files:
        return random.choice(due_files)
    else:
        return random.choice(list(file_data.keys()))


def get_enquiry():
    enqr = input('Успешно повторил? "yes/no": ')
    message = {
        'yes': True, 'y': True,
        'д': True, 'да': True,
        'n': False, 'no': False,
        'н': False, 'нет': False
    }
    try:
        return message[enqr]
    except KeyError:
        return get_enquiry()


def main():
    # Путь к сохраненным данным
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(
        current_dir, '../tests/fixtures/random_problem/random_problem'
    )

    # Считывание данных или создание нового файла
    file_data = load_data(file_path)

    # Получаем полный список файлов в текущей директории
    dir = os.getcwd()
    list_files, latest_file = get_files(dir)

    # Добавляем новые файлы в данные
    for file in list_files:
        if file not in file_data:
            file_data[file] = {
                'interval': 1, 'last_reviewed': str(datetime.now())
            }

    # Выбор файла для повторения
    file_for_review = select_file_for_review(file_data)
    print(f'Твоя задача: {file_for_review}')

    # Обновление интервалов (например, пользователь успешно повторил материал)

    success = get_enquiry()
    file_data = update_intervals(file_data, file_for_review, success)

    # Сохранение обновленных данных
    save_data(file_path, file_data)


if __name__ == "__main__":
    main()
