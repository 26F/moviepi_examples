
from moviepy.editor import *

cut1 = VideoFileClip("blackguydancing//1.mp4")
cut2 = VideoFileClip("blackguydancing//10.mp4")

cut2 = cut2.crossfadein(1)

finalcut = CompositeVideoClip([cut1, cut2])

finalcut.write_videofile("cool.mp4")