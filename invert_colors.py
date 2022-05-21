
from moviepy.editor import *

cut1 = VideoFileClip("blackguydancing//60.mp4")
cut = cut1.fx(vfx.invert_colors)

cut.write_videofile("outb.mp4")