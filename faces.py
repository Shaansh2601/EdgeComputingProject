import numpy as np
import cv2
import pickle
from update_db import detection


def start():
    count=0
    herbal_cream_cascade = cv2.CascadeClassifier('cascades/data/cascade_cream.xml')
    joy_cream_cascade = cv2.CascadeClassifier('cascades/data/joy_cream_cascade.xml')
    colgate_cascade = cv2.CascadeClassifier('cascades/data/cascade_colgate1.xml')
    colgate_cascade_100gm = cv2.CascadeClassifier('cascades/data/cascade_colgate_100gm.xml')

    recognizer_herbal = cv2.face.LBPHFaceRecognizer_create()
    recognizer_herbal.read("./recognizers/face-trainner_herbal.yml")

    recognizer_joy = cv2.face.LBPHFaceRecognizer_create()
    recognizer_joy.read("./recognizers/face-trainner_joy.yml")

    recognizer_colgate = cv2.face.LBPHFaceRecognizer_create()
    recognizer_colgate.read("./recognizers/face-trainner_colgate.yml")

    recognizer_colgate_100gm = cv2.face.LBPHFaceRecognizer_create()
    recognizer_colgate_100gm.read("./recognizers/face-trainner_colgate_100gm.yml")

    labels = {"product_name": 1}
    with open("pickles/face-labels.pickle", 'rb') as f:
        og_labels = pickle.load(f)
        labels = {v: k for k, v in og_labels.items()}

    cap = cv2.VideoCapture(0)

    while (True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        herbal = herbal_cream_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        joy_cream = joy_cream_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        colgate = colgate_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        colgate_100gm = colgate_cascade_100gm.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        for (x, y, w, h) in herbal:
            # print(x,y,w,h)
            roi_gray = gray[y:y + h, x:x + w]  # (ycord_start, ycord_end)
            roi_color = frame[y:y + h, x:x + w]

            # recognize? deep learned model predict keras tensorflow pytorch scikit learn
            id_, conf = recognizer_herbal.predict(roi_gray)
            if conf >= 4 and conf <= 85:
                # print(5: #id_)
                # print(labels[id_])
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                color = (255, 255, 255)
                stroke = 2
                if name != "":
                    count += 1
                    detection(name, count)
                cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)

            img_item = "7.png"
            cv2.imwrite(img_item, roi_color)

            color = (255, 0, 0)  # BGR 0-255
            stroke = 2
            font = cv2.FONT_HERSHEY_SIMPLEX
            end_cord_x = x + w
            end_cord_y = y + h

            cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
        # subitems = smile_cascade.detectMultiScale(roi_gray)
        # for (ex,ey,ew,eh) in subitems:
        #	cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        # Display the resulting frame

        for (x, y, w, h) in joy_cream:
            # print(x,y,w,h)
            roi_gray = gray[y:y + h, x:x + w]  # (ycord_start, ycord_end)
            roi_color = frame[y:y + h, x:x + w]

            # recognize? deep learned model predict keras tensorflow pytorch scikit learn
            id_, conf = recognizer_joy.predict(roi_gray)
            if conf >= 4 and conf <= 85:
                # print(5: #id_)
                # print(labels[id_])
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                color = (255, 255, 255)
                stroke = 2
                if name != "":
                    count += 1
                    detection(name, count)
                cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)

            img_item = "7.png"
            cv2.imwrite(img_item, roi_color)

            color = (255, 0, 0)  # BGR 0-255
            stroke = 2
            font = cv2.FONT_HERSHEY_SIMPLEX
            end_cord_x = x + w
            end_cord_y = y + h

            cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
        # subitems = smile_cascade.detectMultiScale(roi_gray)
        # for (ex,ey,ew,eh) in subitems:
        #   cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        # Display the resulting frame

        for (x, y, w, h) in colgate:
            # print(x,y,w,h)
            roi_gray = gray[y:y + h, x:x + w]  # (ycord_start, ycord_end)
            roi_color = frame[y:y + h, x:x + w]

            # recognize? deep learned model predict keras tensorflow pytorch scikit learn
            id_, conf = recognizer_colgate.predict(roi_gray)
            if conf >= 4 and conf <= 85:
                # print(5: #id_)
                # print(labels[id_])
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                color = (255, 255, 255)
                stroke = 2
                if name != "":
                    count += 1
                    detection(name, count)
                cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)

            img_item = "7.png"
            cv2.imwrite(img_item, roi_color)

            color = (255, 0, 0)  # BGR 0-255
            stroke = 2
            font = cv2.FONT_HERSHEY_SIMPLEX
            end_cord_x = x + w
            end_cord_y = y + h

            cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
        # subitems = smile_cascade.detectMultiScale(roi_gray)
        # for (ex,ey,ew,eh) in subitems:
        #   cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        # Display the resulting frame

        for (x, y, w, h) in colgate_100gm:
            # print(x,y,w,h)
            roi_gray = gray[y:y + h, x:x + w]  # (ycord_start, ycord_end)
            roi_color = frame[y:y + h, x:x + w]

            # recognize? deep learned model predict keras tensorflow pytorch scikit learn
            id_, conf = recognizer_colgate_100gm.predict(roi_gray)
            if conf >= 4 and conf <= 85:
                # print(5: #id_)
                # print(labels[id_])
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                color = (255, 255, 255)
                stroke = 2
                if name != "":
                    count += 1
                    detection(name, count)
                cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)

            img_item = "7.png"
            cv2.imwrite(img_item, roi_color)

            color = (255, 0, 0)  # BGR 0-255
            stroke = 2
            font = cv2.FONT_HERSHEY_SIMPLEX
            end_cord_x = x + w
            end_cord_y = y + h

            cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
        # subitems = smile_cascade.detectMultiScale(roi_gray)
        # for (ex,ey,ew,eh) in subitems:
        #   cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        # Display the resulting frame

        cv2.imshow('frame', frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
