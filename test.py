import GUILib
import wx

app = wx.App()
Frame = GUILib.SketchFrame(None)
Frame.Show(True)
Frame.RefreshData([20,50,57,80])#这个就是接口传入数组
for i in range(1,5):
    Frame.LST.Insert(str(i)) 
app.MainLoop()
