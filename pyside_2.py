"""
ZetCode PySide tutorial 

This example shows an icon
in the titlebar of the window.

author: Jan Bodnar
website: zetcode.com 
last edited: August 2011
"""
import sys
from PySide import QtGui
class Example(QtGui.QWidget):	#Example class inherits from QtGui.QWidget class. 
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):	#All three methods have been inherited from the QtGui.QWidget class. 
        self.setGeometry(300, 300, 250, 150)
        #locates the window on the screen and sets the size of the window.
        #The first two parameters are the x and y positions of the window.
        #The third is the width and the fourth is the height of the window.
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('list_icon_world'))        
    
        self.show()


# We put the startup code inside the main() method. This is a Python idiom.        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()