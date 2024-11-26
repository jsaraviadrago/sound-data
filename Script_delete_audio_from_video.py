from moviepy.editor import VideoFileClip

videoclip = VideoFileClip("https://raw.githubusercontent.com/jsaraviadrago/sound-data/blob/main/chess_rust.mkv") # video example
new_clip = videoclip.without_audio() # strip audio

# Put any folder you want
new_clip.write_videfile("/home/juan-carlos/Vídeos/final_chess_clip.mp4")



