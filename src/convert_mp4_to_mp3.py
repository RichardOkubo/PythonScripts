from moviepy.editor import VideoFileClip

filename = input()

mp4_file = f"{filename}.mp4"
mp3_file = f"{filename}.mp3"

videoclip = VideoFileClip(mp4_file)
audioclip = videoclip.audio
audioclip.write_audiofile(mp3_file)
audioclip.close()
videoclip.close()
