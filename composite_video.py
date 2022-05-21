
from moviepy.editor import VideoFileClip, clips_array, vfx, CompositeVideoClip

clip1 = VideoFileClip("blackguydancing//1.mp4")
clip1 = clip1.resize(0.50)

clip2 = VideoFileClip("blackguydancing//2.mp4")
clip2 = clip2.resize(0.50)

clip3 = VideoFileClip("blackguydancing//3.mp4")
clip3 = clip3.resize(0.50)

clip4 = VideoFileClip("blackguydancing//4.mp4")
clip4 = clip4.resize(0.50)

finalcut = CompositeVideoClip([clip1, clip2.set_position((648 // 2, 0)), 
	                            clip3.set_position((648 // 2, 480 // 2)), 
	                            clip4.set_position((0, 480 // 2))], size=(648, 480))

finalcut.write_videofile("out.mp4")