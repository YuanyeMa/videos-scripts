import ffmpeg
import os

#source_dir = r'F:\\素材\\已分类\\'
#output_dir = r"F:\\素材\\concat\\"

source_dir = r"F:\\素材\\concat\\"
output_dir = r"F:\\素材\\concat-week\\"

def merge_videos_with_time(input_dir, output_file, has_watermark=False, watermark_text=None):
    video_files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
    vides_files = sorted(video_files)
    
    streams = []
    for in_filename in vides_files:
        stream_file = os.path.join(input_dir, in_filename)
        print(str(stream_file))
        try:
            ffmpeg.probe(stream_file)
        except Exception as ex:
            print("!!!!!!!!!!!!!!!! probe video failed , skip this video !!!!!!!!!! ")
            continue
        else:
            stream = ffmpeg.input(stream_file)
            streams.append(stream)
            
    out = ffmpeg.concat(*streams)

    
    if has_watermark and watermark_text:
        out = ffmpeg.drawtext(out, text=watermark_text, x='main_w-text_w-100', y='main_h-text_h-50', fontcolor='white@0.5', fontsize=30)
    
    out = ffmpeg.output(out, output_file)
    
    try:
        print("+++++++++++++++++++++++ output for "+str(output_file)+ "+++++++++++++++++++++++++++")
        ffmpeg.run(out)
    except Exception as ex:
        print("----------------------- output for " + str(output_file) + " failed!!!")
        if os.path.exists(output_file):
            os.remove(output_file)
    print("+++++++++++++++++++++++ output for "+str(output_file) + " concat finished")