#!usr/bin/python
# -*- coding:utf8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from thBasic import thframe
from thBasic import thlibs
import thskindialog

class ThCloudDiskWindow(thframe.ThFrame):
	def __init__(self):
		super(ThCloudDiskWindow,self).__init__()
		self.initCloudDiskData()
		self.initCloudDiskUI()
		self.initCloudDiskConnect()

	def initCloudDiskData(self):
		self.sd=None

	def initCloudDiskUI(self):
		pass

	def initCloudDiskConnect(self):
		self.titleBar.skinButtonClicked.connect(self.skinDialog)


	def skinDialog(self):
	 	if self.sd:
	 		pass
	 	else:
			self.sd=thskindialog.ThSkinDialog()
		rect=self.getTitleBar().getControlGeometry('skinButton')
		rectFrame=self.sd.geometry()
		frameBottomRight=QtCore.QPoint(rect.right(),rect.bottom())
		frameBottomRight=self.mapToGlobal(frameBottomRight)
		self.sd.setGeometry(frameBottomRight.x()-rectFrame.width(),frameBottomRight.y(),rectFrame.width(),rectFrame.height())
	 	self.sd.show()


def main():
	app=QtGui.QApplication(sys.argv)
	print(sys.argv)
	getQss,qss=thlibs.getQssFile('./skin/qss/black.qss')

	if getQss:
		app.setStyleSheet(qss)
		pass

	w=ThCloudDiskWindow()
	w.setGeometry(100,100,800,600)
	w.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()