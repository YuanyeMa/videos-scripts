import ffmpeg
import os

in_filename = r"F:\\素材\\concat\\2023-06-05-output.mp4"
out_filename = r"F:\\素材\\concat\\2023-06-05-output-drawtext.mp4"

def main():
    stream = ffmpeg.input(in_filename)
    stream = ffmpeg.drawtext(stream, text="2023-06-05", x=0, y=0, escape_text=True, box=1, boxcolor=0x000000, fontcolor=0xE0FFFF, alpha=0.5)
    
    out = ffmpeg.output(stream, out_filename)
    ffmpeg.run(out)
    

main()