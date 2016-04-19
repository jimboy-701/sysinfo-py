
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi


app = QApplication([])
widget = loadUi('hwigui.ui')
widget.show()
exit(app.exec_())
