# -*- coding: utf-8 -*-
import wx

import time

from analogclock import *

class DegreeList(wx.ListBox):

    __ItemCount = 0

    def __init__(self, parent, ID, size=(200, 200)):
        wx.ListBox.__init__(self, parent, ID, size)
        self.SetBackgroundColour("white")

    def Insert(self, degree, pos=None):
        if pos == None:
            pos = self.__ItemCount
        wx.ListBox.Insert(self, "Degree " + str(degree), pos)
        self.__ItemCount += 1

class SketchFrame(wx.Frame):

    Clock = None
    List = None
    Statusbar = None
    Text = None
    DegreeData=[]
    de=0

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Degree Measure")
        self.SetMinSize((700, 450))
        self.Statusbar = self.CreateStatusBar()
        self.timer = wx.PyTimer(self.Notify)
        self.timer.Start(100)
        self.Notify()
        menu = wx.Menu()
        exit = menu.Append(-1, "Exit")
        self.Bind(wx.EVT_MENU, self.OnExit, exit)
        Menubar = wx.MenuBar()
        Menubar.Append(menu, "Files")
        self.SetMenuBar(Menubar)

        sz = wx.GridBagSizer(0, 0)
        sz.AddSpacer((-1,5), pos=(0,0))
        sz.AddSpacer((-1,5), pos=(2,0))

        self.Text = wx.StaticText(self, -1, style=wx.ALIGN_CENTER)
        self.Text.SetMaxSize((-1,17))
        self.Text.SetBackgroundColour(self.GetBackgroundColour())
        sz.Add(self.Text, pos=(1,0), flag=wx.ALIGN_CENTER, border=5)

        self.Clock = AnalogClock(self,-1, wx.DefaultPosition)
        self.Clock.SetClockStyle(SHOW_MINUTES_HAND|SHOW_MINUTES_TICKS|TICKS_CIRCLE)
        self.Clock.SetDegree(0)
        sz.Add(self.Clock, pos=(3,0), flag=wx.GROW)

        self.List = DegreeList(self, -1, size=(200, 200))
        self.List.SetMinSize((200, 200))
        self.Bind(wx.EVT_LISTBOX, self.EvtListBox, self.List)
        sz.Add(self.List, pos=(0,1), span=(4,1), flag= wx.EXPAND)

        self.Statusbar.SetStatusText("No degree selected!")
        self.Text.SetLabel("No degree selected!")

        sz.AddGrowableCol(0)
        sz.AddGrowableRow(3)
        self.SetSizer(sz)
        self.Fit()


    def OnExit(self, event):
        self.Close()


    def EvtListBox(self, event):
        self.ShowDegree()
        self.timer.Start(100)
        self.ShowData()
    def Notify(self):
        self.Statusbar.SetStatusText("Degree: %.4f°"%(self.de))
        #self.Text.SetLabel("Degree: %.4f°"%(self.de))

    def RefreshData(self, data):
        self.DegreeData = data
        diff = len(data) - self.List.GetCount()
        while diff:
            if diff > 0:
                self.List.Insert(self.List.GetCount() + 1) 
            if diff < 0:
                self.List.Delete(self.List.GetCount() - 1) 
            diff = len(data) - self.List.GetCount()
        self.ShowDegree()

    def ShowDegree(self):
        self.de = self.DegreeData[self.List.GetSelection()]
        while self.de < 0:
            self.de = 360 + self.de
        while self.de >= 360:
            self.de = self.de - 360

        self.Clock.SetDegree(self.de)
        
