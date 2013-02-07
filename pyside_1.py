# provide necessary imports. basic GUI widgets are located 
# in QtGui module.
import sys
from PySide import QtGui

# Every PySide application must create an application object.
# The application object is located in the QtGui module.
app=QtGui.QApplication(sys.argv)
# The sys.argv parameter is a list of arguments from the command line.

wid=QtGui.QWidget()
# The QWidget widget is the base class of all user interface objects in PySide.
# We provide the default constructor for QWidget.
# The default constructor has no parent. A widget with no parent is called a window.

wid.resize(250,150)
# The resize() method resizes the widget. 250px wide and 150px high.

wid.setWindowTitle('Simple')
# set the title for our window. The title is shown in the titlebar.

wid.show()
# The show() method displays the widget on the screen.

sys.exit(app.exec_())
# we enter the mainloop of the application. The event handling starts from this point.
# The mainloop receives events from the window system and dispatches them
# to the application widgets. The mainloop ends, if we call the exit() method
# or the main widget is destroyed. The sys.exit() method ensures a clean exit.
# The environment will be informed, how the application ended.
# the exec_() method has an underscore. This is obviously because the exec is a python keyword.
# And thus, exec_() was used instead.