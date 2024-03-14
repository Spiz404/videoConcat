import os
import moviepy

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
            description="video concatenation tool, concatentate every mp4 file in a folder")

    parser.add_argument("-p", "--path", help="videos folder path")
    parser.add_argument("-o", "--output", help="concatenation output")

    args = parser.parse_args()
    path = args.path
    output = args.output
    for filepath in os.listdir(path):
        print(filepath)

