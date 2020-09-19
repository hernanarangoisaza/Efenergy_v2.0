import wx
import wx.grid

app = wx.App(False)


class InfoPane(wx.grid.Grid):
    def __init__(self, parent):
        wx.grid.Grid.__init__(self, parent)

        # Set up the presentation
        self.SetRowLabelSize(0)
        self.CreateGrid(1, 6)

        self.SetColLabelAlignment(wx.ALIGN_LEFT, wx.ALIGN_CENTRE)
        self.SetColLabelValue(0, "Name")
        self.SetColLabelValue(1, "Status")
        self.SetColLabelValue(2, "")
        self.SetColLabelValue(3, "File")
        self.SetColLabelValue(4, "Last Action")
        self.SetColLabelValue(5, "Other Info")

frame = wx.Frame(None)
panel = wx.Panel(frame)
info_pane = InfoPane(panel)

note_sizer = wx.BoxSizer()
note_sizer.Add(info_pane, 1, wx.EXPAND)

panel.SetSizer(note_sizer)
frame_sizer = wx.BoxSizer(wx.VERTICAL)
frame_sizer.Add(panel, 1, wx.EXPAND)
frame.SetSizerAndFit(frame_sizer)
frame.Show()

app.MainLoop()