import pydub
import os
import pafy
import sys
import shutil
# getting url and user choice
if len(sys.argv) > 1:
  url = str(sys.argv[1])
else:
  url = str(input("URL :"))
print("0 . Video\n1 . Audio\n2.Custom Quality")
choice = int(input(">>"))
_format = "none"
_cformat = "none"
downlods_path = "/sdcard/Download/"

# convering short url
if 'shorts' in url:
    url = url.replace("/shorts/", "/watch?v=")
    url = url.replace("?feature=share","")

yt = pafy.new(url)
dl_file_name = yt.title

# Coverting video(mp4)
if choice == 0:
    vid = yt.streams
    dl_file_name = dl_file_name+".mp4"
    iGot360p = False
    for i in range(len(vid)):
        if "x360" in vid[i].resolution:
            iGot360p = True
            print("* Size : ", end="")
            print(str(round(vid[i].get_filesize()/1024/1024, 2))+" MB")
            vid[i].download()
            print("Downloaded video")
    if not iGot360p:
        print("Warning :cant get 360p")
        print(str(round(vid[0].get_filesize()/1024/1024, 2))+" MB")
        vid[0].download()
        print("Downloaded video")

# Converting to Audio["mp3"]
elif choice == 1:
    aud = yt.audiostreams
    input_file = yt.title
    out = input_file+".mp3"
    dl_file_name = out
    # Searching for m4a
    for i in range(len(aud)):
        if "m4a" in aud[i].extension:
            _format = str(aud[i].extension)
            print("* Size : ", end="")
            print(str(round(aud[i].get_filesize()/1024/1024, 2))+" MB")
            aud[i].download()
            print("m4a DOwnloaded")
    sound = pydub.AudioSegment.from_file(input_file+"."+_format)
    sound.export(out, format="mp3")
    os.remove(input_file+"."+_format)
    print("mp3 Converted")
# Custom resolution
elif choice == 2:
    vid = yt.streams
    dl_file_name = dl_file_name+".mp4"
    print("\nAvailable Formats :")
    for i in range(len(vid)):
        print(str(i)+" . "+vid[i].extension+"__"+vid[i].resolution)
    ch = int(input(">>"))
    print("* Size : ", end="")
    print(str(round(vid[ch].get_filesize()/1024/1024, 2))+" MB")
    vid[ch].download()
    print("Downloaded Video")
else:
    print("Wrong input bruh!")

print("moving the file to Downloads")
#filter the filename cuz cant move the file in termux
downlods_path = downlods_path+(dl_file_name.replace("|", ""))
downlods_path = downlods_path.replace("?", '')
shutil.move(dl_file_name,downlods_path)
print("Moveed !")
