from yt_dlp import YoutubeDL

# Configurações do yt-dlp
ydl_opts = {
    # Extrai os cookies do seu navegador padrão. 
    # Substitua 'chrome' por 'edge', 'firefox', 'brave', 'opera', etc., dependendo do que você usa.
    'cookiesfrombrowser': ('chrome',), 
}

# O URL que você quer baixar
url = 'https://youtu.be/1_9BPqfXHlo?si=vm0hjhYxVHo9qM-Z'

# Executando o download com as opções
with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])