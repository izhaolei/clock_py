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
        wx.ListBox.Insert(self, item, pos)
        self.__ItemCount += 1
              
      
class SketchFrame(wx.Frame):
    Clock = None
    LST = None

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Degree Measure")
        self.SetMinSize((700, 450))
        sz = wx.FlexGridSizer(1, 2, 0, 0)
        self.Clock = AnalogClock(self,-1, wx.DefaultPosition)
        self.Clock.SetClockStyle(SHOW_MINUTES_HAND|SHOW_MINUTES_TICKS|TICKS_CIRCLE)
        self.Clock.SetDegree(0)
        self.SetSize((400, 350))
        sz.Add(self.Clock, 0, wx.GROW)
        self.LST = ItemList(self, -1, size=(200, 200))
        self.LST.SetMinSize((200, 200))
        sz.Add(self.LST, 0, wx.GROW)
        sz.AddGrowableCol(0, 1)
        sz.AddGrowableCol(1, 0)
        sz.AddGrowableRow(0, 0)
        self.SetSizer(sz)
        self.Fit()

        
if __name__ == '__main__':
    app = wx.App()
    frame = SketchFrame(None)
    wx.FutureCall(100,frame.Clock.SetDegree, 270)
    wx.FutureCall(1200,frame.Clock.SetDegree, 50)
    wx.FutureCall(2000,frame.Clock.SetDegree, 180)
    frame.Show(True)
    lst = range(1, 100)  #TestCode
    for i in lst:  #TestCode
        frame.LST.Insert(str(i))  #TestCode
    app.MainLoop()
