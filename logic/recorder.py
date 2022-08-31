# FILE PER IL REGISTRATORE DELLA MUSICA
# classe per il music_recorder
# deve salvare su file quello che il telefono risce a sentire e salvarlo su un file

# guardare 


# librerie
import sounddevice
import wave

class MusicRecorder:
    def __init__(self, rec_duration = 10): # costruttore
        # valori per la registrazione
        self.rec_duration = rec_duration # durata della registrazione (secondi)
        self.samplerate = 1600 # velocità di campionamento (hz)
        self.channels = 1 # nuemero di canali da registrare
        self.dtype = 'int16' # tipo di dato utilizzato per la registrazione del suono

        self.rec = [] # array in cui verrà mssa la registrazione

    def start_record(self):
        print('Inizio della registrazione...')
        self.rec = sounddevice.rec(
            frames = int(self.rec_duration * self.samplerate), # frames è la lunghezza totale della traccia audio
            samplerate = self.samplerate,
            channels = self.channels,
            dtype = self.dtype,
            )

        sounddevice.stop()
        print('Fine della registrazione')

        print(self.rec)

    def create_wav(self, filename = 'audio.wav', mode = 'wb'): # metodo per aprire il file dove verrà messa la registrazione
        file = wave.open(filename, mode) # apertura del file
        file.setchannels(self.channels)
        file.setsampwith(self.audo_instance.get_sample_size(pyaudio.paInt16))
        file.setframerate(self.rate)
        return file

rec = MusicRecorder()
rec.start_record()