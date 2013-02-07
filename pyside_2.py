"""
ZetCode PySide tutorial 

This example shows an icon in the titlebar of the window.
This example shows a tooltip on a window and a button

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
        ### tooltip - start ###
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10)) #This static method sets a font used to render tooltips.
        self.setToolTip('This is a <b>QWidget</b> widget') #To create a tooltip, we call the setTooltip() method. We can use rich text formatting.

        btn = QtGui.QPushButton('Button', self)	#We create a button widget
        btn.setToolTip('This is a <b>QPushButton</b> widget')	#set a tooltip for it.
        
        btn.resize(btn.sizeHint()) #The button is being resized and moved on the window.
        						   #The sizeHint() method gives a recommended size for the button.
        btn.move(50, 50) 
        ### tooltip - end ###
        #########icon - start ###############
        self.setGeometry(300, 300, 250, 150)
        #locates the window on the screen and sets the size of the window.
        #The first two parameters are the x and y positions of the window.
        #The third is the width and the fourth is the height of the window.
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('list_icon_world'))        
    	##########icon - end ##########
        self.show()


# We put the startup code inside the main() method. This is a Python idiom.        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()