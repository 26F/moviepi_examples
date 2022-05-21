
from moviepy.editor import VideoFileClip, clips_array, vfx, CompositeVideoClip
from random import randrange

# splice 25 clips into one clip. A square number is used.
# we use the square root of the number as the for y and for x
# and 1/5 as the scale for each video
# 1/5 the width of the video and the height of the video 
# is used as the position math, see below.
# because there are 25 videos we scale the audio down by 1/25

count = 1
clips = []
for y in range(5):
	for x in range(5):
		r = randrange(1, 90)
		clip = VideoFileClip(f"blackguydancing//{r}.mp4")
		clip = clip.resize(1/5)
		clip = clip.set_position((int(x * ((1/5) * 648)), int(y * ((1/5) * 480))))
		clip = clip.volumex(1/25)
		clips.append(clip)
		count += 1

finalcut = CompositeVideoClip(clips, size=(648, 480))

finalcut.write_videofile("out.mp4")