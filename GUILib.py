import wx
from analogclock import *
              


class ItemList(wx.ListBox):

    __ItemCount = 0

    def __init__(self, parent, ID, size=(200, 200)):
        wx.ListBox.__init__(self, parent, ID, size)
        self.SetBackgroundColour("white")

    def Insert(self, item, pos=None):
        if pos == None:
            pos = self.__ItemCount
        wx.ListBox.Insert(self, "Degree" + item, pos)
        self.__ItemCount += 1
              
      
class SketchFrame(wx.Frame):
    Clock = None
    LST = None
    Text=None
    DegreeData=[]

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Degree Measure")
        self.SetMinSize((700, 450))
        sz = wx.FlexGridSizer(2, 2, 0, 0)
        self.Clock = AnalogClock(self,-1, wx.DefaultPosition)
        self.Clock.SetClockStyle(SHOW_MINUTES_HAND|SHOW_MINUTES_TICKS|TICKS_CIRCLE)
        self.Clock.SetDegree(0)
        self.SetSize((400, 350))
        sz.Add(self.Clock, 0, wx.GROW)
        self.LST = ItemList(self, -1, size=(200, 200))
        self.LST.SetMinSize((200, 200))
        self.Bind(wx.EVT_LISTBOX, self.EvtListBox, self.LST)
        sz.Add(self.LST, 0, wx.GROW)
        self.Text = wx.TextCtrl(self, -1, "The Degree is:", 
                (100, 30))
        sz.Add(self.Text, 0, wx.ALIGN_CENTER)
        sz.AddGrowableCol(0, 1)
        sz.AddGrowableCol(1, 0)
        sz.AddGrowableRow(0, 0)
        self.SetSizer(sz)
        self.Fit()

    def EvtListBox(self, event):

        self.Clock.SetDegree(self.DegreeData[event.GetSelection()])
        self.Text.Replace(0,18,"The Degree is:"+(str)(self.DegreeData[event.GetSelection()]))

    def RefreshData(self,data):

        self.DegreeData=data

