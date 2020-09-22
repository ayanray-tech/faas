import pandas


class Helper():

    def fetch_data(self, url, names):
        
        dataframe = pandas.read_csv(url, names=names)
        array = dataframe.values
        X = array[:, 0:8]
        Y = array[:, 8]

        return X, Y
