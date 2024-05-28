import json
import os
from torch.utils.data import Dataset
import csv
import pandas as pd

class DiabetesDataset(Dataset):
    def __init__(self):
        file_path = './data/diabetes.csv'
        self.data = pd.read_csv(file_path, header=None, delimiter=',')
        self.validation_data = self.data['validation']
        
        self.data = [{"sent": ins['sentence'].strip(), "label": ins['label']} for ins in self.validation_data]
     
        print( "the number of data", len(self.data))
        #print(self.data[0])
        # from IPython import embed; embed()

    def __getitem__(self, item):
        return self.data[item]

    def __len__(self):
        return len(self.data)
    
