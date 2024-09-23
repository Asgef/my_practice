from my_practice.todo import (
    create_task, add_task, add_tag_to_task, remove_tag_from_task,
    mark_task_completed, filter_tasks_by_tags
)


def test_create_task():
    task = create_task('Test Task', ['tag1', 'tag2', 'tag2'])
    assert task['description'] == 'Test Task'
    assert task['completed'] is False
    assert set(task['tags']) == {'tag1', 'tag2'}

def test_add_task():
    tasks = []
    task = create_task('Test Task', ['tag1'])
    add_task(tasks, task)
    assert len(tasks) == 1
    assert tasks[0]['description'] == 'Test Task'

def test_add_tag_to_task():
    tasks = []
    task = create_task('Test Task', ['tag1'])
    add_task(tasks, task)
    task_id = task['id']
    add_tag_to_task(tasks, task_id, 'tag2')
    assert 'tag2' in tasks[0]['tags']


def test_remove_tag_from_task():
    tasks = []
    task = create_task('Test Task', ['tag1', 'tag2'])
    add_task(tasks, task)
    task_id = task['id']
    remove_tag_from_task(tasks, task_id, 'tag1')
    assert 'tag1' not in tasks[0]['tags']

def test_mark_task_completed():
    tasks = []
    task = create_task('Test Task', ['tag1'])
    add_task(tasks, task)
    task_id = task['id']
    mark_task_completed(tasks, task_id)
    assert tasks[0]['completed'] is True

def test_filter_tasks_by_tags():
    tasks = []
    task1 = create_task('Task 1', ['tag1', 'tag2'])
    task2 = create_task('Task 2', ['tag2'])
    add_task(tasks, task1)
    add_task(tasks, task2)
    filtered = filter_tasks_by_tags(tasks, ['tag1'])
    assert len(filtered) == 1
    assert filtered[0]['description'] == 'Task 1'
