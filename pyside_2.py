"""
ZetCode PySide tutorial 

This example shows an icon in the titlebar of the window.
This example shows a tooltip on a window and a button

author: Jan Bodnar
website: zetcode.com 
last edited: August 2011
"""
import sys
from PySide import QtGui, QtCore
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
        ###Quit button ###
        qbtn=QtGui.QPushButton('Quit', self)
        qbtn.setToolTip('This is a <b>Quit</b> widget')
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        ''' If we click on the button, the signal clicked is emitted.
        # The slot can be a Qt slot or any Python callable.
        # The QtCore.QCoreApplication contains the main event loop. It processes and
        # dispatches all events. The instance() method gives us the current instance.
        # Note that QtCore.QCoreApplication is created with the QtGui.QApplication. 
        The clicked signal is connected to the quit() method, which terminates
        the application. The communication is done between two objects. The sender
        and the receiver. The sender is the push button, the receiver is
        the application object.'''
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(150, 50)       
        ###Quit button - end ###

        #########icon - start ###############
        # self.setGeometry(300, 300, 250, 150)
        #locates the window on the screen and sets the size of the window.
        #The first two parameters are the x and y positions of the window.
        #The third is the width and the fourth is the height of the window.
        self.setWindowTitle('Testing')
        self.setWindowIcon(QtGui.QIcon('list_icon_world'))        
    	##########icon - end ##########
        ### Center Window ###
        self.resize(250,150)
        self.center #The code that will center the window is placed in the custom center() method.
        ### Center Window - end ###
        self.show()
# If we close the QtGui.QWidget, the QCloseEvent is generated. To modify the
# widget behaviour we need to reimplement the closeEvent() event handler.
    def closeEvent(self, event):
        
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()   

    def center(self):
        # We get a rectangle specifying the geometry of the main window. 
        # This includes any window frame.
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        pass
# We put the startup code inside the main() method. This is a Python idiom.        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()