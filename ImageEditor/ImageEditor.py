import tkinter as tk
import os

class ui4imageEditor(tk.Frame):
    def on_enter(self,event):
        event.widget['bg'] = "#656565"
    def on_leave(self,event):
        event.widget['bg'] = '#585858'
    def displaybuttons(self, frame_tool):
            #画像ファイルの検索
            path_tool_icon = "./ImageEditor/icons"
            list_tool_icon = os.listdir(path_tool_icon)
            path_array_tool_icon = []
            for fname in range(len(list_tool_icon)):
                if ".png" == os.path.splitext(list_tool_icon[fname])[1] and "covert60" in os.path.splitext(list_tool_icon[fname])[0]:
                    path_array_tool_icon.append(list_tool_icon[fname])
            #ボタンの配置&画像の読み込み
            button = [None]*len(path_array_tool_icon)
            img = [None]*len(path_array_tool_icon)
            for i in range(len(path_array_tool_icon)):
                b_path = path_tool_icon[2:] + "/"+ path_array_tool_icon[i]
                # print(b_path)
                img[i] = tk.PhotoImage(file=b_path)
                img[i] = img[i].subsample(2,2)
                button[i] = tk.Button(frame_tool, width=40,height=33,compound="center",relief="flat",image=img[i],  background='#585858')
                button[i].bind("<Enter>", self.on_enter)
                button[i].bind("<Leave>", self.on_leave)
                button[i].pack(side=tk.TOP)
                button[i].image = img[i]
    def displaymenus(self):
        text_arr = ["ファイル", "編集", "選択", "ヘルプ"]
        #親
        menu_bar = tk.Menu(self.master,bg="#585858",activeborderwidth=5)
        self.master.config(menu=menu_bar,bg="#585858")
        # menu_bar.config(bg="#585858")
        #子のファイルメニュー
        file_menu = tk.Menu(menu_bar,tearoff=0,
        bg="#585858",foreground="#FFFFFF",activeborderwidth=5)
        menu_bar.add_cascade(label=text_arr[0], menu=file_menu)
        #ファイルメニューの子
        file_menu.add_command(label="新規作成")
        file_menu.add_command(label="開く")
        file_menu.add_command(label="保存")
        file_menu.add_command(label="名前を付けて保存")
        file_menu.add_separator()
        file_menu.add_command(label="エクスポート")
        file_menu.add_separator()
        file_menu.add_command(label="終了")

        #子の編集メニュー
        edit_menu = tk.Menu(menu_bar,tearoff=0)
        menu_bar.add_cascade(label=text_arr[1], menu=edit_menu)
        #子の選択メニュー
        select_menu = tk.Menu(menu_bar,tearoff=0)
        menu_bar.add_cascade(label=text_arr[2], menu=select_menu)
        #子のヘルプメニュー
        help_menu = tk.Menu(menu_bar,tearoff=0)
        menu_bar.add_cascade(label=text_arr[3], menu=help_menu)
    def displaycustommenu(self, frame, array):
        variable = tk.StringVar(self.master)
        variable.set(array[0])
        optionmenu = tk.OptionMenu(frame, variable, *array)
        optionmenu.configure(indicatoron=0,relief="flat",background="#585858",foreground="#FFFFFF",highlightthickness=0)
        optionmenu.pack(side=tk.LEFT)
    def __init__(self,master=None):
        super().__init__(master)
        self.pack()
        self.master.title("Class")
        self.master.state("zoomed")
        self.master['background']="#515151"
        frame_menu = tk.Frame(self.master,height=26, background="#585858")
        frame_menu.pack(fill=tk.X, side=tk.TOP)
        #メニューバー
        self.displaymenus()
        # text_arr = ["ファイル", "編集", "選択", "ヘルプ"]
        # self.displaycustommenu(frame_menu, text_arr)
        # text_arr = ["編集", "元に戻す", "やり直す","カット","コピー","ペースト"]
        # self.displaycustommenu(frame_menu, text_arr)
        #右サイドバー
        frame_side = tk.Frame(self.master,width=300,background="#585858")
        frame_side.pack(fill=tk.Y, side=tk.RIGHT)
        #トップバー
        frame_top = tk.Frame(self.master,height=24, background="#656565")
        frame_top.pack(side=tk.TOP)
        #メインフレーム
        frame_main = tk.Frame(self.master,height=1004, width=1456,background="#FFFFFF")
        frame_main.pack(side=tk.BOTTOM)
        #ツールバーフレーム
        frame_tool = tk.Frame(frame_main, width=35, height=100, background="#656565")
        frame_tool.place(x=11, y=34)
        self.displaybuttons(frame_tool)
        

root = tk.Tk()
app = ui4imageEditor(master=root)
app.mainloop()
# root.minsize(500,500)
# mb = tk.Menu(root)
# root.configure(menu=mb)
# file_menu = tk.Menu(mb)
# mb.add_cascade(label="file", menu=file_menu)
# root.mainloop()