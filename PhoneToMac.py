import time

while "1709" not in open(r"/Users/ivanperanovic/Dropbox/AutoSongPlayer/Song.txt").read():
    time.sleep(1.5)
    print(open("/Users/ivanperanovic/Dropbox/AutoSongPlayer/Song.txt").read())
print("Stopped.")
open(r"/Users/ivanperanovic/Dropbox/AutoSongPlayer/Song.txt", "w").write("")