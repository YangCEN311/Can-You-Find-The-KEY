import wx
from src import gameManager
from database import databaseManager

class MyFrame(wx.Frame):
    GM = gameManager.gManager
    DBM = databaseManager.dbManager
    
    nameInput = wx.TextCtrl
    rankingList = wx.ListCtrl
    def __init__(self, *args, **kwds):
        
        super(MyFrame, self).__init__(*args, **kwds)
        panel = wx.Panel(self)
        
        #sub1--
        sub_panel1 = wx.Panel(panel, size=(300, 40))
        btn1 = wx.Button(sub_panel1, label="開始遊戲", pos=(10, 10))
        btn1.Bind(wx.EVT_BUTTON, self.on_button_click)
        
        self.nameInput = wx.TextCtrl(sub_panel1, pos=(160, 10), size=(80, 20))

        text = wx.StaticText(sub_panel1, label="玩家名稱:", pos=(100, 14))
        
        #sub1--
        #sub2--
        sub_panel2 = wx.Panel(panel)
        
        self.rankingList = wx.ListCtrl(sub_panel2, size=(300, 300), style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.rankingList.InsertColumn(0, 'Rank', width=50)
        self.rankingList.InsertColumn(1, 'Name', width=100)
        self.rankingList.InsertColumn(2, 'Score', width=100)
        
        sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer2.Add(self.rankingList, proportion = 2, flag= wx.EXPAND, border= 10)
        
        sub_panel2.SetSizer(sizer2)
        #sub2--
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(sub_panel1, proportion = 1, flag= wx.ALL, border= 5)
        sizer.Add(sub_panel2, proportion = 2, flag= wx.ALL, border= 5)
        
        panel.SetSizer(sizer)
        panel.SetBackgroundColour(wx.Colour(255,255,255))
        
        self.DBM = databaseManager.dbManager()
        
        self.update_ranking()

    def update_ranking(self):
        self.rankingList.DeleteAllItems()
        sorted_users = self.DBM.search()
        for i in range(len(sorted_users)):
            self.rankingList.InsertItem(i, str(i+1))
            self.rankingList.SetItem(i, 1, sorted_users[i][1])
            self.rankingList.SetItem(i, 2, str(sorted_users[i][2]))

    def on_button_click(self, event):
        player_name = self.nameInput.GetValue()
        self.GM = gameManager.gManager(player_name)
        score = self.GM.play()
        self.DBM.insert(player_name, score)
        self.update_ranking()
    

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame(None, title="Lobby", size=(300, 400))
    frame.Show(True)
    app.MainLoop()
