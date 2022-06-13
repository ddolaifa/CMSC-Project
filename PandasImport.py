import matplotlib as plt
import pandas as pd

class PandasImport:
    def __init__(self, dataset):
        self.dataset = pd.read_csv(dataset)
        self.importCountry()
        self.saveCSV()
        self.saveHdf()

    def importCountry(self):
        merged_file = pd.read_excel('./Country-Code.xlsx', 'Sheet1')
        merged_file = pd.merge(self.dataset, merged_file, on='Country Code', how='left')
        merged_file.groupby(['Country', 'Currency']).size().reset_index().drop(0, axis=1)

        self.dataset = merged_file

    def saveCSV(self):
        self.dataset.read_csv('zomato.csv')

    def saveHdf(self):
        self.dataset.to_hdf("zomato.h5")

    def getRating(self):
        rating_data = self.dataset.loc[self.dataset['Country Code'] == 1].groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index()
        rating_data.rename(columns={0: 'Count'}, inplace=True)

        return rating_data

    def getCountry(self, dataset):
        temp = dataset[['Rating text', 'Count']].groupby(['Rating text']).sum()
        temp.drop('Not rated', axis=0, inplace=True)