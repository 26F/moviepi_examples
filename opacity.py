
from moviepy.editor import *

clip = VideoFileClip("b.mp4")
clip2 = VideoFileClip("blackguydancing//1.mp4")
clip2 = clip2.resize(2.96)
clip2 = clip2.set_opacity(0.5)

master = CompositeVideoClip([clip, clip2]).set_duration(clip2.duration)

master.write_videofile("123.mp4")