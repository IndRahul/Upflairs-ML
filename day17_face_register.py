   ## FACE REGISTERING............   CONSIDER BELOW CODE

#CODE WITH SOME ERRORS..
"""import cv2
import pandas as pd
import face_recognition as fr

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

names=data['name']
enc=data['encoding']
frameCount=0
frameLimit=20

name = input('Enter your name:')
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
                enc.append(face_encoding[0].tolist())
                names.append(name)
                frameCount += 1
                print(frameCount)
                cv2.putText(
                            img, str(frameCount),
                            (50,50), cv2.FONT_HERSHEY_SIMPLEX,1.5
                            (0,0,255),8
                        )
                if frameCount == frameLimit:
                    data = {'name':names, 'encoding':enc}
                    pd.DataFrame(data).to_csv('faces_data.tsv', sep='\t'             #why here .tsv is written
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









# FACE REGISTERING 
#CORRECT, FINAL CODE.....
import cv2
import pandas as pd
import face_recognition as fr

filename = 'database.csv'     #changed here  (roughly writing)
vid = cv2.VideoCapture(0)
fd=cv2.CascadeClassifier(
            cv2.data.haarcascades+'haarcascade_frontalface_default.xml'
)
try:
    face_db = pd.read_csv(filename, index_col=0, sep='\t')    #changed here  (roughly writing)
    data = {
        'name' : face_db['name'].values.tolist(),
        'encoding' : face_db['encoding'].values.tolist(),
    }
except Exception as e:
    print(e)
    data = {'name' : [], 'encoding' : []}

names=data['name']
enc=data['encoding']
frameCount=0
frameLimit=20

name = input('Enter your name:')
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
                enc.append(face_encoding[0].tolist())
                names.append(name)
                frameCount += 1
                print(frameCount)
                cv2.putText(
                            img, str(frameCount),
                            (50,50), cv2.FONT_HERSHEY_SIMPLEX,1.5,          
                            (0,0,255),8
                        )
                if frameCount == frameLimit:
                    data = {'name':names, 'encoding':enc}
                    pd.DataFrame(data).to_csv(filename, sep='\t'            
                                              )
                    break
            cv2.rectangle(img,                             #drawing rectangle on face
                pt1=(x,y), pt2=(x+w, y+h),
                color=(255,0,0), thickness=10
            )
    cv2.imshow('preview', img)
    key=cv2.waitKey(1)
    if key == ord('q'):
        break
cv2.waitKey(1)
cv2.destroyAllWindows()
vid.release()