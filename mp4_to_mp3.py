import subprocess
import os
import sys

def convert_video_to_audio_ffmpeg(video_file, output_ext="mp3"):
    filename, ext = os.path.splitext(video_file)
    subprocess.call(["ffmpeg", "-y", "-i", video_file, f"{filename}.{output_ext}"], 
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)

def get_files_from_dir(dir):
	filelist = []
	for filename in os.listdir(dir):
		filelist.append(filename)
	return(filelist)

if __name__ == "__main__":
	filelist = get_files_from_dir(sys.argv[1])
	print(filelist)
	for file in filelist:
		#vf = sys.argv[1]
		convert_video_to_audio_ffmpeg(file)