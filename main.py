import yt_dlp

def download_video(url):
    ydl_opts = {
        # 'bestvideo+bestaudio/best' garante a qualidade máxima
        'format': 'bestvideo+bestaudio/best',
        # Define o nome do arquivo final
        'outtmpl': '%(title)s.%(ext)s',
        # Tenta converter para mp4 no final para facilitar a compatibilidade
        'merge_output_format': 'mp4',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Iniciando download da melhor qualidade...")
            ydl.download([url])
            print("\nDownload concluído com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    video_url = input("Cole a URL do YouTube aqui: ")
    download_video(video_url)