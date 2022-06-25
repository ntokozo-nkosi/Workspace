from pytube import YouTube

def get_url():
    """
        Get the link and verify steam
    """

    link = input("Enter Url: ")
    yt = YouTube(link)

    set_stream()

    print(f"{title} \n", stream)
    confirm = input(f"Would you like to continue with download? (y or n)")

    if confirm == "y":
        download(stream, title)
    else:
        return 0



def set_stream():
    stream_options = yt.streams.filter(progressive=True)
    title = yt.title

    stream = pick_stream(stream_options)

    while stream == None:
        stream = pick_stream(stream_options)

    return stream

def pick_stream(streams):
    print(streams)
    option = input("Which Stream would you like to download")

    stream = yt.streams.get_by_itag(option)


def download(stream, title):
    print(f"Downloading...{title}")
    stream.download("/home/darthvader/Videos")
    print("Download completed!!")


get_url()
