#IMPORTING LIBRARIES
from matplotlib import pyplot as plt
import os
import numpy as np
from PIL import Image,ImageFilter
import cv2
from PIL.ImageFilter import (
 BLUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
 EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
        )
#INPUT DATA QUESTIONS
folder_path=input('put folder path here')
ask1=input('wanna add some filters ? (Y/N)')
ask2 = int(input('''In which format would you like to receive the output?
1. PNG
2. JPG (also known as JPEG)
Enter the number of the format: '''))

if ask2 == 1:
    extension = '.png'
elif ask2 == 2:
    extension = '.jpg'
else:
    print('INVALID!! File extension not available yet')

#FOLDER LOOPING
for filename in os.listdir(folder_path):
    complete_path=os.path.join(folder_path,filename)

#FACE_DETECTION
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img = cv2.imread(complete_path)
    imgv2=Image.open(complete_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)


    #filter_work_optional..

    if ask1=='Y':
        var_2=int(input('''You can select any one filter from below and enter associated number,
        ~~~~~~~.........~~~~~~~~~~~~~~
        BLUR ()>>1
        DETAIL()>>2
        EDGE_ENHANCE()>>3
        EDGE_ENHANCE_MORE()>>4
        EMBOSS()>>5
        SHARPEN()>>6
        SMOOTH()>>7
        SMOOTH_MORE()>>8
        '''))
        if var_2==1:
            imgv2=imgv2.filter(BLUR)
        elif var_2==2:
            imgv2=imgv2.filter(DETAIL)
        elif var_2==3:
            imgv2=imgv2.filter(EDGE_ENHANCE)
        elif var_2==4:
            imgv2=imgv2.filter(EDGE_ENHANCE_MORE)
        elif  var_2==5:
            imgv2=imgv2.filter(EMBOSS)
        elif  var_2==6:
            imgv2=imgv2.filter(SHARPEN)
        elif var_2==7:
            imgv2=imgv2.filter(SMOOTH)
        elif  var_2==8:
            imgv2=imgv2.filter(SMOOTH_MORE)
        else:
            continue


#EXTRACTING COORDINATES
    for (a,b,c,d) in faces:
        cropped = imgv2.crop((a - c // 4, b - d // 2, a + 5 * c // 4, b + 3 * d // 2))
        #SAVING IMAGES IN FOLDER
        output_name=('output'+str(filename)+str('.')+ extension)
        cropped.save(output_name)


print('''BYE!thanks for using ,, '
                          -V∆R∆D
•_• •_• •_• •_• •_• •_• •_• •_• •_• •_• •_• •_• •_• •_• •_• •_• •_• •_• •_• •_• •_• •_• •_• •_• •_• •_• •_• •_• •_• ''')

