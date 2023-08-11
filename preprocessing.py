import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

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

    # EDA: get the coloum of the isolate name and the drug response
    def create_data_frame_by_drug_name(self):
    # get the dataframe
        drug_response = self.df[['prename', 'CIP', 'CTX', 'CTZ', 'GEN']]
        # count the how many isolates are resistant to the drug where 1 stands for resistant
        CIP_number_of_resistance = drug_response[drug_response['CIP'] == 1].count()['CIP']
        CTX_number_of_resistance = drug_response[drug_response['CTX'] == 1].count()['CTX']
        CTZ_number_of_resistance = drug_response[drug_response['CTZ'] == 1].count()['CTZ']
        GEN_number_of_resistance = drug_response[drug_response['GEN'] == 1].count()['GEN']
        # create a dict with the drug name and the number of resistance
        drug_resistance = {'CIP': CIP_number_of_resistance, 'CTX': CTX_number_of_resistance, 'CTZ': CTZ_number_of_resistance, 'GEN': GEN_number_of_resistance}

        # create a bar chart
        drugs = list(drug_resistance.keys())
        resistance_counts = list(drug_resistance.values())

        plt.bar(drugs, resistance_counts, align='center')
        plt.xlabel('Drug')
        plt.ylabel('Resistance Count')
        plt.show()

    
    def create_sunburst_visualization(self):
    # Group the data by drug and count the number of resistance
        drug_counts = self.df[['prename', 'CIP', 'CTX', 'CTZ', 'GEN']].sum()
        
        # Create a dataframe with drug names and counts
        df_drug_counts = pd.DataFrame({'Drug': drug_counts.index, 'Count': drug_counts.values})
        
        # Create the sunburst visualization
        fig = go.Figure(go.Sunburst(labels=df_drug_counts['Drug'], parents=[''] * len(df_drug_counts), values=df_drug_counts['Count']))
        fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))
        fig.show()
# the instance of the Preprocessing class
# path needs to be changed to the location of the dataset of the working machine
prep = Preprocessing('/Users/estefanosk/Desktop/SummerProject/snps-to-2dcnn-converter/Giessen_Dataset/cip_ctx_ctz_gen_multi_data.csv')

# location of the drug response to each isolate
drug_reposne = Preprocessing('/Users/estefanosk/Desktop/SummerProject/snps-to-2dcnn-converter/Giessen_Dataset/cip_ctx_ctz_gen_pheno.csv')

# calling the methods
# prep.get_dataframe()
# prep.count_number_of_features()
# prep.count_number_of_rows()
# drug_reposne.create_data_frame_by_drug_name()
drug_reposne.create_sunburst_visualization()