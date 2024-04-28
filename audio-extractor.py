from moviepy.editor import VideoFileClip
import argparse
import os
# this his a script that will take either a file name or entire directory as an argument
# it will extract that file or files audio and save it as an mp3 file


# function to extract audio from a video file
def extract_audio(video_filepath, audio_filepath, output_dir):
    # Load the video file
    video = VideoFileClip(video_filepath)
    
    # Extract the audio
    audio = video.audio
    
    #get just the audio file name
    audio_filename = audio_filepath.split("/")[-1]
    # Write the audio to a file
    audio.write_audiofile(output_dir + audio_filename)
    
    # Close the audio and video files to release resources
    audio.close()
    video.close()


# set up command line arguments for either a file name or a directory
parser = argparse.ArgumentParser(description='Extract audio from a video file')
parser.add_argument('-f', type=str, help='Path to the video file')
parser.add_argument('-d', type=str, help='Path to the directory containing video files', default="")
parser.add_argument('-o', type=str, help='Path to the output directory', default=os.getcwd())
args = parser.parse_args()

# make sure that output directory has a slash at the end
if not args.o.endswith('/'):
    args.o = args.o + '/'
output_dir = args.o

#extract audio of a single file
if args.f:
    video_path = args.f
    audio_path = video_path.split('.')[0] + '.mp3'
    extract_audio(video_path, audio_path, output_dir)

if args.d != "":
    #extract audio of all files in a directory
    video_dir = args.d

    for video_file in os.listdir(video_dir):
        if (video_file.endswith(".mp4") or 
        video_file.endswith(".avi") or
        video_file.endswith(".mov") or
        video_file.endswith(".mkv") or
        video_file.endswith(".webm")
        ):
            video_path = os.path.join(video_dir, video_file)
            audio_path = os.path.join(video_dir, video_file.split('.')[0] + '.mp3')
            extract_audio(video_path, audio_path, output_dir)

    
