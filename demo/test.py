# -*- coding: utf-8 -*-
# @Author: chien
# @Email : bill0808fine@gmail.com
# @Date:   2019-06-06 23:43:09
# @Last Modified by:   chien
# @Last Modified time: 2019-06-08 02:40:35


import os
import cv2
path = './dataset1/'
files = os.listdir(path)
if('.DS_Store' in files):
    files.remove('.DS_Store')


def changename(files):
    i = 58
    for name in files:
        newname = path+'image%03d.jpg'%i
        os.rename(path+name , newname )
        i+=1

# changename(files)


def resize_and_sace(path,name,newpath):
    pathname = path+name
    pic = cv2.imread(pathname)


    ############################################################
    pic = pic[100:1700,400:2480]
    padding = (pic.shape[1] - pic.shape[0])//2
    pic = cv2.copyMakeBorder(pic,padding,padding,0,0,cv2.BORDER_CONSTANT)
    ############################################################

    # print(pic.shape)
    # height , width = pic.shape[0:2]
    # new_pic = cv2.resize(pic,(width//2,height//2))
    # pic = pic[100:1700,640:2240]
    new_pic = cv2.resize(pic,(512,512))

    if not os.path.isdir(newpath):
        os.mkdir(newpath)
    cv2.imwrite(os.path.join(newpath,name) , new_pic)
    # cv2.imwrite(os.path.join(newpath,name) , pic)

print(files)
for name in files:
    resize_and_sace(path,name,"mydataset6")



# def resize_and_sace(path,name):
#     pathname = path+name
#     pic = cv2.imread(pahtname)
#     pic = pic[100:1700,640:2240]
#     new_pic = cv2.resize(pic,(512,512))
#     cv2.imwrite("./mydataset/"+name , new_pic)

# print(files)
# for name in files:
#     # print(name)
#     resize_and_sace(path,name)
#     # pic = cv2.imread(path+name)
#     # pic = pic[100:1700,640:2240]
#     # new_pic = cv2.resize(pic,(512,512))
#     # cv2.imwrite("./mydataset/"+name , new_pic)
    
# pic = cv2.imread(name)
# pic = pic[100:1700,640:2240]
# new_pic = cv2.resize(pic,(512,512))
# cv2.imwrite("test.jpg" , new_pic)


