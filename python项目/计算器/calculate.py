# coding=utf-8
# __author__ = 'bingzheng song'

from __future__ import division
import wx
class MyFrame(wx.Frame):
    def __init__(self,title,size):
        super(MyFrame,self).__init__(None,title=title,size=size)
        self.w=size[0]
        self.h=size[1]
        self.equaltion=""
        self.initUI()
        self.Centre()
        self.Show()
    def initUI(self):
        vbox=wx.BoxSizer(wx.VERTICAL)
        self.textPrint=wx.TextCtrl(self,style=wx.TE_READONLY|wx.ALIGN_RIGHT,size=(self.w,self.h*0.15))
        self.textPrint.SetFont(wx.Font(self.h*0.1,wx.SWISS,wx.NORMAL,wx.NORMAL))
        vbox.Add(self.textPrint, flag=wx.EXPAND)
        labels = ["7", "8", "9", "+", "exit",
                "4", "5", "6", "-", "del",
                "1", "2", "3", "*", "AC",
                "0", ".", "%", "/", "=",
                "(", ")", "00", "", ""]
        gridSizer=wx.GridSizer(5, 5)
        for label in labels:
            button=wx.Button(self,label=label)
            button.SetFont(wx.Font(25,wx.SWISS,wx.NORMAL,wx.NORMAL))
            self.createHandler(button,label)
            gridSizer.Add(button,1,wx.EXPAND)
        vbox.Add(gridSizer, proportion=1,flag=wx.EXPAND)
        self.SetSizer(vbox)
    def createHandler(self,button,label):
        items_set = ("exit","del","AC","=")
        if label not in items_set:
            self.Bind(wx.EVT_BUTTON,self.onAppend,button)
        elif label=="exit":
            self.Bind(wx.EVT_BUTTON,self.onExit,button)
        elif label=="del":
            self.Bind(wx.EVT_BUTTON, self.onDel, button)
        elif label=="AC":
            self.Bind(wx.EVT_BUTTON, self.onAC, button)
        else:
            self.Bind(wx.EVT_BUTTON, self.onTarget, button)
    def onAppend(self,event):
        eventButton=event.GetEventObject()
        label=eventButton.GetLabel()
        self.equaltion+=label
        self.textPrint.SetValue(self.equaltion)
    def onDel(self,event):
        self.equaltion=self.equaltion[:-1]
        self.textPrint.SetValue(self.equaltion)
    def onAC(self,event):
        self.equaltion=""
        self.textPrint.SetValue(self.equaltion)
    def onTarget(self,event):
        try:
            if self.equaltion.isalpha():
                self.textPrint.SetValue(self.equaltion)
            else:
                result=eval(self.equaltion)
                self.equaltion=""
                self.textPrint.SetValue(str(result))
        except SyntaxError:
            self.textPrint.SetValue("语法错误".decode("utf-8"))
            self.equaltion=""
    def onExit(self,event):
        self.Close()
app=wx.App()
frame=MyFrame("这是宋炳政写的计算器".decode("utf-8"),(600,450))
app.MainLoop()

# 在整个设计中需要注意
# 首先初始化一个BoxSizer,BoxSizer(wx.VERTICAL)带有一个参数，表示是水平还是垂直
# 接下来就可以往BoxSizer中添加控件，控件种类有很多，他们使用方法大致类似
# 比如添加一个Button，需要指定添加到哪个画布中
# BoxSizer.Add(x,proprotion,flag)添加时有3个参数
# 一是要添加的控件，二是添加的效果,wx.EXPAND表示行填充,三是列填充比例
# gridSizer=wx.GridSizer(4,4)声明一个4行4列的布局

