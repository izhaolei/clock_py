#!/usr/bin/python
import GUILib
import wx

app = wx.PySimpleApp()
Frame = GUILib.SketchFrame(None)
Frame.Show(True)
Frame.RefreshData([20,50,57,80])
wx.FutureCall(3000,Frame.RefreshData,[23,50,57,80, -90])
wx.FutureCall(6000,Frame.RefreshData,[57.91321234,-80, -90])
app.MainLoop()
