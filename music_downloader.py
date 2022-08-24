# PROGETTO MUSIC_DOWNLOADER
# Lo scopo di questo progetto è quello di creare un applicativo che una volta avviato sarà in grado di ascoltare un determinato audio
# Capire di che canzone si tratta
# Estrarre il link della canzone 
# Scaricare la canzone 
# 
# LIBRERIE NECESSARIE PER IL PROGETTO
# Python3: interprete per il codice
# PyAudio: serve per registrare la canzone
# Youtube-dl: serve per scaricare la canzone da youtube 
# Scazamio: serve per capire di che canzone si tratta quella registrata
# Requests: serve per accedere alla pagina di youtube per estrarre il link della canzone
# Re: serve a riconoscere i link nell'html della pagina youtube
# Asyncio: serve per lavorare con shazamio utilizzando delle funzioni asincrone
# Os: serve a interagire con il sistema operativo

# il codice principale sarà in questo file

# documentazione
# youtube-dl: https://github.com/ytdl-org/youtube-dl/blob/master/README.md#embedding-youtube-dl
# shazamio: https://pypi.org/project/shazamio/

# link per installare anaconda
# https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh


# file delle impostazioni
import settings

# altri file
from logic.youtube_url_extractor import UrlExtractor
from logic.shazam import MusicShazam
from logic.downloader import MusicDownloader

# parte di shazam
print('Avvio di Shazam...')
shazam = MusicShazam()

print('Riconoscimento della traccia audio completato')
music_title = shazam.music_title
music_artist = shazam.music_artist

print('Informazioni sulla traccia')
print('-' * 30)
print('Titolo: ', music_title)
print('Artista: ', music_artist)
print('-' * 30)

print()

# parte dell'estrattore di link
print('Estrazione del link migliore da youtube...')
url_extractor = UrlExtractor(song_title = music_title + ' ' + music_artist)
music_link = url_extractor.best_link

print('Miglior link trovato')
print('-' * 30 ,'\nLink: ', music_link)
print('-' * 30)

print()


# parte del downloader 
music_downloader = MusicDownloader()

print('Inizio del download del link ', music_link, '...')
music_downloader.download_music(music_link)