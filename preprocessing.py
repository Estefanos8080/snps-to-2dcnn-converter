import pandas as pd

class Preprocessing:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    # return the dataframe
    def get_dataframe(self):
        print(self.df)

    # return the number of columns in the dataset
    def count_number_of_features(self):
        print(len(self.df.columns))

    # return the number of rows in the dataset
    def count_number_of_rows(self):
        print(len(self.df.index))

    # count the number of rows with missing values where 0 stands for the missing value
    def count_number_of_missing_values(self):
        missing_values = 0
        for index, row in self.df.iterrows():
            if (row == 0).any():
                missing_values += 1
        print("Number of missing Snp's: ", missing_values)

    def get_strain_name_and_snps(self):
        # Get the strain name from the first element in the first row
        strain_name = self.df.iloc[0, 0]
        print("Strain Name:", strain_name)

        # Get the SNPs associated with the strain in the same column
        snps = self.df[self.df.columns[0]].values
        print("SNPs:")
        print(snps)


# the instance of the Preprocessing class
# path needs to be changed to the location of the dataset of the working machine
prep = Preprocessing('/Users/estefanosk/Desktop/SummerProject/snps-to-2dcnn-converter/Giessen_Dataset/cip_ctx_ctz_gen_multi_data.csv')

# calling the methods
prep.get_dataframe()
prep.count_number_of_features()
prep.count_number_of_rows()
prep.get_strain_name_and_snps()
