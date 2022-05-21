
from moviepy.editor import VideoFileClip, concatenate_videoclips

vid = VideoFileClip("7.mp4")

text = TextClip("Black Guy Dancing", fontsize=18, color="pink")
text = text.set_pos('center').set_duration(0.5)
video = CompositeVideoClip([vid, text])

video.write_videofile("bgd.mp4")