import cv2
import matplotlib.pyplot as plt

vid = cv2.VideoCapture(0)

fd = cv2.CascadeClassifier(
     cv2.data.haarcascades+
     'haarcascade_frontalface_default.xml')

sd = cv2.CascadeClassifier(
    cv2.data.haarcascades+
     'haarcascade_smile.xml')
while True:
    flag , img = vid.read()
    if flag is True:
        img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
#         x1,y1,w,h = (800,400,700,200)
        faces = fd.detectMultiScale(img_gray, 1.1, 5)
        for x1,y1,w,h in faces:
            img_crop = img[y1:y1+h,x1:x1+w,:].copy()
            smiles = sd.detectMultiScale(img_crop,1.1,5)
            if len(smiles) == 1:
                print("Smile detected")
                xs,ys,ws,hs = smiles[0]
                cv2.rectangle(
                img,pt1 = (x1+xs,y1+ys), pt2 = (x1+xs+ws,y1+ys+hs),
                         color = (0,255,0)
                         )
                
            cv2.rectangle(
                img,pt1 = (x1,y1), pt2 = (x1+w,y1+h),
                         color = (255,0,0),thickness = 5
                         )
            
        cv2.imshow('Live',img[:,::-1])
        key = cv2.waitKey(1)
        if key == ord('a'):
            break
    else:
        print("Not Running")
        break
vid.release()
cv2.destroyAllWindows()