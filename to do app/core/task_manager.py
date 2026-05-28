from utils.file_handler import load_tasks, save_tasks



def add_task(task_name):
    tasks = load_tasks()

    task = {
        "task": task_name,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)



def delete_task(index):
    tasks = load_tasks()

    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)



def mark_completed(index):
    tasks = load_tasks()

    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)



def get_tasks():
    return load_tasks()