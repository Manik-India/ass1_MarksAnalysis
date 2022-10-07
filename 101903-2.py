#importing necessary packages 
import sys
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import seaborn as sns

def summary_series(series):
    series = pd.to_numeric(series, errors="coerce")
    return series.describe()

#Following function shows the statistics of the file named output.csv
def statistics_manik(df):
    with open('101903077-statistics.txt', 'w') as f:
        for i in range(1, df.shape[1]):
            series = df.iloc[:, i]
            cnt = 0
            for x in series:
                if isinstance(x, str) and not x.isdigit():
                    cnt += 1
            f.write(f'Count Character : {cnt}\n')
            f.write(f'Count NaN: {series.isna().sum()}\n')
            f.write(str(summary_series(series)))

#Following function will make the Histogram
def histogram_manik(df):
    for col in df.iloc[:, 1:]:
        plt.hist(df[col])
        plt.title("Histrogram: Made by Manik")
        plt.grid()
        plt.savefig('101903077-histogram.png')
        plt.close()

#Following Function will make the Piechart 
def piechart_manik(df):
    for col in df.iloc[:, 1:]:
        series = df[col]
        series.dropna(inplace=True)
        counter = dict(Counter(series))
        plt.pie(counter.values(), labels=counter.keys())
        plt.title("Piechart: Made by Manik")
        plt.legend()
        plt.savefig('101903077-piechart.png')
        plt.close() 

#Following Function will make the Line Chart 
def line_manik(df):
    """Makes no sense as requires x as well as y"""
    for col in df.iloc[:, 1:]:
        series = df[col]
        plt.plot(df.iloc[:, 0], series)
        plt.title("Line Chart: Made by Manik")
        plt.grid()
        plt.xlabel('RollNumber')
        plt.ylabel(col)
        plt.savefig('101903077-line.png')
        plt.close()   

#Following Function will make the Bar Graph
def bar_manik(df):
    for col in df.iloc[:, 1:]:
        series = df[col]
        plt.bar( series, df.iloc[:, 0])
        plt.title("Bar Graph: Made by Manik")
        plt.grid()
        plt.xlabel(col)
        plt.ylabel('Roll Number')
        plt.savefig('101903077-bar.png')
        plt.close()

#Following  Function will make the Scatter points graph
def scatter_manik(df):
    for col in df.iloc[:, 1:]:
        series = df[col]
        plt.scatter( series, df.iloc[:, 0])
        plt.title("Scatter Plot: Made by Manik")
        plt.grid()
        plt.xlabel(col)
        plt.ylabel('Roll Number')
        plt.savefig('101903077-scatter.png')
        plt.close() 

def boxplot_manik(df):
    for col in df.iloc[:, 1:]:
        series = df[col]
        sns.boxplot(series)
        plt.savefig('101903077-boxplot.png')
        plt.close()

def manik():
    #Here the argument will be taken from the command line(from terminal)
    file_name = sys.argv[1]
    n = len(sys.argv)
    if(n>2 or n<2):
        print('Wrong Number of arguments passed', file = log_file)
        return 0
    if(file_name != '101903077-output.csv'):
        print("File not found...", file = log_file)
        return 0
    else:
        df = pd.read_csv(file_name)  
        
        #Displays Statistics
        statistics_manik(df)
        print('Wrote Statistics...', file=log_file)
        
        #Display various Graphs
        df['total'] = df.iloc[:, 1:].sum(axis=1, numeric_only=True)
        histogram_manik(df)
        print('Made histograms...', file=log_file)
        piechart_manik(df)
        print('Made Piechart...', file=log_file)
        line_manik(df)
        print('Made Line graph...', file=log_file)
        bar_manik(df)
        print('Made Bar Graph...', file=log_file)
        scatter_manik(df)
        print('Made Scatter Plot...', file=log_file)
        boxplot_manik(df)
        print('Made BoxPlot...', file=log_file)
        print('\n\n\n', file = log_file)

if __name__ == '__main__':
    log_file = open('101903077-log.txt', 'a')
    manik()
    log_file.close()