from pytube import YouTube

def download(stream, title):
    print(f"Downloading...{title}")
    stream.download("/home/darthvader/Videos")
    print("Download completed!!")

# streams = yt.streams.filter(progressive=True)

def get_url():
    """
        Get the link and verify steam
    """

    link = input("Enter Url: ")
    yt = YouTube(link)

    title = yt.title
    stream = yt.streams.get_by_resolution("720p")

    if stream == None:
        stream = yt.streams.get_by_resolution("480p")

    print(f"{title} \n", stream)
    confirm = input(f"Would you like to continue with download? (y or n)")

    if confirm == "y":
        download(stream, title)
    else:
        return 0


get_url()
