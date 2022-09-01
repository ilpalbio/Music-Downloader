# FILE PER IL REGISTRATORE DELLA MUSICA
# classe per il music_recorder
# deve salvare su file quello che il telefono risce a sentire e salvarlo su un file

# guardare 
# https://gist.github.com/kepler62f/9d5836a1eff8b372ddf6de43b5b74d95

# librerie
import pyaudio
import wave
import time

class MusicRecorder:
    def __init__(self, file_name): # costruttore
        # creazione di una istanza di PyAudio
        self.audo_instance = pyaudio.PyAudio()

        # impostazioni della registrazione
        self.channels = 1 # 1 mono, 2 stereo
        self.rate = 16000 # velocità di campionamento del microfono (hertz)
        self.frames_per_buffer = 1024
        self.stream = None # stream
        self.clip_duration = 15

        self.frames = [] # lista dove sono contenuti i bytes della registrazione

        # impostazione del file wav
        self.file_name = file_name
        self.file_mode = 'wb'

        self.wav_file = self.prepare_wav(self.file_name, self.file_mode) # file dove viene salvata la regstrazione



    def start_record(self): # metodo per iniziare la registrazione della canzone
        # apertura della stream
        self.stream = self.audo_instance.open(
            format = pyaudio.paInt16,
            channels = self.channels,
            rate = self.rate,
            input = True,  # input = True significa che registrerà l'audio in input e non lo riproducerà
            frames_per_buffer = self.frames_per_buffer,
            stream_callback = self.get_callback() # callback
            )

        # inizio della stream
        self.stream.start_stream()

        time.sleep(self.clip_duration)



    def stop_record(self): # metodo per fermare la registrazione
        # stop della stream
        self.stream.stop_stream()


    def close(self):
        # chiusura della stream
        self.stream.close()

        # chiusura di pyaudio
        self.audo_instance.terminate()

        # chiusura del file
        self.wav_file.close()


    def get_callback(self):
        def callback(in_data, frame_count, time_info, status_flag):
            # aggiunta dei dati alla lista 
            data = self.wav_file.writeframes(in_data)

            return (data, pyaudio.paContinue)

        return callback

    def prepare_wav(self, file_name, mode): # metodo per aprire il file dove verrà messa la registrazione
        file = wave.open(self.file_name, self.file_mode) # apertura del file
        file.setnchannels(self.channels)
        file.setsampwidth(self.audo_instance.get_sample_size(pyaudio.paInt16))
        file.setframerate(self.rate)
        return file
