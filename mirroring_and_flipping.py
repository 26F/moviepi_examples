
from moviepy.editor import VideoFileClip, clips_array, vfx, CompositeVideoClip

clip1 = VideoFileClip("blackguydancing//1.mp4")
clip1 = clip1.resize(0.50)
clip2 = clip1.fx(vfx.mirror_x)
clip3 = clip1.fx(vfx.mirror_y)
clip4 = clip1.fx(vfx.mirror_x).fx(vfx.mirror_y)

finalcut = CompositeVideoClip([clip1, clip2.set_position((648 // 2, 0)), 
	                            clip3.set_position((648 // 2, 480 // 2)), 
	                            clip4.set_position((0, 480 // 2))], size=(648, 480))

finalcut.write_videofile("out.mp4")