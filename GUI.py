import kataster
import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, \
    QMainWindow, QPlainTextEdit, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QCursor


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setStyleSheet("background: #161219;")
        self.closeButton = QtWidgets.QPushButton(self)
        self.b5 = QtWidgets.QPushButton(self)
        self.b4 = QtWidgets.QPushButton(self)
        self.b3 = QtWidgets.QPushButton(self)
        self.b2 = QtWidgets.QPushButton(self)
        self.b1 = QtWidgets.QPushButton(self)
        self.label1 = QtWidgets.QLabel(self)
        self.setGeometry(100, 60, 860, 650)
        self.setWindowTitle("Zinformatyzowane systemy katastralne")
        self.textArea = QPlainTextEdit(self)
        self.initUI()

    def initUI(self):
        self.textArea.resize(400, 540)
        self.textArea.move(400, 60)
        self.textArea.setFont(QFont("Rota"))
        self.textArea.setStyleSheet(
            "*{font-size: 22px;" +
            "color: 'white';}" +
            "*:hover{background: '#350032';}"
        )

        self.b1.setText("Upload your text file")
        self.b1.move(60, 60)
        self.b1.clicked.connect(self.openFile)
        self.b1.setFixedWidth(270)
        self.b1.setFixedHeight(40)
        self.b1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.b1.setStyleSheet(
            "*{border: 2px solid '#BC006C';" +
            "border-radius: 5px;" +
            "font-size: 22px;" +
            "color: 'white';}" +
            "*:hover{background: '#BC006C';}"
        )

        self.b2.setText("Show all values")
        self.b2.move(60, 130)
        self.b2.clicked.connect(self.setText)
        self.b2.setFixedWidth(270)
        self.b2.setFixedHeight(40)
        self.b2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.b2.setStyleSheet(
            "*{border: 2px solid '#BC006C';" +
            "border-radius: 5px;" +
            "font-size: 22px;" +
            "color: 'white';}" +
            "*:hover{background: '#BC006C';}"
        )

        self.b3.setText("Valid values")
        self.b3.move(60, 200)
        self.b3.clicked.connect(self.setText)
        self.b3.setFixedWidth(270)
        self.b3.setFixedHeight(40)
        self.b3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.b3.setStyleSheet(
            "*{border: 2px solid '#BC006C';" +
            "border-radius: 5px;" +
            "font-size: 22px;" +
            "color: 'white';}" +
            "*:hover{background: '#BC006C';}"
        )

        self.b4.setText("Invalid values")
        self.b4.move(60, 270)
        self.b4.clicked.connect(self.setText)
        self.b4.setFixedWidth(270)
        self.b4.setFixedHeight(40)
        self.b4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.b4.setStyleSheet(
            "*{border: 2px solid '#BC006C';" +
            "border-radius: 5px;" +
            "font-size: 22px;" +
            "color: 'white';}" +
            "*:hover{background: '#BC006C';}"
        )

        self.b5.setText("Clear all")
        self.b5.move(60, 340)
        self.b5.clicked.connect(self.setText)
        self.b5.setFixedWidth(270)
        self.b5.setFixedHeight(40)
        self.b5.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.b5.setStyleSheet(
            "*{border: 2px solid '#BC006C';" +
            "border-radius: 5px;" +
            "font-size: 22px;" +
            "color: 'white';}" +
            "*:hover{background: '#BC006C';}"
        )

        self.closeButton.setText("Close")
        self.closeButton.move(60, 563)
        self.closeButton.clicked.connect(self.closeApp)
        self.closeButton.setFixedWidth(270)
        self.closeButton.setFixedHeight(40)
        self.closeButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.closeButton.setStyleSheet(
            "*{border: 2px solid '#BC006C';" +
            "border-radius: 5px;" +
            "font-size: 22px;" +
            "color: 'white';}" +
            "*:hover{background: '#FC0000';}"
        )

    def msg_box(self, text, msg_type):
        msg = QMessageBox(self)
        msg.setWindowTitle(f'{msg_type}')
        msg.setStyleSheet("QMessageBox{background-color: #161219;" + "color: white;" + "font: bold;"
                          "width: 700px;" + "height: 500px;}" + "QLabel{background:transparent; color:#fff;" +
                          "font-size: 15px;}"
                          "QPushButton{width: 150px;" + "border: 2px solid '#BC006C';" +
                          "border-radius: 3px;" +
                          "font-size: 15px;" +
                          "color: 'white';}" + "QPushButton:hover{background-color: '#BC006C';}")
        msg.setText(f'{text}')
        if msg_type == 'crit-error':
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setIcon(QMessageBox.Critical)
        if msg_type == 'error':
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setIcon(QMessageBox.Warning)
        if msg_type == 'info':
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setIcon(QMessageBox.Information)
        if msg_type == 'question':
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.setIcon(QMessageBox.Question)
        msg.show()
        return msg

    def closeApp(self):
        self.close()

    @staticmethod
    def openFile():
        global filename
        try:
            filename = str(
                QFileDialog().getOpenFileNames(None, "Select a text file", filter="Text files (*.txt)")[0][0])
        except (FileNotFoundError, OSError):
            pass

    def setText(self):
        send = self.sender()
        try:
            klasouzytek = kataster.openFileKlasouzytek(filename)
        except (UnicodeDecodeError, ValueError):
            self.msg_box("Load a valid file!", "Error!")
        else:
            valid, notValid = kataster.validItems(klasouzytek)
            if send.text() == "Show all values":
                self.textArea.clear()
                for code in klasouzytek:
                    self.textArea.appendPlainText(str(code))
                self.textArea.appendPlainText("\n" + "All the values: " + str(len(klasouzytek)))
            if send.text() == "Valid values":
                self.textArea.clear()
                for code in valid:
                    self.textArea.appendPlainText(str(code))
                self.textArea.appendPlainText("\n" + "The number of valid values: " + str(len(valid)))
            if send.text() == "Invalid values":
                self.textArea.clear()
                for code in notValid:
                    self.textArea.appendPlainText(str(code))
                self.textArea.appendPlainText("\n" + "The number of invalid values: " + str(len(notValid)))
            if send.text() == "Clear all":
                self.textArea.clear()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
