import sqlite3
import json
import pandas as pd
import datetime
import os



""" 
Aim of class is to have a persistent db to store the data of the latest and past weather
    Input: Latest Data from Api Call
    Output: Want the past data for our UI
    Tools: pandas, sqlite3, datetime, os   
"""

class Data_Bank():
    def __init__(self, latest_data):
        
        self.data = pd.DataFrame([latest_data])

        ##check if db already exists
        if os.path.isfile("my_database.db"):
            self.is_new_db = False
        else:
            self.is_new_db = True

        ## Connect to my_database.db and if not available -> create db
        self.conn = sqlite3.connect("my_database.db")

        ## Include new data into data base with corresponding date 
        self.dates_access = self.date_today_yesterday()
        new_data_entry = self.create_db(self.data)
        new_data_entry.to_sql("weather table" , con=self.conn, index=False, if_exists="append")

    ## get date of today and yesterday 
    def date_today_yesterday(self):
        print(datetime.datetime.now())
        date_today = datetime.date.today()
        day = int(date_today.strftime("%d"))
        year = int(date_today.strftime("%Y"))
        month = date_today.strftime("%m")
        return [f"{day}.{month}.{year}", f"{day-1}.{month}.{year}" ]

    ## First Create Data Frame we want to have 
    ## We want date,lon,lat,weather-main, main-temp,main-temp-feels_like, sys-country
    def create_db(self,df_new):
        df = pd.DataFrame()
        df["date"] = [self.dates_access[0]]
        df["lat"]  = [ float(df_new["coord"][0]["lat"])   ]  ## Need to have brackets here
        df["lon"] = float(df_new["coord"][0]["lon"])
        df["weather"] = df_new["weather"][0][0]["main"]
        df["temp"] = float(df_new["main"][0]["temp"])
        df["temp_feels_like"] = float(df_new["main"][0]["feels_like"])
        df["country"] = df_new["sys"][0]["country"]

        return df
    
    def show_db(self):
        test = pd.read_sql_query("SELECT * FROM weather_bank", self.conn)
        print(test.info())
        print(test)
    
    def get_old_data(self, is_new_db):
        ## If created a new db, only can show the latest fetched data from API call
        if is_new_db:
            date_yesterday = self.dates_access[0]
            print("Not found weather data from yesterday") ## include twice latest data
        else:
            date_yesterday = self.dates_access[1]
            print(date_yesterday)

        ## Query to get weather data from yesterday
        query = "SELECT * FROM weather_bank WHERE date= (?) "
        weather_yesterday = pd.read_sql_query(query, self.conn, params=(date_yesterday,) ) ## need tuple or else read as input seq of length 10!


        print((weather_yesterday))
        return weather_yesterday



