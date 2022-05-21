
from moviepy.editor import VideoFileClip, clips_array, vfx, CompositeVideoClip

clip = VideoFileClip("green.mp4")
background = VideoFileClip("out.mp4")
maskedclip = clip.fx(vfx.mask_color, color=[0, 255, 0], thr=100, s=5)

finalcut = CompositeVideoClip([background, maskedclip]).set_duration(background.duration)

finalcut.write_videofile("out_b.mp4")