import matplotlib.pyplot as plt
import seaborn as sns

class Visualization:
    def __init__(self):
        pass

    def plotRating(self, dataset):
        col = ['white', 'red', 'orange', 'yellow', 'green', 'darkgreen']
        sns.set_style('darkgrid')
        sns.barplot(x='Aggregate rating', y='Count', hue='Rating text', data=dataset, palette=col)
        plt.rcParams['figure.figsize'] = (20, 10)

    def plotCountry(self, dataset):
        restaurant_voting = dataset.groupby(['Country']).mean()
        plt.figure(figsize=(8, 5), frameon=True, dpi=100)
        restaurant_voting['Votes'].sort_values().plot(kind='barh', figsize=(10, 6))
