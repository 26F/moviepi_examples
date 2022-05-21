
from moviepy.editor import VideoFileClip, concatenate_videoclips

clip1 = VideoFileClip("blackguydancing//1.mp4")
clip2 = VideoFileClip("blackguydancing//2.mp4")
clip3 = VideoFileClip("blackguydancing//3.mp4")
clip4 = VideoFileClip("blackguydancing//4.mp4")

finalcut = concatenate_videoclips([clip1, clip2, clip3, clip4])
finalcut.write_videofile("out.mp4")