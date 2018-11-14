#importing libraries 
import pandas as pd 
from textblob import TextBlob

#defining the function
def quick_sentiment(path_to_csv, colname_with_text): 
    #csv to pandas dataframe
    df = pd.read_csv(path_to_csv, index_col=None, 
                     low_memory=False,encoding='utf8', 
                     sep=';', error_bad_lines=False)
    #selects needed column 
    df_temp = pd.DataFrame(df[colname_with_text])
    #calls TextBlob function on each row in that column  
    sentiments = []
    for index, row in df_temp.iterrows():
        row_str = row.to_string()
        blob = TextBlob(row_str)
        polarity = blob.sentiment.polarity
        sentiments.append(polarity)
    #adds new columns to dataframe
    df['sent'] = sentiments 
    df['sent_class']=df['sent'].apply(lambda row: 'undef' if row==0 else 'pos' if row>0 else 'neg')
    df.to_csv(path_to_csv, encoding='utf8', sep=';')
    return df

#calling the function 
''' 1. create a variable, where new dataframe should be stored (in this example: new_df)
    2. call the function 'quick_sentiment' with two arguments: 
        1)path to the csv file (new csv will replace the old one)   
        2)the column with text to be analyzed  
'''
new_df = quick_sentiment(r"C:\Users\kondratievr\Desktop\tweets.csv","text")

 

#             

