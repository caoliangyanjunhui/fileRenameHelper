# -*- coding:UTF-8 -*-
import wx

class NumPanel(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent, -1)
		#self.SetBackgroundColour(wx.BLUE)

		sizer = wx.BoxSizer(wx.VERTICAL)
		self.addRadioBox(sizer)
		self.addTextStartNum(sizer)
		self.SetSizer(sizer)

	def addRadioBox(self, sizer):
		options = [u'加前缀', u'加后缀']
		self.rb = wx.RadioBox(
				self, -1, u"文件名", wx.DefaultPosition, wx.DefaultSize,
				options, 2, wx.RA_SPECIFY_COLS
				)
		sizer.Add(self.rb, 0, wx.ALL, 1)

	def addTextStartNum(self, sizer):
		self.newName = wx.TextCtrl(self, -1, "001", size=(126, -1))
		sizer.Add(self.newName, flag=wx.LEFT | wx.TOP, border=1)

#---------------------------------------------------------------------------
class TestFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(
			self, None, -1, u'radio box', size=(600,400)
			)
		self.mainPanel = wx.Panel(self, -1, style=0)
		self.mainSizer = wx.BoxSizer(wx.VERTICAL)

		self.radioBox = NumPanel(self.mainPanel)

		self.mainSizer.Add(self.radioBox, 1, wx.RIGHT | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)
		self.mainPanel.SetSizer(self.mainSizer)

def test():
	app = wx.PySimpleApp()
	frame = TestFrame()
	frame.Show(True)
	app.MainLoop()

if __name__ == '__main__':
	test()