class Task:
    comments = []
    completed = False

    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date

    def change_name(self, new_name: str):
        if self.name == new_name:
            return "Name cannot be the same."
        self.name = new_name
        return self.name

    def change_due_date(self, new_date: str):
        if self.due_date == new_date:
            return "Date cannot be the same."
        self.due_date = new_date
        return self.due_date

    def add_comment(self, comment: str):
        Task.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        if comment_number not in range(len(Task.comments)):
            return "Cannot find comment."
        Task.comments[comment_number] = new_comment
        return ", ".join(Task.comments)

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"


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
        for task in Section.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        removed_tasks = 0
        for task in Section.tasks:
            if task.completed:
                Section.tasks.remove(task)
                removed_tasks += 1
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        return f"Section {self.name}:\n" + "\n".join([task.details() for task in Section.tasks])

"""
section = Section("New section")
task = Task("Tst", "27.04.2020")
section.add_task(task)
section.complete_task("Tst")
message = task.completed
print(message)
#self.assertTrue(message)
"""
"""      
11    def test_complete_task_message(self):
        section = Section("New section")
        task = Task("Tst", "27.04.2020")
        section.add_task(task)
        message = section.complete_task("Tst")
        expected = "Completed task Tst"
        self.assertEqual(message, expected)
        
    
13    def test_clean_section(self):
        section = Section("New section")
        task = Task("Tst", "27.04.2020")
        section.add_task(task)
        section.complete_task("Tst")
        message = section.clean_section()
        expected = "Cleared 1 tasks."
        self.assertEqual(message, expected)
        
    
"""
