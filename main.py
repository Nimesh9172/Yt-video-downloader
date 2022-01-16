from pytube import YouTube

url = input("Enter youtube video link: ")

yt = YouTube(url)

print(f"Title of video: {yt.title}")
print(f"Number of views: {yt.views}")
print(f"length of video: {yt.length},seconds")

stream = str(yt.streams.filter(progressive=True))
streamlist = stream.split(", ")
print("All available options for downloads:")
for i in range(0,len(streamlist)):
    sp = streamlist[i].split(" ")
    print(f"{i+1}) {sp[1]} and {sp[-6]}")

tag = int(input("Enter the itag: "))
dow = yt.streams.get_by_itag(tag)
print("Downloading....")
dow.download()
print("Download completed!!")
