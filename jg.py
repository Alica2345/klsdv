class Task:
    def init(self, name, description, deadline, status):
        self.name = "Д/З"
        self.description = "Задание в учебнике"
        self.deadline = "2024-12-3"
        self.status = "не виполнено"

class TaskManager:
    def init(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def mark_as_completed(self, task):
        task.status = "выполнено"

    def print_tasks(self):
        for task in self.tasks:
            print(f" {task.name}, {task.description},  {task.deadline}, {task.status}")

task_manager = TaskManager()

task1 = Task("Сделай дз", "напиши єто в тетради и здай", "2024-12-3")

task_manager.add_task(task1)

task_manager.print_tasks()