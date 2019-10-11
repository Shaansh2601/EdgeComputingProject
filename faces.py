import numpy as np
import cv2
import pickle
from update_db import detection


def start():
	count=0
	herbal_cascade = cv2.CascadeClassifier('cascades/data/cascade_cream.xml')
	joy_cascade = cv2.CascadeClassifier('cascades/data/joy_cream_cascade.xml')
	colgate_100gm_cascade = cv2.CascadeClassifier('cascades/data/cascade_colgate_100gm.xml')
	colgate_50gm_cascade = cv2.CascadeClassifier('cascades/data/cascade_colgate_50gm.xml')


	recognizer = cv2.face.LBPHFaceRecognizer_create()
	recognizer.read("./recognizers/face-trainner.yml")

	labels = {"person_name": 1}
	with open("pickles/face-labels.pickle", 'rb') as f:
		og_labels = pickle.load(f)
		labels = {v: k for k, v in og_labels.items()}

	cap = cv2.VideoCapture(0)

	while (True):
		# Capture frame-by-frame
		ret, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		herbal_cream = herbal_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
		joy_cream = joy_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
		colgate_100gm = colgate_100gm_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
		colgate_50gm = colgate_50gm_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

		for (x, y, w, h) in herbal_cream:
			# print(x,y,w,h)
			roi_gray = gray[y:y + h, x:x + w]  # (ycord_start, ycord_end)
			roi_color = frame[y:y + h, x:x + w]

			# recognize? deep learned model predict keras tensorflow pytorch scikit learn
			id_, conf = recognizer.predict(roi_gray)
			if conf >= 4 and conf <= 85:
				# print(5: #id_)
				# print(labels[id_])
				font = cv2.FONT_HERSHEY_SIMPLEX
				name = labels[id_]
				color = (255, 255, 255)
				stroke = 2
				if name!="":
					count+=1
					detection(name,count)
					print(name)
				cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)

			img_item = "7.png"
			cv2.imwrite(img_item, roi_color)

			color = (255, 0, 0)  # BGR 0-255
			stroke = 2
			end_cord_x = x + w
			end_cord_y = y + h
			cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

		for (x, y, w, h) in joy_cream:
			# print(x,y,w,h)
			roi_gray = gray[y:y + h, x:x + w]  # (ycord_start, ycord_end)
			roi_color = frame[y:y + h, x:x + w]

			# recognize? deep learned model predict keras tensorflow pytorch scikit learn
			id_, conf = recognizer.predict(roi_gray)
			if conf >= 4 and conf <= 85:
				# print(5: #id_)
				# print(labels[id_])
				font = cv2.FONT_HERSHEY_SIMPLEX
				name = labels[id_]
				color = (255, 255, 255)
				stroke = 2
				if name!="":
					count+=1
					detection(name,count)
					print(name)
				cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)

			img_item = "7.png"
			cv2.imwrite(img_item, roi_color)

			color = (255, 0, 0)  # BGR 0-255
			stroke = 2
			end_cord_x = x + w
			end_cord_y = y + h
			cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

		for (x, y, w, h) in colgate_100gm:
			# print(x,y,w,h)
			roi_gray = gray[y:y + h, x:x + w]  # (ycord_start, ycord_end)
			roi_color = frame[y:y + h, x:x + w]

			# recognize? deep learned model predict keras tensorflow pytorch scikit learn
			id_, conf = recognizer.predict(roi_gray)
			if conf >= 4 and conf <= 85:
				# print(5: #id_)
				# print(labels[id_])
				font = cv2.FONT_HERSHEY_SIMPLEX
				name = labels[id_]
				color = (255, 255, 255)
				stroke = 2
				if name!="":
					count+=1
					detection(name,count)
				cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)

			img_item = "7.png"
			cv2.imwrite(img_item, roi_color)

			color = (255, 0, 0)  # BGR 0-255
			stroke = 2
			end_cord_x = x + w
			end_cord_y = y + h
			cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
		for (x, y, w, h) in colgate_50gm:
			# print(x,y,w,h)
			roi_gray = gray[y:y + h, x:x + w]  # (ycord_start, ycord_end)
			roi_color = frame[y:y + h, x:x + w]

			# recognize? deep learned model predict keras tensorflow pytorch scikit learn
			id_, conf = recognizer.predict(roi_gray)
			if conf >= 4 and conf <= 85:
				# print(5: #id_)
				# print(labels[id_])
				font = cv2.FONT_HERSHEY_SIMPLEX
				name = labels[id_]
				color = (255, 255, 255)
				stroke = 2
				if name!="":
					count+=1
					detection(name,count)
				cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)

			img_item = "7.png"
			cv2.imwrite(img_item, roi_color)

			color = (255, 0, 0)  # BGR 0-255
			stroke = 2
			end_cord_x = x + w
			end_cord_y = y + h
			cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)


		# subitems = smile_cascade.detectMultiScale(roi_gray)
		# for (ex,ey,ew,eh) in subitems:
		#	cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
		# Display the resulting frame
		cv2.imshow('frame', frame)
		if cv2.waitKey(20) & 0xFF == ord('q'):
			break

	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()
