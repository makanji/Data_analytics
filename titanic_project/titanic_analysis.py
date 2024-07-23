#importation of needed libraries and dependance 
import pandas as pd

#load the titanic dataset from Github
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_data = pd.read_csv(url)
# Display the first few rows of the dataset
print(titanic_data.head())