#!/bin/python3
import ffmpeg

input_video =  r"/mnt/e/test/days/2023-06-05.mp4"
output_video = r"/mnt/e/test/2023-06-05.mp4-output.mp4"


def main():
    try:
        ffmpeg.probe(input_video)
    except Exception as e:
        print("probe field")
    else:
        stream = ffmpeg.input(input_video)
        stream = ffmpeg.drawtext(stream, text="2023-06-05", x='main_w-text_w-100', y='main_h-text_h-50', fontcolor='white@0.5', fontsize=30)
        out = ffmpeg.output(stream, output_video)

        try:
            ffmpeg.run(out)
        except Exception as e:
            print("drawtext filed : " + str(e))

main()
