from pytube import YouTube

link = input("Link: ")
type_link = input('video / audio: ')
yt = YouTube(link, use_oauth=True, allow_oauth_cache=True)
print("Название:" , yt.title)

# yt.streams.first().download()
# yt.streams.filter(file_extension='mp4').first().download('video')
if type_link == "video":
    print("Начинаю скачивать  видео...")
    yt.streams.filter(res='1080p').first().download('video')
    print('Видео скачалось')
elif type_link == "audio":
    print("Скачиваю аудио")
    yt.streams.filter(only_audio=True).first().download('audio')
    print('Аудио скачалось')





