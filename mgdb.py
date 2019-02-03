import urllib
import requests
import zipfile
import io
import pandas as pd
import pymongo

def get_data(url):
    # from a file
    # url = 'https://www.data.gouv.fr/fr/datasets/r/32803cb2-0e0f-41f1-a32e-1fd9ee4fd141'
    rq = requests.get(url).content  # access the response body as bytes from the response object
    data = io.StringIO(rq.decode('utf-8'))  # decode the bytes -> csv file
    df = pd.read_csv(data, sep=';', encoding="utf-8")  # csv to dataframe
    df.columns = df.columns.str.replace('.', '') # MongoDB uses the dot notation to access the elements of an array and to access the fields of an embedded document.
    df['Session'] = df['Session'].fillna(0).astype(int).astype(str)
    df['Code département'] = df['Code département'].fillna(0).astype(int).astype(str)
    df[df.columns[-7:]] = df[df.columns[-7:]].round(2)
    return df

def create_db(client,url):
    #apb_collection.count():
    if 'db_apb' not in client.list_database_names():
        data = get_data(url)
        db_apb = client["db_apb"] #creating a database
        apb_collection =  db_apb["apb"] #creating a collection in the previously created database
        apb_collection.insert_many(data.to_dict('records')) #inserting the data previously converted to a dataframe
    else:
        print("The database already exists")

    return client.db_apb.apb
        