from pytube import YouTube

def get_url():
    link = input("Enter Url: ")
    return YouTube(link)

def set_stream(yt):
    title = yt.title
    stream_options = yt.streams.filter(progressive=True)

    print("\n", "Available Streams:")
    for stream in stream_options:
        print(stream, "\n")

    stream = pick_stream(yt)

    return stream

def pick_stream(yt):
    option = input("Which stream would you like to download? (Enter integer) --> ")
    return yt.streams.get_by_itag(option)

def confirm_download(str, yt):
    print(f"{yt.title} \n", str)
    confirm = input(f"Would you like to continue with download? (y or n) --> ")

    if confirm == "y":
        return True
    else:
        return False

def download():
    yt = get_url()
    stream = set_stream(yt)

    if confirm_download(stream, yt):
        print(f"Downloading...{yt.title}")
        stream.download("/home/darthvader/Videos")
        print("Download completed!!")
    else:
        download()

download()
