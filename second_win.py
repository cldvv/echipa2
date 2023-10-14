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
    
    def next_click(self):
        self.tw = TestWin()
        self.hide()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    ''' sets what the window will look like (label, size, location) '''
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        ''' creates graphic elements '''
        #self.questionnary = AllQuestions()
        self.btn_next = QPushButton(txt_sendresults, self)
        self.btn_test1 = QPushButton(txt_starttest1, self)
        self.btn_test2 = QPushButton(txt_starttest2, self)
        self.btn_test3 = QPushButton(txt_starttest3, self)


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

        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test1.setValidator(self.validator)
        self.line_test1.setValidator(QIntValidator(0, 150))

        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test2.setValidator(self.validator)
        self.line_test2.setValidator(QIntValidator(0, 150))

        self.line_test3 = QLineEdit(txt_hinttest3)
        self.line_test3.setValidator(self.validator)
        self.line_test3.setValidator(QIntValidator(0, 150))
    
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()
        self.r_line.addWidget(self.text_timer, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.text_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment = Qt.AlignLeft) 
        self.l_line.addWidget(self.text_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test1, alignment = Qt.AlignLeft) 
        self.l_line.addWidget(self.text_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test2, alignment = Qt.AlignLeft) 
        self.l_line.addWidget(self.text_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3, alignment = Qt.AlignLeft) 
        self.l_line.addWidget(self.btn_next, alignment = Qt.AlignCenter) 
        self.h_line.addLayout(self.l_line)  
        self.h_line.addLayout(self.r_line)        
        self.setLayout(self.h_line)
    
    def next_click(self):
        self.hide()
        self.prs = Person(self.line_name.text, int(self.line_age.text()))
        self.exp = Experiment(self.prs, self.line_test1.text(), self.line_test2.text(), self.line_test2.text())
        self.fw = FinalWin(self.exp)

    def timer_test1(self):
        ''' '''

    def timer1Event(self):
        ''' '''

    def timer2Event(self):
        ''' '''

    def timer_bob(self):
        ''' '''

    def timer3Event(self):
        ''' '''

    def timer_final(self):
        ''' '''

    def connects(self):
        '''conectati butoanele btn_next,   btn_test1,   btn_test2, btn_test3
        la functiile asociate  next_click, timer_test1, timer_bob, timer_final'''

    ''' sets what the window will look like (label, size, location) '''
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
