#-*- coding:UTF-8 -*-


import  wx

#---------------------------------------------------------------------------

class ClientPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)

        b = wx.Button(self, -1, "Create and Show a DirDialog", (50,50))
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)


    def OnButton(self, evt):
        # In this case we include a "New directory" button. 
        dlg = wx.DirDialog(self, "Choose a directory:",
                          style=wx.DD_DEFAULT_STYLE
                           #| wx.DD_DIR_MUST_EXIST
                           #| wx.DD_CHANGE_DIR
                           )

        # If the user selects OK, then we process the dialog's data.
        # This is done by getting the path data from the dialog - BEFORE
        # we destroy it. 
        if dlg.ShowModal() == wx.ID_OK:
            print 'You selected: %s\n' % dlg.GetPath()

        # Only destroy a dialog after you're done with it.
        dlg.Destroy()


class ClientFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(
			self, None, -1, u'文件批量重命名 v0.0.1', size=(800,600), 
			style=wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE)
		self.SetMinSize((640,480))
		self.CreateStatusBar(1, wx.ST_SIZEGRIP)

		mainPanel = wx.Panel(self, -1, style=0)
		mainSizer = wx.BoxSizer(wx.VERTICAL)

		openPanel = ClientPanel(mainPanel)

		mainSizer.Add(openPanel, 1, wx.EXPAND, 5)
		mainPanel.SetSizer(mainSizer)
def main():
	app = wx.PySimpleApp()
	frame = ClientFrame()
	frame.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()        