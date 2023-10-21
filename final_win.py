from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # checking the types of input values
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, QGridLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)
        
from instr import *

class FinalWin(QWidget):
    def __init__(self, exp):
        ''' the window in which a survey is being conducted '''
        super().__init__()

        #getting data about the experiment
        self.exp = exp

        # creating and configuring graphic elements:
        self.initUI()

        #establishes connections between elements
        # self.connects()

        #sets the window appearance (label, size, location)
        self.set_appear()
        
        # start:
        self.show()

    def results(self):
        if self.exp.person.age < 7:
            self.index = 0
            return "there is no data for this age"
        self.index = (4 * (int(self.exp.test1) + int(self.exp.test2) + int(self.exp.test3)) - 200) / 10


        '''if varsta este intre 7 si 8 ani (inclusive)'''
        if self.exp.person.age == 7 or self.exp.person.age == 8:
            if self.index >= 21:
                return txt_res1
            elif self.index < 21 and self.index >= 17:
                return txt_res2
            elif self.index < 17 and self.index >= 12:
                return txt_res3
            elif self.index < 12 and self.index >= 6.5:
                return txt_res4
            else:
                return txt_res5

        '''daca/if varsta este intre 9 si 10 ani (inclusive)
         - scrieti ca in exemplul 7-8 ani de mai sus ajustand indecsii dupa tabelul din prezentare'''
       
        '''daca/if este intre 11 si 12 ani (inclusive)
        - scrieti ca in exemplul 7-8 ani ajustand indecsii dupa tabelul din prezentare'''
        
        '''daca/if este intre 13 si 14 ani (inclusive)
        - scrieti ca in exemplul 7-8 ani ajustand indecsii dupa tabelul din prezentare'''
        
        '''daca/if este mai mare egal ca 15 ani
        - scrieti ca in exemplul 7-8 ani ajustand indecsii dupa tabelul din prezentare'''
        return "nu este gata"

    def initUI(self):
        ''' creates graphic elements '''
        self.workh_text = QLabel(txt_workheart + self.results())
        self.index_text = QLabel(txt_index + str(self.index))

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment = Qt.AlignCenter)         
        self.setLayout(self.layout_line)

    ''' sets what the window will look like (label, size, location) '''
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

