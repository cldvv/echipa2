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
        #self.in...
        
        '''apelul metodei care leaga partea vizuala (exemplu butonul) de 
           partea functionala (functia care se executa la apasarea butonului)'''
        #self.con...

        '''sets the window appearance (label, size, location)'''
        #self.set_ap...
        
        '''start:'''
        self.show()

    ''' crearea, configurarea si adaugarea in interfata a elementelor grafice
        precum texte si butoane '''
    def initUI(self):
        self.btn_next = QPushButton(txt_next)
        self.hello_text = QLabel(txt_hello)
        #self.instruction = ...

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        #adauga in panou Qlabelul instruction aliniat la stanga
        #adauga in panou Qbutonul next aliniat pe centru      
        self.setLayout(self.layout_line)

    '''functia care este declansata la apasarea butonului next'''
    def next_click(self):
        '''in aceasta functie trebuie sa instantiem (cream) fereastra a2-a'''
        '''numele clasei care creaza feastra a2-a o gasiti in fisierul secon_win.py'''
        #self.tw = NumeleClaseiFerestreiDoi()
        self.hide() #aceasta instructiune ascunde fereastra actuala pt a face loc pt cea noua
    
    def connects(self):
        '''functia care conecteaza butonul de functia next_click'''
        #self.btn_next.clicked.connect(self.NUMELE_FUNCTIEI_CARE_AFISEAZA_FEREASTRA_DOI)

    def set_appear(self):
        '''functia care seteaza aparenta ferestrei (titlu, dimensiune, pozitia pe ecran)'''
        '''in fisierul instr.py gasiti numele variabilelor in care sunt tinute titlul, latimea, lungimea si pozitia ferestrei'''
        #self.setWindowTitle(TITLU_FEREASTRA)
        #self.resize(LATIME_FEREASTRA, LUNGIME_FEREASTRA)
        #self.move(POZTIA_X, POZITIA_Y)

app = QApplication([])
mw = MainWin()
app.exec_()
