
from moviepy.editor import *

clip = VideoFileClip("b.mp4")

master = clip.fl_time(lambda t: 4 * t)
realm = master.subclip(0, 10)
realm.write_videofile("123.mp4")