from  matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar )

from  matplotlib.figure  import  Figure
from  PyQt5.QtWidgets  import *

from  matplotlib.backends.backend_qt5agg  import  FigureCanvasQTAgg

from  matplotlib.figure  import  Figure


import  numpy  as  np 
import  random

class  MplWidget (QWidget):
    
    def  __init__ ( self ,  parent  =  None ):

        QWidget . __init__ ( self ,  parent )
        
        self . canvas  =  FigureCanvasQTAgg ( Figure ())
        
        vertical_layout  =  QVBoxLayout () 
        vertical_layout . addWidget ( self . canvas )
        
        self . canvas . axes  =  self . canvas . figure . add_subplot ( 111 ) 
        self . setLayout ( vertical_layout )


self.pushButton_2.clicked.connect(self . update_graph )

        


   

def  update_graph ( self ):

    fs  =  500 
    f  =  random . randint ( 1 ,  100 ) 
    ts  =  1 / fs 
    length_of_signal  =  100 
    t  =  np . linspace ( 0 , 1 , length_of_signal )
        
    cosinus_signal  =  np . cos ( 2 * np . pi * f * t ) 
    sinus_signal  =  np . sin ( 2 * np . pi * f * t )

    self . MplWidget . canvas . axes . clear () 
    self . MplWidget . canvas . axes . plot ( t ,  cosinus_signal ) 
    self . MplWidget . canvas . axes . plot ( t ,  sinus_signal ) 
    self . MplWidget . canvas . axes . legend (( 'cosinus' ,  'sinus' ),loc = 'upper right' ) 
    self . MplWidget . canvas . axes . set_title ( ' Cosinus - Sinus Signal' ) 
    self . MplWidget . canvas . draw ()

