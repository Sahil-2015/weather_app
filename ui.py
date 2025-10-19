import tkinter as tk   

""" 
Aim of class is to only show the weather of today and yesterday and calculate the temperature difference
    Input: Latest weather data and from yesterday
    Output: Show on GUI the weather data
    Tools: tkinter
"""


class WeatherInterface:

    def __init__(self, data_today, old_data, is_new_db):
        window = tk.Tk()
        window.title("Wheater App")
        self.today = data_today
        self.yesterday= old_data
        self.is_new_db = is_new_db

        ## Variables for API Call
        self.API_lat = 0
        self.API_lon = 0
        # self.create_layout()
        self.user_input()
        window.config(padx=30,pady=30)

        window.mainloop()
    

    def create_layout(self):
        data_today = (self.today)["main"]["temp"]
        data_today2 = (self.today)["main"]["feels_like"]

        t_today = tk.Label(text=f"Temperature today: {(data_today)}\u00b0")
        t_today.grid(row=0,column=0)

        t_today_feel = tk.Label(text=f"Temperature today feels like: {data_today2}\u00b0 ")
        t_today_feel.grid(row =1, column=0)
        
        if self.is_new_db == False: 
            data_yesterday = (self.yesterday)["temp"][0]
            data_yesterday2 = (self.yesterday)["temp_feels_like"][0]
            
            t_yesterday = tk.Label(text=f"Temperature yesterday: {data_yesterday}\u00b0 ")
            t_yesterday.grid(row=0,column=1)

            t_yesterday_feel = tk.Label(text=f"Temperatur yesterday felt like: {data_yesterday2}\u00b0 ")
            t_yesterday_feel.grid(row=1, column=1)


            t_delta = tk.Label(text=f"Temperature Differenz: {abs(float(data_today)) - abs(float(data_yesterday))}\u00b0")    
            t_delta.grid(row=2 , column=2)
        else:
            print("Only able to show the today's weather")


    def user_input(self):
        input_lat_label = tk.Label(text="Lat:")
        input_lat_label.grid(row=3, column=0)
        self.text_lat = tk.Entry()
        self.text_lat.grid(row=3,column=1)
        input_lon_label = tk.Label(text="Lon:")
        input_lon_label.grid(row=4, column=0)
        self.text_lon = tk.Entry()
        self.text_lon.grid(row=4,column=1)
        button = tk.Button(text="Start",command=self.print_input  )
        button.grid(row=3, column=2)
        
    def print_input(self):
        # print(self.text_lat.get())
        # print(self.text_lon.get())
        self.API_lat = self.text_lat.get()
        self.API_lon = self.text_lon.get()

