
from moviepy.editor import *

clip = VideoFileClip("green.mp4")
background = VideoFileClip("out.mp4")
string = "smooth soprano jazz is coming to a town near you smooth jazz blah blah blah blah blah"
textclip = TextClip(string, fontsize=60, color="white")
textclip = textclip.set_pos("left")
textclip = vfx.scroll(textclip, h=480, w=1024, x_speed=200, x_start=0)
maskedclip = clip.fx(vfx.mask_color, color=[0, 255, 0], thr=100, s=5)

finalcut = CompositeVideoClip([background, maskedclip, textclip]).set_duration(background.duration)

finalcut.write_videofile("out_b.mp4")