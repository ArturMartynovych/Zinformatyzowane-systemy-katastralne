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
        self.dia = QMessageBox(self)
        self.setStyleSheet("background: #161219;")
        self.closeButton = QtWidgets.QPushButton(self)
        self.b5 = QtWidgets.QPushButton(self)
        self.b4 = QtWidgets.QPushButton(self)
        self.b3 = QtWidgets.QPushButton(self)
        self.b2 = QtWidgets.QPushButton(self)
        self.b1 = QtWidgets.QPushButton(self)
        self.label1 = QtWidgets.QLabel(self)
        self.setGeometry(100, 60, 800, 650)
        self.setWindowTitle("Zinformatyzowane systemy katastralne")
        self.textArea = QPlainTextEdit(self)
        self.initUI()

    def initUI(self):
        self.textArea.resize(400, 600)
        self.textArea.move(395, 0)
        self.textArea.setFont(QFont("Rota"))
        self.textArea.setStyleSheet(
            "*{font-size: 22px;" +
            "color: 'white';}" +
            "*:hover{background: '#350032';}"
        )

        self.label1.setText("first label")
        self.label1.move(700, 50)

        self.b1.setText("Upload your text file")
        self.b1.move(60, 30)
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
        self.b3.move(60, 230)
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
        self.b4.move(60, 330)
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
        self.b5.move(60, 430)
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
        self.closeButton.move(60, 580)
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

        self.dia.setStyleSheet(
            "QLabel{color:#fff;}")

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
            self.dia.warning(self, "Error!", "Load a valid file!", self.dia.Ok)
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
