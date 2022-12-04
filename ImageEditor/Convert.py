from PIL import Image
import os
import numpy as np

after_size = 80

path_tool_icon = "./ImageEditor/icons"
list_tool_icon = os.listdir(path_tool_icon)
path_array_tool_icon = []
for fname in range(len(list_tool_icon)):
    if ".png" == os.path.splitext(list_tool_icon[fname])[1] and "block" not in os.path.splitext(list_tool_icon[fname])[0]:
        path_array_tool_icon.append(list_tool_icon[fname])
for i in range(len(path_array_tool_icon)):
    path = path_tool_icon+"/"+path_array_tool_icon[i]
    img = Image.open(path)
    b_img = np.array(img, np.uint8)
    # print(b_img.shape)
    img2 = Image.new(img.mode, (after_size, after_size), (255,255,255,0))
    img2.paste(img, (after_size//2-b_img.shape[0]//2, after_size//2-b_img.shape[1]//2))
    # img2.show()
    ppath = path_tool_icon[2:]+"/covert"+str(after_size)+path_array_tool_icon[i]+".png"
    img2.save(ppath)