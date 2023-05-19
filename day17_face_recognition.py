# Recognition Step................  CONSIDER BELOW CODE.....

#CODE WITH SOME ERRORS..
"""import cv2
import pandas as pd
import face_recognition as fr

import numpy as np

vid = cv2.VideoCapture(0)
fd=cv2.CascadeClassifier(
            cv2.data.haarcascades+'haarcascade_frontalface_default.xml'
)

try:
    face_db = pd.read_csv('faces_data.tsv', index_col=0, sep='\t')
    data = {
        'name' : face_db['name'].values.tolist(),
        'encoding' : face_db['encoding'].values.tolist(),
    }
except Exception as e:
    print(e)
    data = {'name' : [], 'encoding' : []}

# print(data)

while True:
    flag, img=vid.read()
    if flag:
        faces = fd.detectMultiScale(
            cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),
            scaleFactor = 1.1,
            minNeighbors=5,
            minSize = (50,50)
        )

        if len(faces)==1:
            x,y,w,h = faces[0]
            img_face = img[y:y+h, x:x+w, :].copy()
            img_face= cv2.resize(img_face,(400,400),
                                 interpolation=cv2.INTER_CUBIC)
            #cv2.imwrite(f'{name}_{frameCount}.png', img_face)
            face_encoding = fr.face_encodings(img_face)

            if len(face_encoding) == 1:
                #print("Recognition will start")
                for ind, enc_value in enumerate(data['encoding']):
                        matched=fr.compare_faces(
                             face_encoding, np.array(eval(enc_value))
                        )[0]
                        if matched == True:
                            cv2.putText(
                                img, data['name'] [ind],
                                (50,50), cv2.FONT_HERSHEY_SIMPLEX,1.5,
                                (0,0,255),8
                            )
                            break
        cv2.rectangle(img,
            pt1=(x,y), pt2=(x+w, y+h),
            color=(0,255,0), thickness=10
        )
        cv2.imshow('preview', img)
        key=cv2.waitKey(1)
        if key == ord('q'):
            break
cv2.waitKey(1)
cv2.destroyAllWindows()
vid.release()"""






















# Recognition Step.................
#CORRECT, FINAL CODE.....
"""import cv2
import pandas as pd
import face_recognition as fr

import numpy as np

filename='database.csv'
vid = cv2.VideoCapture(0)
fd=cv2.CascadeClassifier(
            cv2.data.haarcascades+'haarcascade_frontalface_default.xml'
)

try:
    face_db = pd.read_csv(filename, index_col=0, sep='\t')
    data = {
        'name' : face_db['name'].values.tolist(),
        'encoding' : face_db['encoding'].values.tolist(),
    }
except Exception as e:
    print(e)
    data = {'name' : [], 'encoding' : []}

# print(data)             #written roughly (delete later)

while True:
    flag, img=vid.read()
    if flag:
        faces = fd.detectMultiScale(
            cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),
            scaleFactor = 1.1,
            minNeighbors=5,
            minSize = (50,50)
        )

        if len(faces)==1:
            x,y,w,h = faces[0]
            img_face = img[y:y+h, x:x+w, :].copy()
            img_face= cv2.resize(img_face,(400,400),
                                 interpolation=cv2.INTER_CUBIC)
            #cv2.imwrite(f'{name}_{frameCount}.png', img_face)
            face_encoding = fr.face_encodings(img_face)

            if len(face_encoding) == 1:
                #print("Recognition will start")              #not sure
                for ind, enc_value in enumerate(data['encoding']):
                        matched=fr.compare_faces(
                             face_encoding, np.array(eval(enc_value))
                        )[0]
                        if matched == True:
                            cv2.putText(
                                img, data['name'] [ind],
                                (50,50), cv2.FONT_HERSHEY_SIMPLEX,1.5,
                                (0,0,255),8
                            )
                            break
        cv2.rectangle(img,                                        #drawing rectangle on face
            pt1=(x,y), pt2=(x+w, y+h),                            
            color=(0,0,255), thickness=10
        )
        cv2.imshow('preview', img)
        key=cv2.waitKey(1)
        if key == ord('q'):
            break
cv2.waitKey(1)
cv2.destroyAllWindows()
vid.release()"""











#MAKING CHANGES (UPDATINDG) UPPER CODE 
import cv2
import pandas as pd
import face_recognition as fr

import numpy as np

filename='database.csv'
vid = cv2.VideoCapture(0)
fd=cv2.CascadeClassifier(
            cv2.data.haarcascades+'haarcascade_frontalface_default.xml'
)

try:
    face_db = pd.read_csv(filename, index_col=0, sep='\t')
    data = {
        'name' : face_db['name'].values.tolist(),
        'encoding' : face_db['encoding'].values.tolist(),
    }
except Exception as e:
    print(e)
    data = {'name' : [], 'encoding' : []}

# print(data)             #written roughly (delete later)

while True:
    flag, img=vid.read()
    if flag:
        faces = fd.detectMultiScale(
            cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),
            scaleFactor = 1.1,
            minNeighbors=5,
            minSize = (50,50)
        )

        if len(faces)==1:
            x,y,w,h = faces[0]
            img_face = img[y:y+h, x:x+w, :].copy()
            img_face= cv2.resize(img_face,(400,400),
                                 interpolation=cv2.INTER_CUBIC)
            #cv2.imwrite(f'{name}_{frameCount}.png', img_face)
            face_encoding = fr.face_encodings(img_face)

            if len(face_encoding) == 1:
                #print("Recognition will start")              #not sure
                for ind, enc_value in enumerate(data['encoding']):
                        matched=fr.compare_faces(
                             face_encoding, np.array(eval(enc_value))
                        )[0]
                        if matched == True:
                            cv2.putText(
                                img, data['name'] [ind],
                                (50,50), cv2.FONT_HERSHEY_SIMPLEX,1.5,
                                (0,0,255),8
                            )
                            break
        cv2.rectangle(img,                                        #drawing rectangle on face
            pt1=(x,y), pt2=(x+w, y+h),                            
            color=(0,0,255), thickness=10
        )
        cv2.imshow('preview', img)
        key=cv2.waitKey(1)
        if key == ord('q'):
            break
cv2.waitKey(1)
cv2.destroyAllWindows()
vid.release()                   