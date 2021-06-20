from pytube import YouTube

try:
    yt = YouTube(url=input("Url: "))
except Exception as e:
    print(f"ERRO! {e}")
else:
    yt.streams.first().download()
    print("PROCESSO FINALIZADO")
