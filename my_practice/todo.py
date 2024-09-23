# Task: Todo List with Tags
#
# Implement an abstraction for managing a todo list with tags.
#
# The Task entity should be represented by a dictionary with the following keys:
# - description: a string with the task's description.
# - completed: a boolean status (True if completed, False if not).
# - tags: a list of tags (strings) related to the task.
#
# Functionality:
# 1. create_task(description, tags): Creates and returns a new task dictionary.
#    Ensure the tags field has no duplicates.
# 2. add_task(tasks, task): Adds the task to the global task list and returns it.
# 3. add_tag_to_task(tasks, task_id, tag): Adds a tag to the task if it's not
#    already present and returns the updated task list.
# 4. remove_tag_from_task(tasks, task_id, tag): Removes the specified tag from
#    the task and returns the updated task list.
# 5. mark_task_completed(tasks, task_id): Marks the task as completed and
#    returns the updated task list.
# 6. filter_tasks_by_tags(tasks, filter_tags): Returns a new list of tasks
#    containing all the provided tags. If filter_tags is not provided, return
#    all tasks.


# Задача: Список дел с тегами
#
# Реализуйте абстракцию для работы со списком дел с тегами.
#
# Сущность задачи (task) должна быть представлена словарем со следующими ключами:
# - description: описание задачи (строка).
# - completed: статус задачи (выполнена или нет, булево значение).
# - tags: список тегов (строк), связанных с задачей.
#
# Функциональность:
# 1. create_task(description, tags): Создаёт и возвращает словарь задачи.
#    Убедитесь, что в поле 'tags' нет дубликатов.
# 2. add_task(tasks, task): Добавляет задачу в список и возвращает его.
# 3. add_tag_to_task(tasks, task_id, tag): Добавляет тег к задаче, если его нет,
#    и возвращает обновлённый список задач.
# 4. remove_tag_from_task(tasks, task_id, tag): Удаляет тег из задачи и
#    возвращает обновлённый список.
# 5. mark_task_completed(tasks, task_id): Помечает задачу как выполненную и
#    возвращает обновлённый список.
# 6. filter_tasks_by_tags(tasks, filter_tags): Возвращает задачи, содержащие
#    все указанные теги. Если фильтры не указаны, возвращает все задачи.
#

#
# Example:
# task1 = create_task('Task 1', ['tag1', 'tag2', 'tag2'])
# => {
#      'id': 1,
#      'description': 'Task 1',
#      'completed': False,
#      'tags': ['tag1', 'tag2']
#    }
#
# add_task(tasks, task1)
# => [{'id': 1, 'description': 'Task 1', 'completed': False, 'tags': ['tag1', 'tag2']}]
#
# add_tag_to_task(tasks, 1, 'tag3')
# => {'id': 1, 'description': 'Task 1', 'completed': False, 'tags': ['tag1', 'tag2', 'tag3']}
#
# remove_tag_from_task(tasks, 1, 'tag1')
# => {'id': 1, 'description': 'Task 1', 'completed': False, 'tags': ['tag2', 'tag3']}
#
# filter_tasks_by_tags(tasks, ['tag5'])  # []


from uuid import uuid4


def create_task(description: str, tags: list) -> dict:
    tags = list(set(tags))
    id = int(uuid4()) % 1000
    result = {
        'id': id,
        'description': description,
        'completed': False,
        'tags': tags
    }
    return result


def add_task(tasks: list, task:dict) -> list:
    tasks.append(task)
    return tasks


def add_tag_to_task(tasks: list, task_id: int, tag: str) -> list:
    if not tasks:
        return tasks

    for task in tasks:
        task_idx = task.get('id')
        if task_idx == task_id:
            if tag not in task['tags']:
                task['tags'].append(tag)
                return tasks
            else:
                return tasks
    return tasks


def remove_tag_from_task(tasks: list, task_id: int, tag:str) -> list:
    if not tasks:
        return tasks

    for task in tasks:
        task_idx = task.get('id')
        if task_idx == task_id:
            if tag in task['tags']:
                task['tags'].remove(tag)
                return tasks
            return tasks
    return tasks


def mark_task_completed(tasks: list, task_id: int) -> list:
    if not tasks:
        return tasks

    for task in tasks:
        task_idx = task.get('id')
        if task_idx == task_id:
            task['completed'] = True
            return tasks
    return tasks


def filter_tasks_by_tags(tasks: list, filter_tags=None) -> list:

    if filter_tags is None:
        return tasks

    result = []

    for task in tasks:
        if all(tag in task['tags'] for tag in filter_tags):
            result.append(task)
    return result

# TODO: Проработать на этом примере дубли кода. Расширить тестовые случаи
# Абстракция данных, список, словарь, множество, генерация случайного id
