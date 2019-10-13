import cv2
import os
import numpy as np
from PIL import Image
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")

herbal_cascade = cv2.CascadeClassifier('cascades/data/cascade_cream.xml')
joy_cream_cascade = cv2.CascadeClassifier('cascades/data/joy_cream_cascade.xml')
colgate_cascade = cv2.CascadeClassifier('cascades/data/cascade_colgate1.xml')
colgate_100gm_cascade = cv2.CascadeClassifier('cascades/data/cascade_colgate_100gm.xml')


recognizer_herbal = cv2.face.LBPHFaceRecognizer_create()
recognizer_joy = cv2.face.LBPHFaceRecognizer_create()
recognizer_colgate = cv2.face.LBPHFaceRecognizer_create()
recognizer_colgate_100gm = cv2.face.LBPHFaceRecognizer_create()

current_id = 0
label_ids = {}

y_labels_herbal = []
x_train_herbal = []


y_labels_joy = []
x_train_joy = []

y_labels_colgate = []
x_train_colgate = []

y_labels_colgate_100gm = []
x_train_colgate_100gm = []


for root, dirs, files in os.walk(image_dir):
	for file in files:
		if file.endswith("png") or file.endswith("jpg"):
			path = os.path.join(root, file)
			label = os.path.basename(root).replace(" ", "-").lower()
			#print(label, path)
			if not label in label_ids:
				label_ids[label] = current_id
				current_id += 1
			id_ = label_ids[label]
			#y_labels.append(label) # some number
			#x_train.append(path) # verify this image, turn into a NUMPY arrray, GRAY
			pil_image = Image.open(path).convert("L") # grayscale
			size = (550, 550)
			final_image = pil_image.resize(size, Image.ANTIALIAS)
			image_array = np.array(final_image, "uint8")
			#print(image_array)
			herbal = herbal_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)
			joy_cream = joy_cream_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)
			colgate = colgate_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)
			colgate_100gm = colgate_100gm_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)

			for (x,y,w,h) in herbal:
				roi = image_array[y:y+h, x:x+w]
				x_train_herbal.append(roi)
				y_labels_herbal.append(id_)

			for (x,y,w,h) in joy_cream:
				roi = image_array[y:y+h, x:x+w]
				x_train_joy.append(roi)
				y_labels_joy.append(id_)

			for (x,y,w,h) in colgate:
				roi = image_array[y:y+h, x:x+w]
				x_train_colgate.append(roi)
				y_labels_colgate.append(id_)

			for (x,y,w,h) in colgate_100gm:
				roi = image_array[y:y+h, x:x+w]
				x_train_colgate_100gm.append(roi)
				y_labels_colgate_100gm.append(id_)
#print(y_labels)
#print(x_train)

with open("pickles/face-labels.pickle", 'wb') as f:
	pickle.dump(label_ids, f)

recognizer_herbal.train(x_train_herbal, np.array(y_labels_herbal))
recognizer_herbal.save("recognizers/face-trainner_herbal.yml")

recognizer_joy.train(x_train_joy, np.array(y_labels_joy))
recognizer_joy.save("recognizers/face-trainner_joy.yml")

recognizer_colgate.train(x_train_colgate, np.array(y_labels_colgate))
recognizer_colgate.save("recognizers/face-trainner_colgate.yml")


recognizer_colgate_100gm.train(x_train_colgate_100gm, np.array(y_labels_colgate_100gm))
recognizer_colgate_100gm.save("recognizers/face-trainner_colgate_100gm.yml")