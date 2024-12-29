import sys
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication, QScrollArea, QWidget,
    QVBoxLayout, QDialog, QLabel)
from PySide6.QtCore import Qt, QSize


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        self.edit = QLineEdit()
        self.scroll = QScrollArea()
        self.button = QPushButton("отправить")
        self.setWindowTitle("velocita месенджер заготовка")
        self.label = QLabel("напиши сообщение")
        self.vbox = QVBoxLayout()
        self.widget = QWidget()
        self.widget.setLayout(self.vbox)
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        # Set dialog layout
        self.setLayout(layout)
        self.resize(400, 300)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)

    # Greets the user
    def greetings(self):
        d = []
        f1 = open("user1.txt", "r", encoding="UTF-8")
        f = open("user1.txt", "a", encoding="UTF-8")
        #print(self.edit.text())
        f.write(self.edit.text() + "\n")
        f.close()
        lines = f1.readlines()
        aline = ""
        for line in lines:
            aline = str(aline) + " " + str(line)
            object = QLabel(line)
            self.vbox.addWidget(object)
        aline = aline[0] + aline[2:]
        print(aline)
        self.label.setText(str(aline))



if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec())
