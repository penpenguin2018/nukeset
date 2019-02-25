#coding:utf8
from PySide2.QtWidgets import *
import os
import nuke

class NkLibrary(QWidget):
	def __init__(self):
		super(NkLibrary, self).__init__()

		#variable
		self.libpath = os.getenv("NUKE_PATH")+"/nk/"
		self.appname = "Nuke Library"
		self.version = "v0.1"

		#widget
		self.nklist = QListWidget()
		self.addNkList()
		self.ok = QPushButton("OK")
		self.cancel = QPushButton("Cancel")
		
		#layout
		self.setWindowTitle(self.appname + " " + self.version)
		layout = QVBoxLayout()
		layout.addWidget(self.nklist)
		layout.addWidget(self.ok)
		layout.addWidget(self.cancel)
		self.setLayout(layout)

		#event
		self.cancel.clicked.connect(self.close)
		self.nklist.itemClicked.connect(self.itemClick)
		self.ok.clicked.connect(self.pushOK)

	def addNkList(self):
		nkpath = os.getenv("NUKE_PATH")+"/nk/"
		if not os.path.exists(nkpath):
			nuke.message(nkpath + "경로가 존재하지 않습니다.")
		for i in os.listdir(nkpath):
			base, ext = os.path.splitext(i)
			if ext != ".nk":
				continue
			self.nklist.addItem(QListWidgetItem(i))
	
	def itemClick(self, item):
		self.currentItem = item.text()
		
	def pushOK(self):
		nuke.nodePaste(self.libpath + self.currentItem)
		self.close()

def main():
	global customApp
	try:
		customApp.close()
	except:
		pass
	
	customApp = NkLibrary()
	try:
		customApp.show()
	except:
		pass
