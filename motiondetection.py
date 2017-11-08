import numpy as np
import cv2
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
g_old = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #initial video frame to compare to the next
h,w = g_old.shape 
g_old = cv2.resize(g_old,(w/10,h/10), interpolation = cv2.INTER_AREA) #sizing it down to decrease compute power needed
while(True):
	ret, frame = cap.read()
	g_new = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	imgt2 = cv2.resize(g_new,(w/10,h/10), interpolation = cv2.INTER_AREA)
	img_diff = cv2.absdiff(imgt2,g_old)
	cv2.imshow('Result',img_diff)
	if cv2.countNonZero(img_diff) > 1950: #this difference is the optimal I found during testing
		print "I saw you move."
	g_old=imgt2
cap.release()
cv2.destroyAllWindows()
