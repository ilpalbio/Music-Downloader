# PROGETTO MUSIC_DOWNLOADER
# Lo scopo di questo progetto è quello di creare un applicativo che una volta avviato sarà in grado di ascoltare un determinato audio
# Capire di che canzone si tratta
# Estrarre il link della canzone 
# Scaricare la canzone 
# 
# LIBRERIE NECESSARIE PER IL PROGETTO
# Python3: interprete per il codice
# Sounddevice: serve per registrare la canzone
# Se su ubuntu non installa pyaudio con 'pip install pyaudio' eseguire prima 'sudo apt-get install portaudio19-dev python-pyaudio'
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

# file delle impostazioni
import settings

# altri file
from logic.youtube_url_extractor import UrlExtractor
from logic.shazam import MusicShazam
from logic.downloader import MusicDownloader
from logic.recorder import MusicRecorder

# parte della registrazione della canzone
recorder = MusicRecorder(file_name = settings.NAME_REC_FILE)

# inizione della registrazione
print('Inizio della registrazione...')
recorder.start_record()

print('Fine della registrazione')
recorder.stop_record
recorder.close()

print()

# parte di shazam
print('Avvio di Shazam...')
shazam = MusicShazam(nfile = settings.NAME_REC_FILE)

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
music_downloader = MusicDownloader(file_path = settings.MUSIC_PATH)

print('Inizio del download del link ', music_link, '...')
music_downloader.download_music(music_link)