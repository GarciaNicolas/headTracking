import cv2 as cv
import os


dir = 'encierroSanFermin-recortado'                     #Directory's path

with os.scandir(dir) as imgs:                           #Call as imgs the directory's scan
    os.chdir(dir)                                       #Change actual directory to the new one
    counter = 0
    for imgName in imgs:
        img = cv.imread(imgName.name)
        cv.imshow('Frame {:d}'.format(counter), img)
        cv.waitKey(0)
        counter +=1
        cv.destroyWindow('Frame {:d}'.format(counter-1))
        #Add any function or effect
           

#cv.waitKey(0)

    #img = cv.imread(imgName.name)
    #cv.imshow('Frame', img)                            To show the frames in screen



    #gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)         To convert into gray
    #cv.imshow('Gray', gray)

