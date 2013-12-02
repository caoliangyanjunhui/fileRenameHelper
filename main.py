# -*- coding:UTF-8 -*-

import wx
import buttonPanel
import grid

class ClientFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(
			self, None, -1, u'办证利器-业务管理 v0.0.4', size=(800,600)
			)

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

	def bindEvents(self):
		self.buttonBox.buttonOpen.Bind(wx.EVT_BUTTON, self.onOpenButtonClick)

	def onOpenButtonClick(self, evt):
		dlg = wx.DirDialog(self, u"选择要批处理的文件夹",
						  style=wx.DD_DEFAULT_STYLE
						   | wx.DD_DIR_MUST_EXIST
						   #| wx.DD_CHANGE_DIR
						   )
		if dlg.ShowModal() == wx.ID_OK:
			self.folderPath = dlg.GetPath()
			print 'folder selected: ', self.folderPath
		dlg.Destroy()


def main():
	app = wx.PySimpleApp()
	frame = ClientFrame()
	frame.Show(True)
	app.MainLoop()

if __name__ == '__main__':
	main()