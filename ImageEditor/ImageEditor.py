import tkinter as tk
import UI_functions

def on_enter(event):
    event.widget['bg'] = "#656565"

def on_leave(event):
    event.widget['bg'] = '#585858'

root = tk.Tk()
##ウインドウ
root.title("tkinterのウインドウ")
root.state("zoomed")
root['background']="#515151"
##フレーム
#メニューバー
frame_menu = tk.Frame(root,height=26, background="#585858")
frame_menu.pack(fill=tk.X, side=tk.TOP)
#右サイドバー
frame_side = tk.Frame(root,width=460,background="#585858")
frame_side.pack(fill=tk.Y, side=tk.RIGHT)
#トップバー
frame_top = tk.Frame(root,height=24, background="#656565")
frame_top.pack(side=tk.TOP)
#メインフレーム
frame_main = tk.Frame(root,height=1004, width=1456,background="#FFFFFF")
frame_main.pack(side=tk.BOTTOM)
frame_tool = tk.Frame(frame_main, width=40, height=100, background="#656565")
frame_tool.place(x=9, y=34)
text_arr = ["aiueo", "iueoa", "ueoai", "eoaiu", "oaiue"]
for i in range(len(text_arr)):
    button = tk.Button(frame_tool, relief="flat",height=2, text=text_arr[i],  background='#585858')
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    button.pack(side=tk.TOP)
root.mainloop()