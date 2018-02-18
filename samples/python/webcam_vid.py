import numpy as np
import cv2

cap=cv2.VideoCapture(0);
print("Resolution\n"+str(cap.get(3))+"X"+str(cap.get(4))+"\n")

while(True):
	ret,frame =cap.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	cv2.imshow('frame',gray)

	if cv2.waitKey(1)&0xFF==ord('q'):
		break
cap.release()
cv2.destroyAllWindows()