from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, QGridLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from second_win import *

       
class MainWin(QWidget):
    def __init__(self):
        ''' the window which the greeting is located in '''
        super().__init__()

        '''apelarea metodei care creaza si configureaza elementele grafice'''
        self.initUI()
        
        '''apelul metodei care leaga partea vizuala (exemplu butonul) de 
           partea functionala (functia care se executa la apasarea butonului)'''
        self.connects()

        '''sets the window appearance (label, size, location)'''
        self.set_appear()
        
        '''start:'''
        self.show()

    ''' crearea, configurarea si adaugarea in interfata a elementelor grafice
        precum texte si butoane '''
    def initUI(self):
        self.btn_next = QPushButton(txt_next)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel('This application allows you to use the Rufier test to make an initial diagnosis of your health.\n'
                    'The Rufier test is a set of physical exercises designed to assess your cardiac performance during physical exertion.\n'
                    'The subject lies in the supine position for 5 minutes and has their pulse rate measured for 15 seconds; \n'
                    'then, within 45 seconds, the subject performs 30 squats.\n'
                    'When the exercise ends, the subject lies down and their pulse is measured again for the first 15 seconds\n'
                    'and then for the last 15 seconds of the first minute of the recovery period.\n'
                    'Important! If you feel unwell during the test (dizziness,\n'
                    'tinnitus, shortness of breath, etc.), stop the test and consult a physician.' )


        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)      
        self.setLayout(self.layout_line)

    def next_click(self):
        '''in aceasta functie trebuie sa instantiem (cream) fereastra a2-a'''
        self.tw = TestWin()
        self.hide()
    
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def set_appear(self):
        '''functia care seteaza aparenta ferestrei (titlu, dimensiune, pozitia pe ecran)'''
        '''in fisierul instr.py gasiti numele variabilelor in care sunt tinute titlul, latimea, lungimea si pozitia ferestrei'''
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

app = QApplication([])
mw = MainWin()
app.exec_()
