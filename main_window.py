from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,
                             QPushButton, QMessageBox, QDateTimeEdit, QLineEdit, QTextEdit, QSpinBox, QToolBar)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QAction

import datetime
from models import TaskRepository
from services import ReminderService


class MainWindow(QMainWindow):
    def __init__(self, app, theme_manager):
        super().__init__()
        self.setWindowTitle("ReminApp")
        self.resize(1000, 600)

        self.repo = TaskRepository()
        self.reminder_service = ReminderService(self.repo)
        self.theme_manager = theme_manager
        self.app = app
        self.dark_mode = False

        # Header toolbar
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)
        theme_action = QAction("Tema Değiştir", self)
        theme_action.triggered.connect(self.toggle_theme)
        toolbar.addAction(theme_action)

        # Sol panel
        self.title_input = QLineEdit()
        self.desc_input = QTextEdit()
        self.due_input = QDateTimeEdit(datetime.datetime.now())
        self.due_input.setCalendarPopup(True)
        self.interval_input = QSpinBox()
        self.interval_input.setRange(0, 1440)
        self.interval_input.setSuffix(" dk")

        self.add_btn = QPushButton("Ekle")
        self.add_btn.clicked.connect(self.add_task)
        self.update_btn = QPushButton("Güncelle")
        self.update_btn.setEnabled(False)
        self.update_btn.clicked.connect(self.update_selected)
        self.del_btn = QPushButton("Sil")
        self.del_btn.setEnabled(False)
        self.del_btn.clicked.connect(self.delete_selected)

        left_layout = QVBoxLayout()
        left_layout.addWidget(self.title_input)
        left_layout.addWidget(self.desc_input)
        left_layout.addWidget(self.due_input)
        left_layout.addWidget(self.interval_input)
        left_layout.addWidget(self.add_btn)
        left_layout.addWidget(self.update_btn)
        left_layout.addWidget(self.del_btn)

        # Sağ panel
        self.list = QListWidget()
        self.list.itemSelectionChanged.connect(self.on_selection_changed)
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.list)

        # Ana layout
        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout, 2)
        main_layout.addLayout(right_layout, 3)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.refresh_list()

        # Hatırlatma timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_reminders)
        self.timer.start(60000)

    def refresh_list(self):
        self.list.clear()
        for task in self.repo.list():
            status = "[✓]" if task.done else "[ ]"
            item = QListWidgetItem(
                f"{status} {task.title} - {task.description} (Son: {task.due_time}, Aralık: {task.interval_minutes} dk)")
            item.setData(Qt.ItemDataRole.UserRole, task.id)
            self.list.addItem(item)

    def add_task(self):
        title = self.title_input.text().strip()
        desc = self.desc_input.toPlainText().strip()
        due_time = self.due_input.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        interval = self.interval_input.value()
        if not title:
            QMessageBox.warning(self, "Uyarı", "Başlık boş olamaz.")
            return
        self.repo.create(title, desc, due_time, interval)
        self.refresh_list()
        self.clear_inputs()

    def update_selected(self):
        items = self.list.selectedItems()
        if not items:
            return
        task_id = items[0].data(Qt.ItemDataRole.UserRole)
        title = self.title_input.text().strip()
        desc = self.desc_input.toPlainText().strip()
        due_time = self.due_input.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        interval = self.interval_input.value()
        self.repo.update(task_id, title, desc, due_time, interval)
        self.refresh_list()
        self.clear_inputs()

    def delete_selected(self):
        items = self.list.selectedItems()
        if not items:
            return
        task_id = items[0].data(Qt.ItemDataRole.UserRole)
        self.repo.delete(task_id)
        self.refresh_list()
        self.clear_inputs()

    def on_selection_changed(self):
        items = self.list.selectedItems()
        if items:
            self.update_btn.setEnabled(True)
            self.del_btn.setEnabled(True)
            # Seçilen öğeyi inputlara yükle
            task_id = items[0].data(Qt.ItemDataRole.UserRole)
            for task in self.repo.list():
                if task.id == task_id:
                    self.title_input.setText(task.title)
                    self.desc_input.setPlainText(task.description)
                    dt = datetime.datetime.strptime(
                        task.due_time, "%Y-%m-%d %H:%M:%S")
                    self.due_input.setDateTime(dt)
                    self.interval_input.setValue(task.interval_minutes)
                else:
                    self.update_btn.setEnabled(False)

    def clear_inputs(self):
        self.title_input.clear()
        self.desc_input.clear()
        self.due_input.setDateTime(datetime.datetime.now())
        self.interval_input.setValue(0)
        self.update_btn.setEnabled(False)
        self.del_btn.setEnabled(False)

    def check_reminders(self):
        reminders = self.reminder_service.check_reminders()
        for task in reminders:
            QMessageBox.information(self, "Hatırlatma",
                                    f"Görev: {task.title}\nAçıklama: {task.description}\nSon tarih: {task.due_time}")

    def toggle_theme(self):
        if self.dark_mode:
            self.theme_manager.apply_light(self.app)
        else:
            self.theme_manager.apply_dark(self.app)
        self.dark_mode = not self.dark_mode
