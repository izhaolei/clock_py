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

        sz = wx.GridBagSizer(2, 2)

        self.Clock = AnalogClock(self,-1, wx.DefaultPosition)

        self.Clock.SetClockStyle(SHOW_MINUTES_HAND|SHOW_MINUTES_TICKS|TICKS_CIRCLE)

        self.Clock.SetDegree(0)

        sz.Add(self.Clock,pos= (0,0),flag= wx.GROW)

        self.LST = ItemList(self, -1, size=(200, 200))

        self.LST.SetMinSize((200, 200))

        self.Bind(wx.EVT_LISTBOX, self.EvtListBox, self.LST)

        sz.Add(self.LST, pos=(0,1),flag= wx.EXPAND)

        self.Text = wx.TextCtrl(self, -1, "The Degree is:", 

                (0, 0))

        sz.Add(self.Text, pos=(1,0), span=(1,2),flag=wx.ALIGN_CENTER)

        sz.AddGrowableCol(0)

        sz.AddGrowableRow(0)

        self.SetSizer(sz)

        self.Fit()



    def EvtListBox(self, event):



        self.Clock.SetDegree(self.DegreeData[event.GetSelection()])

        self.Text.Replace(0,18,"The Degree is:"+(str)(self.DegreeData[event.GetSelection()]))



    def RefreshData(self,data):



        self.DegreeData=data




