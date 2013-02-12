"""
ZetCode PySide tutorial 

This program creates a statusbar.
A statusbar is created with the help of the QtGui.QMainWindow widget.
In the above example, we create a menubar with one menu. This menu will contain one action, which will terminate the application if selected.
A statusbar is created as well. The action is accessible with the Ctrl + Q shortcut.
Toolbars provide a quick access to the most frequently used commands.
author: Jan Bodnar
website: zetcode.com 
last edited: August 2011
"""

import sys
from PySide import QtGui
class Example(QtGui.QMainWindow):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		textEdit = QtGui.QTextEdit()
		self.setCentralWidget(textEdit) #Here we create a text edit widget. We set it to be the
		# central widget of the QtGui.QMainWindow. The central widget will occupy all space that is left.
		### MENU ###
		# A PySide QtGui.QAction is an abstraction for actions performed
		# with a menubar, toolbar or with a custom keyboard shortcut.
		# we create an action, with a specific icon and an 'Exit' label.
		# exitAction = QtGui.QAction(QtGui.QIcon('exit.png'),'Exit',self) #### this is for icons
		exitAction = QtGui.QAction('Exit',self)
		exitAction.setShortcut('Ctrl+Q') # a shortcut is defined for this action
		exitAction.setStatusTip('Exit application')
		# creates a status tip, which is shown in the statusbar, when we hover
		# a mouse pointer over the menu item
		exitAction.triggered.connect(self.close)
		# When we select this particular action, a triggered signal is emitted. The signal
		# is connected to the close() method of the QtGui.QMainWindow widget. This terminates
		# the application.
		### TOOLBAR ###
		self.toolbar = self.addToolBar('Exit')
		self.toolbar.addAction(exitAction)
		### TOOLBAR - end ###
		### MENU - end ###
		# self.statusBar().showMessage('Ready') #THIS IS JUST A STATUS
		self.statusBar()
		### MENU ###
		menubar = self.menuBar()
		# We create a file menu with the addMenu() method of the menubar object. 
		fileMenu = menubar.addMenu('&File')
		# We add the previously created action to the file menu.
		fileMenu.addAction(exitAction)
		### MENU - end ###
		# To get the statusbar, we call the statusBar() method of the QtGui.QMainWindow class.
    	# The first call of the method creates a status bar. Subsequent calls return
    	# the statusbar object. The showMessage() displays a message on the statusbar.
		self.setGeometry(300,300,250,150)
		self.setWindowTitle('Testing')
		self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


