import os
from moviepy.editor import concatenate_videoclips, VideoFileClip

if __name__ == "__main__":
    import argparse

    # arg parser
    parser = argparse.ArgumentParser(
            description="video concatenation tool, concatentate every mp4 file in a folder")

    parser.add_argument("-p", "--path", help="videos folder path")
    parser.add_argument("-o", "--output", help="concatenation output")

    args = parser.parse_args()
    path = args.path
    print(path)
    output = args.output
    if path == None:
        print("input path must be not None")
    else:
        if output == None:
            output = path + "output.mp4"

        videos = [VideoFileClip(path + "/"  + video) for video in os.listdir(path) if os.path.splitext(video)[1] == ".mp4"]
        video = concatenate_videoclips(videos, method="compose")
        video.write_videofile(output, threads = 8, fps = 24)
        
        print(videos)
        
