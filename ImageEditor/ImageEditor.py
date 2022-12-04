import tkinter as tk
import UI_functions
import os


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
frame_side = tk.Frame(root,width=300,background="#585858")
frame_side.pack(fill=tk.Y, side=tk.RIGHT)
#トップバー
frame_top = tk.Frame(root,height=24, background="#656565")
frame_top.pack(side=tk.TOP)
#メインフレーム
frame_main = tk.Frame(root,height=1004, width=1456,background="#FFFFFF")
frame_main.pack(side=tk.BOTTOM)
frame_tool = tk.Frame(frame_main, width=35, height=100, background="#656565")
frame_tool.place(x=11, y=34)
#ツールバー
text_arr = ["aiueo", "iueoa", "ueoai", "eoaiu", "oaiue"]
#ツールバー画像の読み込み
path_tool_icon = "./ImageEditor/icons"
list_tool_icon = os.listdir(path_tool_icon)
path_array_tool_icon = []
for fname in range(len(list_tool_icon)):
    if ".png" == os.path.splitext(list_tool_icon[fname])[1] and "covert60" in os.path.splitext(list_tool_icon[fname])[0]:
    # if ".png" == os.path.splitext(list_tool_icon[fname])[1] and "covert60" not in os.path.splitext(list_tool_icon[fname])[0] and "block" not in os.path.splitext(list_tool_icon[fname])[0]:
        # print(list_tool_icon[fname])
        path_array_tool_icon.append(list_tool_icon[fname])
# print(path_array_tool_icon)
button = [None]*len(path_array_tool_icon)
img = [None]*len(path_array_tool_icon)
for i in range(len(path_array_tool_icon)):
    b_path = path_tool_icon[2:] + "/"+ path_array_tool_icon[i]
    # print(b_path)
    img[i] = tk.PhotoImage(file=b_path)
    img[i] = img[i].subsample(2,2)
    button[i] = tk.Button(frame_tool, width=40,height=33,compound="center",relief="flat",image=img[i],  background='#585858')
    button[i].bind("<Enter>", on_enter)
    button[i].bind("<Leave>", on_leave)
    button[i].pack(side=tk.TOP)
root.mainloop()