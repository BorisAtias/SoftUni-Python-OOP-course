class Section:

    tasks = []

    def __init__(self, name):
        self.name = name

    def add_task(self, new_task: Task):
        if new_task in Section.tasks:
            return f"Task is already in the section {self.name}"
        Section.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        if task_name not in Section.tasks:
            return f"Could not find task with the name {task_name}"
        Task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        removed_tasks = 0
        for task in Section.tasks:
            if task.completed:
                Section.tasks.remove(task)
                removed_tasks += 1
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        return f"Section {self.name}:\n" + "\n".join([task.details() for task in Section.tasks])
