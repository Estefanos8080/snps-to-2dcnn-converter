import pandas as pd

class Preprocessing:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    # return the number of columns in the dataset
    def count_number_of_features(self):
        print(len(self.df.columns))

    # return the number of rows in the dataset
    def count_number_of_rows(self):
        print(len(self.df.index))

# the instance of the Preprocessing class
# path needs to change to the location of the dataset of the working machine
prep = Preprocessing('/Users/estefanosk/Desktop/SummerProject/Giessen_Dataset/cip_ctx_ctz_gen_multi_data.csv')

# Call the class methods using the instance
prep.count_number_of_rows()
prep.count_number_of_features()
