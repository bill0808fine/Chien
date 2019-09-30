# -*- coding: utf-8 -*-
# @Author: chien
# @Email : bill0808fine@gmail.com
# @Date:   2019-06-06 23:43:09
# @Last Modified by:   chien
# @Last Modified time: 2019-06-08 11:24:03


import json
import cv2

#load josn file
with open('test.json', 'r') as f:
    data = json.load(f)

    
images = data['images']
for image in images:
    # print(image['file_name'][-12:])
    image['file_name'] = image['file_name'][-12:]

for i in range(len(images)):
    print(data['images'][i]['file_name'])

with open("mytest.json","w") as f:
    json.dump(data,f)
    print("success...")