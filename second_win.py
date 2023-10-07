from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # checking the types of input values
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, QGridLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from final_win import *

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Experiment():
    def __init__(self, person, test1, test2, test3):
        self.person = person
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3

class TestWin(QWidget):
    def __init__(self):
        ''' the window in which a survey is being conducted '''
        super().__init__()

        # creating and configuring graphic elements:
        self.initUI()

        #establishes connections between elements
        self.connects()

        #sets the window appearance (label, size, location)
        self.set_appear()
        
        # start:
        self.show()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def initUI(self):
        ''' creates graphic elements '''
        #self.questionnary = AllQuestions()
        self.btn_next = QPushButton(txt_sendresults, self)
        '''modificati cele 3 linii comentate de mai jos ca sa instantiati 3 butoane.
           Cautati variabilele care contin textele in fisierul instr.py'''
        #self.btn_test1 = butonul 'Start the first test'
        #self.btn_test2 = butonul 'Start doing squats'
        #self.btn_test3 = butonul 'Start the final test'


        self.text_name = QLabel(txt_name)
        self.text_age = QLabel(txt_age)
        self.text_test1 = QLabel(txt_test1)
        self.text_test2 = QLabel(txt_test2)
        self.text_test3 = QLabel(txt_test3)
        self.text_timer = QLabel(txt_timer)
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))

        self.loc = QLocale(QLocale.English, QLocale.UnitedStates) # language, country
        self.validator = QDoubleValidator()
        self.validator.setLocale(self.loc)

        self.line_name = QLineEdit(txt_hintname)

        self.line_age = QLineEdit(txt_hintage)
        self.line_age.setValidator(self.validator) # age should be a number!
        self.line_age.setValidator(QIntValidator(7, 150))

        '''la fel ca line_age de mai sus, instantiati alte 3 casute de text
           line_test1 (txt_hinttest1), 
           line_test2 (txt_hinttest2), 
           line_test3 (txt_hinttest3)'''
        
        self.l_line = QVBoxLayout() #PANOUL DIN STANGA (pt texte, casute de text, butoane)
        self.r_line = QVBoxLayout() #PANOUL DIN DREAPTA (pt numarator genoflexiuni si temporizator)
        self.h_line = QHBoxLayout() #PANOUL PRINCIPAL CARE LE CONTINE PE CELE DOUA PANOURI DE MAI SUS
        self.r_line.addWidget(self.text_timer, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.text_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment = Qt.AlignLeft) 
        self.l_line.addWidget(self.text_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test1, alignment = Qt.AlignLeft)
        #self.l_line.addWidget(self.btn_test1, alignment = Qt.AlignLeft)
        #self.l_line.addWidget(self.line_test1, alignment = Qt.AlignLeft) 
        self.l_line.addWidget(self.text_test2, alignment = Qt.AlignLeft)
        #self.l_line.addWidget(self.btn_test2, alignment = Qt.AlignLeft) 
        self.l_line.addWidget(self.text_test3, alignment = Qt.AlignLeft)
        #self.l_line.addWidget(self.btn_test3, alignment = Qt.AlignLeft)
        #self.l_line.addWidget(self.line_test2, alignment = Qt.AlignLeft)
        #self.l_line.addWidget(self.line_test3, alignment = Qt.AlignLeft) 
        self.l_line.addWidget(self.btn_next, alignment = Qt.AlignCenter) 
        self.h_line.addLayout(self.l_line)  
        self.h_line.addLayout(self.r_line)        
        self.setLayout(self.h_line)
    
    def next_click(self):
        self.hide() #se ascunde fereastra curenta pt a face loc celei noi
        self.prs = Person(self.line_name.text, int(self.line_age.text()))
        self.exp = Experiment(self.prs, self.line_test1.text(), self.line_test2.text(), self.line_test2.text())
        self.fw = FinalWin(self.exp)

    def timer_test1(self):
        '''timer primul test'''

    def timer1Event(self):
        pass

    def timer2Event(self):
        pass

    def timer_bob(self):
        '''timer genoflexiuni'''

    def timer3Event(self):
        pass

    def timer_final(self):
        '''temporizatorul final'''

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        '''conectarea celorlalte 3 butoane cu functiile asociate
           respectiv timer_test1, timer_bob, timer_final
        '''

    ''' sets what the window will look like (label, size, location) '''
    def set_appear(self):
        '''functia care seteaza aparenta ferestrei (titlu, dimensiune, pozitia pe ecran)'''
        '''in fisierul instr.py gasiti numele variabilelor in care sunt tinute titlul, latimea, lungimea si pozitia ferestrei'''
        #self.setWindowTitle(TITLU_FEREASTRA)
        #self.resize(LATIME_FEREASTRA, LUNGIME_FEREASTRA)
        #self.move(POZTIA_X, POZITIA_Y)
