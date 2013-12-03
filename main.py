# -*- coding:UTF-8 -*-

import wx
import buttonPanel
import grid
import renameFile
import csvHandler
import os

class ClientFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(
			self, None, -1, u'文件重命名工具 v0.6', size=(1000,600)
			)
		self.fileList = None
		self.showList = None
		self.folderPath = None
		self.lastSaveFolderPath = os.getcwd()
		self.lastOpenFolderPath = os.getcwd()
		self.lastOpenFileFolderPath = os.getcwd()

		self.addIcon()
		self.addStatusBar()
		self.splitWindow = wx.SplitterWindow(self)
		self.mainPanel = self.newMainPanel(self.splitWindow)
		self.infoPanel = self.newInfoPanel(self.splitWindow)
		self.splitWindow.SplitHorizontally(self.mainPanel, self.infoPanel, -100)
		self.splitWindow.SetMinimumPaneSize(20)
		self.bindEvents()


	def newMainPanel(self, parent):
		mainPanel = wx.Panel(parent, -1)
		mainSizer = wx.BoxSizer(wx.VERTICAL)

		self.buttonBox = buttonPanel.ButtonBox(mainPanel)
		mainSizer.Add(self.buttonBox, proportion=0, flag= wx.TOP, border=5)

		self.grid = grid.FileTableGrid(mainPanel)
		mainSizer.Add(self.grid, proportion= 1, flag=wx.TOP | wx.EXPAND,  border=5)

		mainPanel.SetSizer(mainSizer)
		return mainPanel

	def newInfoPanel(self, parent):
		infoPanel = wx.Panel(parent)
		infoPanel.SetBackgroundColour("white")

		vbox = wx.BoxSizer(wx.VERTICAL)
		self.infoText = wx.TextCtrl(infoPanel, -1, style=wx.TE_MULTILINE)
		vbox.Add(self.infoText, proportion=1, flag=wx.EXPAND | wx.ALL)
		infoPanel.SetSizerAndFit(vbox)
		return infoPanel

	def addStatusBar(self):
		self.statusBar = wx.StatusBar(self)
		self.SetStatusBar(self.statusBar)

	def addIcon(self):
		icon = wx.Icon('ico/rename32.ico', wx.BITMAP_TYPE_ICO)
		self.SetIcon(icon)

	def bindEvents(self):
		self.buttonBox.buttonOpen.Bind(wx.EVT_BUTTON, self.onOpenButtonClick)
		self.buttonBox.buttonExport.Bind(wx.EVT_BUTTON, self.onExportButtonClick)
		self.buttonBox.buttonPreview.Bind(wx.EVT_BUTTON, self.onPreviewButtonClick)
		self.buttonBox.buttonRename.Bind(wx.EVT_BUTTON, self.onRenameButtonClick)

	def onOpenButtonClick(self, evt):
		self.folderPath = None
		dlg = wx.DirDialog(self, u"选择要批处理的文件夹",
						  style=wx.DD_DEFAULT_STYLE
						   | wx.DD_DIR_MUST_EXIST
						   #| wx.DD_CHANGE_DIR
						   )
		if dlg.ShowModal() == wx.ID_OK:
			self.folderPath = dlg.GetPath()

		dlg.Destroy()

		if self.folderPath:
			self.showStatus(u'正在扫描文件……')
			self.fileList, self.showList = renameFile.FileReader().readAllFrom(self.folderPath)
			self.grid.setData(self.showList)
			self.showInfo(self.folderPath)
			self.showStatus(u'打开成功')
		else:
			self.showInfo(u'未打开有效文件夹')
			self.showStatus(u'取消')

	def onExportButtonClick(self, evt):
		if not self.showList:
			self.showInfo(u'尚未指定需要处理的文件夹，无数据可供导出')
			self.showStatus(u'导出失败')
			return
		
		dlg = wx.FileDialog(
			self, message=u"文件存为……", defaultDir=self.lastSaveFolderPath, 
			defaultFile=u"导出文件表格.csv", wildcard=u'逗号分隔数据表(*.CSV)|*.csv|All files (*.*)|*.*', style=wx.SAVE
			)
		if dlg.ShowModal() == wx.ID_OK:
			filePath = dlg.GetPath()
		else:
			return

		try:
			csvHandler.CSV().write(filePath, self.showList)
		except Exception, e:
			self.infoText.SetValue(str(e))
			self.showStatus(u'导出失败')
			return
		self.showInfo(filePath)
		self.showStatus(u'导出完成')

	def onPreviewButtonClick(self, evt):
		self.preview()
		self.showInfo(u'预览')

	def onRenameButtonClick(self, evt):
		self.preview()
		self.rename()
		self.showInfo(u'重命名文件数量:' + str(len(self.fileList)))
		self.showStatus(u'重命名执行完成')

	def preview(self):
		operations = self.getOperations()
		self.fileList, self.showList = renameFile.FileRename(self.fileList, operations).preview()
		self.grid.setData(self.showList)

	def rename(self):
		renameFile.FileRename(self.fileList).excute()

	def showInfo(self, text):
		if not text: return
		try:
			self.infoText.SetValue(text)
		except Exception, e:
			self.infoText.SetValue(str(e))

	def showStatus(self, text):
		self.statusBar.SetStatusText(text, 0)


	def getOperations(self):
		operations = {}
		operations['newNameOperation'] = self.buttonBox.renameGroup.getSelection()
		operations['newName'] = self.buttonBox.renameGroup.getNewName()
		operations['addNumOperation'] = self.buttonBox.numGroup.getSelection()
		operations['startNum'] = self.buttonBox.numGroup.getStartNum()
		return operations
		

def main():
	app = wx.PySimpleApp()
	frame = ClientFrame()
	frame.Show(True)
	app.MainLoop()

if __name__ == '__main__':
	main()