# FILE PER IL REGISTRATORE DELLA MUSICA
# classe per il music_recorder
# deve salvare su file quello che il telefono risce a sentire e salvarlo su un file

# guardare 
# https://gist.github.com/kepler62f/9d5836a1eff8b372ddf6de43b5b74d95

# librerie
import pyaudio
import wave

class MusicRecorder():
    def __init__(self): # costruttore
        # creazione di una istanza di PyAudio
        self.audo_instance = pyaudio.PyAudio()

        # impostazioni della registrazione
        self.channels = 1 # 1 mono, 2 stereo
        self.rate = 16000 # velocità di campionamento del microfono (hertz)
        self.frames_per_buffer = 1024
        self.clip_duration = 4 # durata di ogni clip (secondi)
        self.overlap = 0 # tempo di sovrapposizionamento delle clip (secondi)
        self.stream = None # stream
        self.frames = [] # lista in cui verrà immagazzinato il codice binario di input del microfono

    def start_record(self): # metodo per iniziare la registrazione della canzone
        # fps
        fps = int(self.rate / self.frames_per_buffer * self.clip_duration)
        # apertura della stream
        self.stream = self.audo_instance.open(
            format = pyaudio.paInt16,
            channels = self.channels,
            rate = self.rate,
            input = True,  # input = True significa che registrerà l'audio in input e non lo riproducerà
            frames_per_buffer = self.frames_per_buffer,
            stream_callback = self.store_record # callback
            )

        # inizio della stream
        self.stream.start_stream()
        print("Inizio della registrazione ...")

        # inizio della registrazione
        try:
            while True:

                print('Sto ascoltando...')
                # aggiunta dei dati al wav file
                if len(self.frames) > fps:
                    clip = []
                    for i in range(0, fps):
                        clip.append(self.frames[i])

                file = self.create_wav() # creazione del file
                file.writeframes(b''.join(clip)) # scrittura dei dati nel file ( i dati sono bytes)
                file.close() # chiusura del file

                self.frames = self.frames[(self.clip_duration - self.overlap - 1):]

        except KeyboardInterrupt:
            print("Fine registrazione")
            self.stop_record



    def stop_record(self): # metodo per fermare la registrazione
        # stop della stream
        self.stream.stop_stream()

        # chiusura della stream
        self.stream.close()

        # chiusura di pyaudio
        self.audo_instance.close()

    def store_record(self, in_data, frame_count, time_info, status_flag):
        # aggiunta dei dati alla lista 
        data = self.frames.append(in_data)

        return (data, pyaudio.paContinue)

    def create_wav(self, filename = 'audio.wav', mode = 'wb'): # metodo per aprire il file dove verrà messa la registrazione
        file = wave.open(filename, mode) # apertura del file
        file.setchannels(self.channels)
        file.setsampwith(self.audo_instance.get_sample_size(pyaudio.paInt16))
        file.setframerate(self.rate)
        return file
