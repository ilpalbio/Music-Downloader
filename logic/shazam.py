# FILE IN CUI VERRA' RICONOSCIUTA LA CANZONE REGISTRATA

# librerie
import shazamio
import asyncio

class MusicShazam:
    # costruttore
    def __init__(self, nfile = 'music.wav'):
        self.__nfile = nfile
        self.music_title = None
        self.music_artist = None
        
        self.__start_loop()

    # metodo per riconoscere la canzone dalla traccia
    async def __recognize_song(self):
        shazam = shazamio.Shazam()
        
        music = await shazam.recognize_song(self.__nfile)
        
        return music

    # metodo per estrarre tutte le info utili dalla traccia riconosciuta
    def __music_info(self, music):
        info_song = shazamio.Serialize.track(data = music['track'])
        
        # aggiunta delle info agli attributi della classe
        self.music_title = info_song.title 
        self.music_artist = info_song.subtitle
    
    # metodo per creare un nuovo loop con async e chiamare il metodo recognize_song
    def __start_loop(self):
        async_loop = asyncio.get_event_loop() # loop di asyncio
        music = async_loop.run_until_complete(self.__recognize_song())
        
        # chiamata del prossimo metodo
        self.__music_info(music)


