import json
import os
from torch.utils.data import Dataset
import csv
import pandas as pd

class BankDataset(Dataset):
    def __init__(self):
        file_path = './Bank_Personal_Loan_Modelling.xlsx'
        self.data = pd.read_excel(file_path)
        self.validation_data = self.data['validation']
        
        self.data = [{"sent": ins['sentence'].strip(), "label": ins['label']} for ins in self.validation_data]
     
        print( "the number of data", len(self.data))
        #print(self.data[0])
        # from IPython import embed; embed()

    def __getitem__(self, item):
        return self.data[item]

    def __len__(self):
        return len(self.data)
    
