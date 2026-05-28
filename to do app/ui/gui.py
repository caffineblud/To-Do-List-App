import tkinter as tk
from tkinter import messagebox

from core.task_manager import (
    add_task,
    delete_task,
    mark_completed,
    get_tasks
)



def run_app():
    root = tk.Tk()
    root.title("To-Do List App")
    root.geometry("450x550")
    root.resizable(False, False)

    # ---------- FUNCTIONS ----------

    def refresh_tasks():
        task_listbox.delete(0, tk.END)

        tasks = get_tasks()

        for task in tasks:
            status = "✓" if task["completed"] else "✗"
            task_listbox.insert(
                tk.END,
                f"{task['task']} [{status}]"
            )


    def handle_add_task():
        task_name = task_entry.get()

        if task_name.strip() == "":
            messagebox.showwarning(
                "Warning",
                "Task cannot be empty!"
            )
            return

        add_task(task_name)

        task_entry.delete(0, tk.END)
        refresh_tasks()


    def handle_delete_task():
        try:
            selected_index = task_listbox.curselection()[0]
            delete_task(selected_index)
            refresh_tasks()

        except:
            messagebox.showwarning(
                "Warning",
                "Please select a task."
            )


    def handle_mark_completed():
        try:
            selected_index = task_listbox.curselection()[0]
            mark_completed(selected_index)
            refresh_tasks()

        except:
            messagebox.showwarning(
                "Warning",
                "Please select a task."
            )

    # ---------- TITLE ----------

    title_label = tk.Label(
        root,
        text="TO-DO LIST",
        font=("Arial", 22, "bold")
    )

    title_label.pack(pady=15)

    # ---------- TASK ENTRY ----------

    task_entry = tk.Entry(
        root,
        font=("Arial", 14),
        width=28
    )

    task_entry.pack(pady=10)

    # ---------- BUTTONS ----------

    add_button = tk.Button(
        root,
        text="Add Task",
        font=("Arial", 12),
        width=18,
        command=handle_add_task
    )

    add_button.pack(pady=5)

    complete_button = tk.Button(
        root,
        text="Mark Completed",
        font=("Arial", 12),
        width=18,
        command=handle_mark_completed
    )

    complete_button.pack(pady=5)

    delete_button = tk.Button(
        root,
        text="Delete Task",
        font=("Arial", 12),
        width=18,
        command=handle_delete_task
    )

    delete_button.pack(pady=5)

    # ---------- TASK LIST ----------

    task_listbox = tk.Listbox(
        root,
        font=("Arial", 12),
        width=42,
        height=16
    )

    task_listbox.pack(pady=20)

    # ---------- INITIAL LOAD ----------

    refresh_tasks()

    # ---------- RUN ----------

    root.mainloop()