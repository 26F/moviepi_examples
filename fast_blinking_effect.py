
from moviepy.editor import *

cut1 = VideoFileClip("video//79.mp4")
cut2 = VideoFileClip("video//2.mp4")
global tic
tic = 0

def blink(get_frame, t):
	global tic
	if tic % 2 == 0:
		frame = cut2.get_frame(t)
	else:
		frame = get_frame(t)
	tic += 1
	return frame

cut3 = cut1.fl(blink)

cut3.write_videofile("outa.mp4")