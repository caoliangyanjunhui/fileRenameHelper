# -*- coding:UTF-8 -*-

import wx

import groupRename
import groupNum
	 
class ButtonBox(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		self.addOpenBox(sizer)
		self.addRenameGroup(sizer)
		self.addNumGroup(sizer)
		self.addPreviewButton(sizer)
		self.addRenameButton(sizer)
		self.addExportButton(sizer)
		self.SetSizer(sizer)


	def addOpenBox(self, sizer):
		box = wx.BoxSizer(wx.VERTICAL)
		self.addOpenFileButton(box)
		self.addOpenFolderButton(box)
		sizer.Add(box,  0, flag=wx.LEFT | wx.ALIGN_CENTER_VERTICAL, border=10)

	def addOpenFileButton(self, sizer):
		self.buttonOpenFile = wx.Button(self, -1, u"打开文件")
		sizer.Add(self.buttonOpenFile, 0, flag=wx.TOP, border=0)


	def addOpenFolderButton(self, sizer):
		self.buttonOpenFolder = wx.Button(self, -1, u"打开目录")
		sizer.Add(self.buttonOpenFolder, 0, flag=wx.TOP, border=10)


	def addRenameGroup(self, sizer):
		self.renameGroup = groupRename.RenamePanel(self)
		sizer.Add(self.renameGroup, flag=wx.LEFT, border=10)

	def addNumGroup(self, sizer):
		self.numGroup = groupNum.NumPanel(self)
		sizer.Add(self.numGroup, flag=wx.LEFT, border=1)

	def addPreviewButton(self, sizer):
		self.buttonPreview = wx.Button(self, -1, u"预览")
		sizer.Add(self.buttonPreview, 0, flag=wx.LEFT | wx.ALIGN_CENTER_VERTICAL, border=10) 

	def addRenameButton(self, sizer):
		self.buttonRename = wx.Button(self, -1, u"执行重命名")
		sizer.Add(self.buttonRename, 0, flag=wx.LEFT | wx.ALIGN_CENTER_VERTICAL, border=10)

	def addExportButton(self, sizer):
		self.buttonExport = wx.Button(self, -1, u"导出Excel")
		sizer.Add(self.buttonExport, 0, flag=wx.LEFT | wx.ALIGN_CENTER_VERTICAL, border=10)

	def reset(self):
		self.renameGroup.reset()
		self.numGroup.reset()

#---------------------------------------------------------------------------
class TestFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, u'button panel', size=(1024,120))
		self.mainPanel = wx.Panel(self, -1, style=0)
		self.mainSizer = wx.BoxSizer(wx.VERTICAL)

		self.buttonBox = ButtonBox(self.mainPanel)

		self.mainSizer.Add(self.buttonBox, 1, wx.RIGHT | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)
		self.mainPanel.SetSizer(self.mainSizer)

def test():
	app = wx.PySimpleApp()
	frame = TestFrame()
	frame.Show(True)
	app.MainLoop()

if __name__ == '__main__':
	test()