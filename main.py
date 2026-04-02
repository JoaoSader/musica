import yt_dlp

def download_video(url):
    ydl_opts = {
        # 'ios' ou 'tv' costumam pular o erro de login/bot
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': '%(title)s.%(ext)s',
        
        # FORÇA O DISFARCE (Isso resolve o erro de Sign in)
        'extractor_args': {
            'youtube': {
                'player_client': ['tv'],
            }
        },
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Disfarçando o script como TV e iniciando...")
            ydl.download([url])
            print("\nDownload concluído!")
    except Exception as e:
        print(f"\nErro persistente: {e}")

if __name__ == "__main__":
    video_url = input("URL do YouTube: ")
    download_video(video_url)