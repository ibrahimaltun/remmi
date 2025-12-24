import datetime
import notify2
from PyQt6.QtWidgets import QMessageBox
from models import TaskRepository


class ReminderService:
    def __init__(self, repo: TaskRepository, parent=None):
        self.repo = repo
        self.parent = parent  # QMainWindow referansı (popup için)
        notify2.init("ToDoApp")

    def check_reminders(self):
        now = datetime.datetime.now()
        reminders = []
        for task in self.repo.list():
            if task.done:
                continue
            if not task.due_time:
                continue
            due = datetime.datetime.strptime(
                task.due_time, "%Y-%m-%d %H:%M:%S")
            interval = task.interval_minutes

            if interval > 0:
                delta = (now - due).total_seconds() / 60.0
                if delta >= 0 and delta % interval < 1:
                    reminders.append(task)
                    self._notify(task)
            else:
                if abs((now - due).total_seconds()) < 60:
                    reminders.append(task)
                    self._notify(task)
        return reminders

    def _notify(self, task):
        # Sistem bildirimi (Linux notification center)
        n = notify2.Notification(
            f"Görev Hatırlatma: {task.title}",
            f"Açıklama: {task.description}\nSon tarih: {task.due_time}"
        )
        n.set_timeout(10000)
        n.show()

        # Uygulama içi popup
        if self.parent:
            QMessageBox.information(
                self.parent,
                "Görev Hatırlatma",
                f"Görev: {task.title}\nAçıklama: {task.description}\nSon tarih: {task.due_time}"
            )
