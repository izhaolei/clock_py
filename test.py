#!/usr/bin/python
import GUILib
import wx

app = wx.PySimpleApp()
Frame = GUILib.SketchFrame(None)
Frame.Show(True)
for i in range(1,5):
    Frame.List.Insert('degree'+str(i))
Frame.RefreshData([20,50,57,80])
wx.FutureCall(3000,Frame.RefreshData,[23,50,57,80, -90])
wx.FutureCall(6000,Frame.RefreshData,[57.91321234,-80, -90])
wx.FutureCall(9000,Frame.RefreshData,[40.91321234,-80, -90,80])
wx.FutureCall(10000,Frame.RefreshData,[23,50,57, -90])
wx.FutureCall(11000,Frame.RefreshData,[57.91321234,-80, -90])
wx.FutureCall(12000,Frame.RefreshData,[40.91321234, -90,80])
wx.FutureCall(13000,Frame.RefreshData,[23,50,57,80, -90])
wx.FutureCall(14000,Frame.RefreshData,[57.91321234,-80, -90])
wx.FutureCall(15000,Frame.RefreshData,[40.91321234,-80, -90,80])
wx.FutureCall(16000,Frame.RefreshData,[23,50,57, -90])
wx.FutureCall(17000,Frame.RefreshData,[57.91321234,-80, -90])
wx.FutureCall(18000,Frame.RefreshData,[40.91321234, -90,80])
app.MainLoop()
