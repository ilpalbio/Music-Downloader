# librerie
import youtube_dl

class MusicDownloader:
    # costruttore
    def __init__(self):
        self.youtube_options = {
            'format' : 'bestaudio/best', # qualità dell'audio bestaudio è solo per l'audio metre best è anche per il video
            
            'progress_hooks' : [
                self.installation_info
            ],
            
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }],
        }

    # metodo per scaricare la canzone
    def download_music(self, link):
        with youtube_dl.YoutubeDL(self.youtube_options) as youtube:
            youtube.download([link])
            
    # metodo per visualizzare le informazioni del download della canzone
    def installation_info(self, d):
        if d['status'] =='finished':
            print('Download completato con successo')