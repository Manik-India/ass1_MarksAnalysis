#importing necessary modules
import logging
import pandas as pd
import sys

#This section is used to make log file with timings and messages
logging.basicConfig(filename="101903077.log",format='%(asctime)s %(message)s',filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.info("Kindly pass two arguments in command line: one is py file name and the other is csv file..")

#Following Section is used to take the input.csv from the command line
file_name = sys.argv[1]
n = len(sys.argv)

if(n>2 or n<2):
    logger.warning("More or less than 2 input parameters have passed")
if(file_name != 'input.csv'):
    logger.error("File not Found.")

try: 
    df = pd.read_csv(file_name)

    df['Marks'].replace('X',0,inplace = True)
    df['Marks'].replace('-',0,inplace = True)
    df['Marks'].replace('NAN',0,inplace = True)
    df.fillna(0, inplace = True)

    df["Marks"] = df["Marks"].astype(str).astype(int)

    #Transforms the input.csv to the required data 
    table = pd.pivot_table( df, values='Marks', index=['RollNumber'],columns=['Submission'])

    #replace the corrupted data with mean of the subject.
    table['P1'].replace(0,table['P1'].mean(),inplace = True)
    table['P2'].replace(0,table['P2'].mean(),inplace = True)
    table['P3'].replace(0,table['P3'].mean(),inplace = True)
    table['P4'].replace(0,table['P4'].mean(),inplace = True)
    table['P5'].replace(0,table['P5'].mean(),inplace = True)

    #filling null values with 0
    table.fillna(0, inplace= True)

    #converting the object values to int
    table['P1']= table['P1'].astype(int)
    table['P2']= table['P2'].astype(int)
    table['P3']= table['P3'].astype(int)
    table['P4']= table['P4'].astype(int)
    table['P5']= table['P5'].astype(int)

    #convert tables to .csv file
    table.to_csv("101903077-output.csv")

except:
    logger.error("File not Found")