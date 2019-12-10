import pytube

def main():
    url = "https://www.youtube.com/watch?v=s6Zf76tN48A"
    yt = pytube.YouTube(url)
    print("Going to downloaf {}".format(url))
    fname = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    print("Downloaded video to {}".format(fname))

if __name__ == '__main__':
    main()
