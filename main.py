import os
import rename
import concat_video
import argparse

# raw_files_dir = r"/mnt/e/test/resource/"
# renamed_files_dir = r"/mnt/e/test/renamed/"
# days_dir = r"/mnt/e/test/days/"
# weeks_dir = r"/mnt/e/test/weeks/"


def main():
    args = parse_args()
    
    # 1. renaming
    if not os.path.exists(args.renamed_files_dir):
        os.makedirs(args.renamed_files_dir)
        
    rename.rename_video(args.raw_files_dir, args.renamed_files_dir)
    
    if(args.rename-only):
        return
    
    # 2. first concat 
    if not os.path.exists(args.days_dir):
        os.makedirs(args.days_dir)
    
    for week_dir in os.listdir(args.renamed_files_dir):
        week_dir_path = os.path.join(args.renamed_files_dir, week_dir)
        if os.path.isdir(week_dir_path):
            for day_dir in os.listdir(week_dir_path):
                day_dir_path = os.path.join(week_dir_path,day_dir)
                
                output_file = os.path.join(args.days_dir, str(day_dir)+".mp4") 
                text = str(day_dir)
                concat_video.merge_videos_with_time(day_dir_path, output_file, True, text)
                
    # 3. second concat
    if not os.path.exists(args.weeks_dir):
        os.makedirs(args.weeks_dir)
    
    concat_video.merge_videos_with_time(args.days_dir, os.path.join(args.weeks_dir, "output.mp4"))

def parse_args():
    parser = argparse.ArgumentParser(description="Script for process videos.")
    parser.add_argument('--rename-only', '-ro', type=bool, default=False)
    parser.add_argument("--raw_dir", '-i', type=str, dest=raw_files_dir, required=True)
    parser.add_argument("--renamed_dir", '-o', type=str, dest=renamed_files_dir, required=True)
    parser.add_argument("--days_out_dir", '-do', type=str, dest=days_dir)
    parser.add_argument("--weeks_out_dir", '-wo', type=str, dest=weeks_dir)
    args  = parser.parse_args()
    return args

main()