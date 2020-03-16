import pathlib
import sys
import clicking
import fileHandling
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog,QComboBox,QTextBrowser, QProgressBar,QLabel)

from PySide2.QtGui import QPixmap, QColor

from PySide2.QtCore import QBasicTimer

stepper = 0


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Chat Smasher")
        # Create Widgets

        self.edit = QLineEdit("Welcome")
        self.button = QPushButton("Load Files")
        self.stopButton = QPushButton("Stop")
        self.box1 = QComboBox()  # Holds name of files
        self.filePreview = QTextBrowser()  # Preview Files
        self.loadingBar = QProgressBar(self)

        self.preview = QTextBrowser()
        self.champBox = QComboBox()
        self.ConfirmButton = QPushButton("Start")
        # Create layout and add widgets
        layout = QVBoxLayout()



        self.label2 = QLabel()
        self.label2.setText("Caleb's Chat Smasher")
        self.label2.setStyleSheet("QLabel { background-color : green; color : white; font-size: 20px; text-align : "
                                  "center; }")


        self.label = QLabel()
        pixmap = QPixmap('lek.png')
        self.timer = QBasicTimer()
        self.step = 0
        self.label.setPixmap(pixmap)

        layout.addWidget(self.label2)
        layout.addWidget(self.label)


        #layout.addWidget(self.edit)
        self.champBox = QComboBox()
       # layout.addWidget(self.champBox)
        layout.addWidget(self.button)
        layout.addWidget(self.box1)


        layout.addWidget(self.filePreview)
        layout.addWidget(self.ConfirmButton)
        layout.addWidget(self.stopButton)
        self.loadingBar.setStyleSheet("QProgressBar::chunk {background-color: red}")

        layout.addWidget(self.loadingBar)

        #self.file
        # Set layout
        self.setLayout(layout)
        p = self.palette()
        p.setColor(self.foregroundRole(),QColor(10,10,10,127))
        p.setColor(self.backgroundRole(),QColor(0,0,0,127))

        self.setPalette(p)
        self.setFixedWidth(450)
        self.setFixedHeight(700)


        #make connections
        self.button.clicked.connect(self.imclicked)
        self.ConfirmButton.clicked.connect(self.newStart)
        self.stopButton.clicked.connect(self.stop)
        self.box1.activated.connect(self.updatePreview)

    def start(self):
        print("Ready to Go")
        myFile = pathlib.Path.cwd() /'copypastas' / self.box1.currentText()
        clicking.type_page(myFile)
        self.loadingBar.setStyleSheet("QProgressBar::chunk {background-color: green } QProgressBar {text-align: center}")

    def stop(self):
        self.timer.stop()
        #self.loadingBar.setValue(0)

    def imclicked(self):
        self.updatelist()

    def newStart(self):
        global stepper
        stepper = 0
        self.loadingBar.setValue(0)
        self.loadingBar.setStyleSheet("QProgressBar::chunk {background-color: red;} QProgressBar {text-align: center}")
        self.startTracking()

    def updatelist(self):
        self.box1.clear()
        fileNames = fileHandling.getFileNames()
        for names in fileNames:
            self.box1.addItem(names)
        self.updatePreview()

    def updatePreview(self):
        self.filePreview.clear()
        myFile =  pathlib.Path.cwd() / 'copypastas' / self.box1.currentText()
        with open(myFile, 'r') as pageRead:
            for line in pageRead:
                self.filePreview.append(line)

    def startTracking(self):
        self.timer.start(80,self)

    def timerEvent(self, event):
        global stepper
        stepper +=1
        self.loadingBar.setValue(stepper)
        if self.loadingBar.value() == 100:
            self.start()
            self.timer.stop()


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())