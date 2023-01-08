import cv2

video = cv2.VideoCapture('path/to/video.mp4')
focus_measure = cv2.Laplacian(gray, cv2.CV_64F).var()
best_focus_measure = 0
best_frame = None

while True:
  _, frame = video.read()
  if frame is None:
    break
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  focus_measure = cv2.Laplacian(gray, cv2.CV_64F).var()
  if focus_measure > best_focus_measure:
    best_focus_measure = focus_measure
    best_frame = frame

video.release()

cv2.imwrite('best_focused_frame.jpg', best_frame)