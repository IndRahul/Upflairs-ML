import cv2,skimage

vid = cv2.VideoCapture(0)
while True:
    flag,img = vid.read()
    if flag:
        gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        red_img = cv2.subtract(img[:,:,-1],gray_img)
        th,red_binary = cv2.threshold(red_img,55,255,cv2.THRESH_BINARY)
        red_binary2 = skimage.morphology.remove_small_objects(
                                        red_binary.astype(bool),150)
        strel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10,10))
        red_binary3 = cv2.dilate(red_binary2.astype('uint8'),strel,iterations=1)
        red_binary4 = skimage.morphology.remove_small_holes(
                                    red_binary3.astype(bool),500
                        )
        labels = skimage.measure.label(red_binary4)
        rp = skimage.measure.regionprops(labels,red_binary4)
        img_orig = img.copy()
        if len(rp) > 0:
            (y1,x1,y2,x2) = rp[0].bbox
            cv2.rectangle(
                img_orig,
                pt1 = (x1,y1),pt2 = (x2,y2),
                color = (255,255,0),
                thickness=10
            )
        cv2.imshow('Preview',img_orig)
        key = cv2.waitKey(1)
        if key == ord('a'):
            break
            
vid.release() 
cv2.destroyAllWindows()
        