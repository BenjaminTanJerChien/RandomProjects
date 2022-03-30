import os

def main():
    i = 0
    path = "C:/Users/jerch/Pictures/Saved Pictures/" #path to the dir(must use frontslash)
    for filename in os.listdir(path):
        my_dest = f"img{str(i)}.jpg" # can change this t be anything based on they type of files or what you what to achive 
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1

if __name__ == "__main__":
    main()


