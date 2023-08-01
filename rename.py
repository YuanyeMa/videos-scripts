
import sys
import ffmpeg
import os
import shutil
from datetime import datetime, timedelta

def rename_video(raw_files_dir, renamed_files_dir): #, faile_files_dir):
    format = "%Y-%m-%dT%H:%M:%S.000000Z"
    failed_file_list = []
    for filename in os.listdir(raw_files_dir):
        ori_name = os.path.join(raw_files_dir, filename)
        
        try:
            probe = ffmpeg.probe(ori_name)
            creation_time = probe['format']['tags']['creation_time']
        except Exception as ex:
            print("Deal " + ori_name + " failed! : " + str(ex))
            failed_file_list.append(ori_name)
            #shutil.move()
            continue
        
        date = datetime.strptime(creation_time, format)
        weeks_dir = os.path.join(renamed_files_dir, "weeks-"+str(date.strftime("%W")))
        if not os.path.exists(weeks_dir):
            try:
                os.makedirs(weeks_dir)
            except Exception as ex:
                print("Failed mkdir  " + weeks_dir + " ! : " + str(ex))
        
        bj_time = date + timedelta(hours=8)
    
        dir_name = bj_time.strftime("%Y-%m-%d")
        file_name = bj_time.strftime("%H-%M-%S")
        
        dir = os.path.join(weeks_dir, dir_name)
        if not os.path.exists(dir):
            os.makedirs(dir)
        
        target_name = os.path.join(dir, file_name+".mp4")
        shutil.move(ori_name, target_name)
        print("move " + ori_name+" to " + target_name) 
    
    print("----------------------------------------------")
    print("parse failed files : ")
    for file_name in failed_file_list:
        print(file_name)
    print("----------------------------------------------")
    
def main():
    rename_video(sys.argv[1], sys.argv[2])
    
main()