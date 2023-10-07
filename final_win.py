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

        '''getting data about the experiment'''
        self.exp = exp

        ''' creating and configuring graphic elements:'''
        #self.ini...

        '''establishes connections between elements'''
        #self.conn...

        '''sets the window appearance (label, size, location)'''
        #self.set_ap...
        
        # start:
        self.show()

    def results(self):
        self.index = 0
        return 'blank'

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
        '''functia care seteaza aparenta ferestrei (titlu, dimensiune, pozitia pe ecran)'''
        '''in fisierul instr.py gasiti numele variabilelor in care sunt tinute titlul, latimea, lungimea si pozitia ferestrei'''
        #self.setWindowTitle(TITLU_FEREASTRA)
        #self.resize(LATIME_FEREASTRA, LUNGIME_FEREASTRA)
        #self.move(POZTIA_X, POZITIA_Y)
