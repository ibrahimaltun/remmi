import sys
from PyQt6.QtWidgets import QApplication
from db import init_db
from main_window import MainWindow
from theme_manager import ThemeManager


def main():
    init_db()
    app = QApplication(sys.argv)
    theme_manager = ThemeManager()
    win = MainWindow(app, theme_manager)
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
