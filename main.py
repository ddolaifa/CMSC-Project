from PandasImport import PandasImport
from Visualization import Visualization
from ProcessData import ProcessData
from TrainData import TrainData


pandas = PandasImport("zomato.csv")
pd.read

pandas.importCountry()

rating_data = pandas.getRating()

visualize = Visualization()

visualize.plotRating(rating_data)

visualize.plotCountry(rating_data)

process_data = ProcessData(pandas.dataset)
processed_data = process_data.processData()

X_train, X_test, y_train, y_test = process_data.splitData()

train_data = TrainData()
train_data.trainData(X_train, X_test, y_train, y_test)