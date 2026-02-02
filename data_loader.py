import pandas as pd
import numpy as np
import json
from urllib.parse import urlparse
import re
import warnings
warnings.filterwarnings('ignore')

class DataLoader:
    def __init__(self, train_path, test_path):
        #__init__ fja se poziva automatski prilikom kreiranja objekta
        #train_path:putanja do train.tsv fajla
        #test_path:putanja do test.tsv fajla
        
        self.train_path = train_path
        self.test_path = test_path
        self.train_data = None
        self.test_data = None
        
    def load_data(self):
        #ucitavamo train i test podatke
        try:
            #train podaci
            print("Učitavanje train podataka...")
            self.train_data = pd.read_csv(self.train_path, sep=',')
            print(f"Train podaci učitani: {self.train_data.shape}")
        
            #test podaci
            print("Učitavanje test podataka...")
            self.test_data = pd.read_csv(self.test_path, sep=',')
            print(f"Test podaci učitani: {self.test_data.shape}")
            
            return True
        except Exception as e:
            print(f"Greška pri učitavanju podataka: {e}")
            return False
    
    def get_basic_info(self):
        #vraca osnovne info o podacima
        if self.train_data is None or self.test_data is None:
            print("Prvo učitaj podatke pozivom load_data()")
            return None
        
        info = {
            'train_shape': self.train_data.shape,
            'test_shape': self.test_data.shape,
            'train_columns': list(self.train_data.columns),
            'test_columns': list(self.test_data.columns),
        }
        
        return info
    
    
    
    def get_processed_data(self):
        #vraca obradjene podatke sa svim feature-ima
            #tuple: (train_processed, test_processed)

        if self.train_data is None or self.test_data is None:
            print("Prvo ucitajte podatke pozivom load_data()")
            return None, None
        
        train_processed = self.train_data
        
        test_processed = self.test_data
        
        return train_processed, test_processed



