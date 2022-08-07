# FILE DOVE VERRA' TROVATA LA CANZONE REGISTRATA
# links della documentazione dei moduli
# requests: https://requests.readthedocs.io/en/latest/

# librerie
import requests
import re

# classe 
class UrlExtractor:
    
    # costruttore
    def __init__(self, song_title = 'starboy kyro remix'):
        self.song_title = song_title
        self.url = 'https://www.youtube.com/results?search_query=' + self.song_title.replace(' ', '+')
        self.pattern = '/watch\?v=\w{11}'
        self.best_link = None
        
        # appena viene istanziata la classe fa partire subito il metodo start_request
        self.start_request()
    
    # metodo per inviare la request a youtube
    def start_request(self):
        req = requests.get(url = self.url)
        
        self.parse_page(req)


    # metodo per estrarre le informazioni utili dalla pagina i youtube
    def parse_page(self, req):
        # tutta la pagina youtube
        page_body = req.text
        
        # ricerca di tutti i link delle canzoni della pagina
        video_links = re.findall(self.pattern, page_body)
        
        # controllo se ci sono link estratti
        if len(video_links) != 0: 
            print('Estrazione links completata con successo')
            self.filter_links(video_links)
            
        else:
            print('Ops... Non ci sono risultati')      
    
    # metodo per filtrare tutti gli url estratti
    def filter_links(self, links):
        # filtraggio di tutti i risultati
        # il miglior link è sempre il primo perchè youtube mostra la canzone originale come primo risultato
        self.best_link = 'https://www.youtube.com' + links[0]
    
recogniser = UrlExtractor()
print('Miglior link estratto',recogniser.best_link)