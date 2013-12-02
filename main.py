# -*- coding:UTF-8 -*-

import wx
import buttonPanel
import grid
import renameFile
import csvHandler

class ClientFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(
			self, None, -1, u'文件重命名工具 v0.3', size=(800,600)
			)
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

	def onOpenButtonClick(self, evt):
		self.folderPath = None
		dlg = wx.DirDialog(self, u"选择要批处理的文件夹",
						  style=wx.DD_DEFAULT_STYLE
						   | wx.DD_DIR_MUST_EXIST
						   #| wx.DD_CHANGE_DIR
						   )
		if dlg.ShowModal() == wx.ID_OK:
			self.folderPath = dlg.GetPath()
			self.fileList, self.showList = renameFile.FileReader().readAllFrom(self.folderPath)
			self.grid.setData(self.showList)
			self.showInfo(self.folderPath)
			self.showStatus(u'文件夹打开成功')
		else:
			self.showStatus(u'未打开有效文件夹')
		dlg.Destroy()

	def onExportButtonClick(self, evt):
		try:
			filePath = csvHandler.CSV().write(self.showList)
		except Exception, e:
			self.infoText.SetValue(str(e))
			self.showStatus(u'导出失败')
			return
		self.showInfo(filePath)
		self.showStatus(u'导出完成')

	def showInfo(self, text):
		if not text: return
		try:
			self.infoText.SetValue(text)
		except Exception, e:
			self.infoText.SetValue(str(e))

	def showStatus(self, text):
		self.statusBar.SetStatusText(text, 0)


def main():
	app = wx.PySimpleApp()
	frame = ClientFrame()
	frame.Show(True)
	app.MainLoop()

if __name__ == '__main__':
	main()