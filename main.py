from pytube import YouTube

def Download(Link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Ocorreu um erro ao realizar o download")
    print("Download completo")

link = input("Insira o link:")
Download(link)