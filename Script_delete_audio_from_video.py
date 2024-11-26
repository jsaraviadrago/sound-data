from moviepy.editor import VideoFileClip

videoclip = VideoFileClip("/home/juan-carlos/Vídeos/chess_rust.mkv") # video example
new_clip = videoclip.without_audio() # strip audio

# Put any folder you want
new_clip.write_videofile("/home/juan-carlos/Vídeos/final_chess_clip.mp4")



