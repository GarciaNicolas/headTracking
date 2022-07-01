
# mp4ToJpeg
#    >python mp4ToJpeg
#    >videoName (only the name, without any extension)

import os
import cv2
vidName = input()
vidcap = cv2.VideoCapture(vidName+'.mp4')
path = './'+vidName 

os.mkdir(vidName)
os.chdir(path)

success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)          
  success,image = vidcap.read()                           #(Bool, image)
  print('Read a new frame: ', success)
  count += 1



  # I suppose it removes al JPG images
  #vidcap.release()
  #cv.destroyAllWindows()