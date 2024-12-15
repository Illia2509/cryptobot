import tkinter as tk
from tkinter import messagebox

# Observer Pattern класс
class Observer:
    def update(self, message):
        pass

print('Hello')


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.observers = []

    def add_task(self, task):
        if not task.strip():  # смотрим пустая ли задача 
            task = "New Task"  # добавляем New Task тупо по умолчанию
        self.tasks.append(task)
        self.notify_observers(f"Task added: {task}")  # показываем что был добавлен новый таск 

    def remove_task(self, task):
        if task not in self.tasks:  # Проверяем, есть ли задача впринципи в списке
            self.notify_observers("Error: Task not found.")  # пишем что задача не найцдена для удаленияError: Task not found.
            return
        self.tasks.remove(task)
        self.notify_observers(f"Task removed: {task}")  # удаляем таску 

    def add_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

# UI класс
class TaskManagerApp(tk.Tk, Observer):
    def __init__(self, task_manager):
        super().__init__()
        self.task_manager = task_manager
        self.task_manager.add_observer(self)  # Регистрируем UI как наблюдателя

        self.title("Task Manager")
        self.geometry("500x400") # размер окна 

        self.create_widgets()

    def create_widgets(self):
        self.task_entry = tk.Entry(self, width=50)  # Поле ввода для таски
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(self, text="Add Task", command=self.add_task)  # Кнопка для добавления таски 
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(self, text="Remove Task", command=self.remove_task)  # Кнопка для удаления таски
        self.remove_button.pack(pady=5)

        self.task_listbox = tk.Listbox(self, width=50, height=10)  # Список task (внизу под кнопками)
        self.task_listbox.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get().strip()  # Получаем текст из поля ввода
        self.task_manager.add_task(task)  # Добавляем задачу в TaskManager
        self.task_entry.delete(0, tk.END)  # Очищаем поле ввода

    def remove_task(self):
        selected_task = self.task_listbox.get(tk.ACTIVE)  # Получаем выбранную задачу
        if selected_task:
            self.task_manager.remove_task(selected_task)  # Удаляем задачу
        else:
            messagebox.showwarning("Warning", "No task selected to remove.")  # Предупреждение, если таск не выбран

    def update(self, message):
        self.refresh_task_list()  # Обновляем список таск
        messagebox.showinfo("Notification", message)  # Уведомляем пользователя

    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)  # Очищаем список
        for task in self.task_manager.tasks:  # Добавляем актуальные задачи
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    task_manager = TaskManager()  # Создаем экземпляр TaskManager
    app = TaskManagerApp(task_manager)  # Создаем и запускаем GUI
    app.mainloop()
