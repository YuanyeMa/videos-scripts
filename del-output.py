import os

def main():
    for root, dirs, files in os.walk(r"F:\\\素材\\已分类\\"):
        for file in files:
            if (file == r'output.mp4'):
                remove_file = os.path.join(root, file)
                os.remove(remove_file)
                print("remove file : "+str(remove_file))
            
    

main()