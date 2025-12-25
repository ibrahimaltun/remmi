class Task:
    def __init__(self, id, title, description, due_time, interval_minutes, done=False):
        self.id = id
        self.title = title
        self.description = description
        self.due_time = due_time
        self.interval_minutes = interval_minutes
        self.done = done


class TaskRepository:
    def __init__(self):
        self.tasks = []

    def create(self, title, desc, due_time, interval, done=False):
        new_id = len(self.tasks) + 1
        task = Task(new_id, title, desc, due_time, interval, done)
        self.tasks.append(task)
        return task

    def update(self, task_id, title, desc, due_time, interval, done=False):
        for task in self.tasks:
            if task.id == task_id:
                task.title = title
                task.description = desc
                task.due_time = due_time
                task.interval_minutes = interval
                task.done = done
                return task

    def delete(self, task_id):
        self.tasks = [t for t in self.tasks if t.id != task_id]

    def list(self):
        return self.tasks

    def mark_done(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.done = True
                return task
