import os
import subprocess
import time

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from hardlink_ui import Ui_Form
from PySide6.QtGui import QTextCursor


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.source_dir = ''
        self.target_dir = ''
        self.count = 0
        self.ui.select_source_dir.clicked.connect(self.select_source_dir_function)
        self.ui.select_target_dir.clicked.connect(self.select_target_dir_function)
        self.ui.progress_bar.setValue(0)
        self.ui.progress_bar.setMaximum(100)
        self.ui.excute.clicked.connect(self.execute)

    def select_source_dir_function(self):
        self.source_dir = QFileDialog.getExistingDirectory(self, 'select_source_dir')
        self.ui.source_dir_line.setText(self.source_dir)

    def select_target_dir_function(self):
        self.target_dir = QFileDialog.getExistingDirectory(self, 'select_target_dir')
        self.ui.target_dir_line.setText(self.target_dir)

    def create_hard_links(self, source_dir, target_dir, info, max_steps):
        items = os.listdir(source_dir)
        for item in items:
            source_path = os.path.join(source_dir, item)
            target_path = os.path.join(target_dir, item)

            if os.path.isfile(source_path):
                try:
                    subprocess.run(f'mklink /H "{target_path}" "{source_path}"', shell=True, check=True,
                                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    info.insertPlainText(f'为 {source_path} 创建硬链接\n')
                    info.moveCursor(QTextCursor.MoveOperation.End)
                    self.count += 1
                    self.ui.progress_bar.setValue((self.count / max_steps) * 100)
                except subprocess.CalledProcessError:
                    print(f"Failed to create hard link for {source_path}")

            elif os.path.isdir(source_path):
                os.makedirs(target_path, exist_ok=True)
                self.create_hard_links(source_path, target_path, info, max_steps)

    def execute(self):
        if not self.source_dir or not self.target_dir:
            QMessageBox.information(self, "Error", "请先选择源目录和目标目录")
            return
        self.ui.progress_bar.setValue(0)
        self.ui.progress_info_text.clear()
        self.count = 0
        source_dir_name = os.path.basename(self.source_dir)
        target_dir_path = os.path.join(self.target_dir, source_dir_name)
        os.makedirs(target_dir_path, exist_ok=True)

        max_steps = sum(len(files) for _, _, files in os.walk(self.source_dir))
        start_time = time.time()

        self.create_hard_links(self.source_dir, target_dir_path, self.ui.progress_info_text, max_steps)

        end_time = time.time()
        elapsed_time = end_time - start_time
        self.ui.progress_info_text.insertPlainText(f'硬链接完成，耗时 {elapsed_time:.2f} 秒\n')


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
