import requests
import pandas as pd
import json 
import psycopg2
from sqlalchemy import create_engine
import os


#API fails --> pipeline continues safely 
url = "https://openlibrary.org/search.json?q=personal+development"

headers = {
    "User-Agent": "Mozilla/5.0"
}

x = requests.get(url, headers=headers)

print("Status:", x.status_code)

if x.status_code == 200:
    json_data = x.json()
    
    if 'docs' in json_data:
        data = json_data['docs']
    else:
        print(" docs not found")
        data = []
else:
    print("Request failed")
    data = []

with open("books.json","w",encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii=False,indent=2)

new_data=pd.read_json("books.json")

df=new_data.copy()

# transform
# keep only the required columns
df=df[['title','author_name','first_publish_year', 'language']]

print(df.columns)

# convert list to a string
df['author_name']= df['author_name'].apply(lambda x: x[0] if isinstance(x,list) else x)
df['language'] = df['language'].apply(lambda x: x[0] if isinstance(x, list) else x)

# filling missing values
# df.isnull().sum()
df['author_name']=df['author_name'].fillna("Unknown")
df['first_publish_year']=df['first_publish_year'].fillna(0)
df['language']=df['language'].fillna("Unknown")
# type converting
# df.dtypes
df['title']=df['title'].astype(str)
df['author_name']=df['author_name'].astype(str)
df['first_publish_year']=df['first_publish_year'].round().astype(int)
df['language']=df['language'].astype(str)

# remove duplicates
# df.duplicated().sum()
df.drop_duplicates(inplace=True)
#orient='records' converts a pandas DataFrame into a list of dictionaries. 
#force_ascii=False is used in specific Python libraries, most notably the built-in json module and the pandas library's to_json() method, to preserve non-ASCII characters as Unicode strings rather than escaping them into \uXXXX
df.to_json("books_cleaned.json",orient="records",force_ascii=False, indent=2)

with open("books_cleaned.json", "r",encoding="UTF-8") as f:
    cleaned_books= json.load(f)

print(cleaned_books[:5])

conn=psycopg2.connect(
    host="localhost",
    port= 5434,
    database="booksdb",
    user= "admin",
    password="psd00"

)
# create a cursor to execute SQL commands
cursor=conn.cursor()

# load it to postgreSQL
engine=create_engine("postgresql+psycopg2://admin:psd00@localhost:5434/booksdb")

#load the cleaned json file into a dataframe
df_cleaned = pd.read_json("books_cleaned.json")

# insert into postgreSQL table
# index=False
df_cleaned.to_sql("books",engine, if_exists="append", index=False)

print("Data inserted into PostgreSQL")
