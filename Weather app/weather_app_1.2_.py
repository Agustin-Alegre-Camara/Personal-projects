
from tkinter import *
from tkinter import messagebox
import requests
import os
from datetime import datetime
import customtkinter
from PIL import Image


class Weather_App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Weather app')

        # Load and create background images

        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image1 = customtkinter.CTkImage(Image.open(current_path + "/images/sunny_weather.jpg"),
                                               size=(700, 800))
        self.bg_image2 = customtkinter.CTkImage(Image.open(current_path + "/images/snow.jpg"),
                                               size=(700, 800))
        self.bg_image3 = customtkinter.CTkImage(Image.open(current_path + "/images/rain.jpeg"),
                                               size=(700, 800))
        self.bg_image4 = customtkinter.CTkImage(Image.open(current_path + "/images/few_clouds_weather.jpg"),
                                               size=(700, 800))
        self.bg_image5 = customtkinter.CTkImage(Image.open(current_path + "/images/cloudy.jpg"),
                                               size=(700, 800))
        self.bg_image6 = customtkinter.CTkImage(Image.open(current_path + "/images/drizzle.jpeg"),
                                               size=(700, 800))
        self.bg_image7 = customtkinter.CTkImage(Image.open(current_path + "/images/foggy.jpg"),
                                               size=(700, 800))
        self.bg_image8 = customtkinter.CTkImage(Image.open(current_path + "/images/lightning_storm.jpg"),
                                               size=(700, 800))
        self.images =[self.bg_image1, self.bg_image2, self.bg_image3, self.bg_image4, self.bg_image5, self.bg_image6, self.bg_image7, self.bg_image8]  


        # Load and create icon images

        current_path = os.path.dirname(os.path.realpath(__file__))
        self.icon_image1 = customtkinter.CTkImage(Image.open(current_path + "/icon_images/01d@2x.png"),
                                               size=(20, 20))
        self.icon_image2 = customtkinter.CTkImage(Image.open(current_path + "/icon_images/02d@2x.png"),
                                               size=(20, 20))
        self.icon_image3 = customtkinter.CTkImage(Image.open(current_path + "/icon_images/03d@2x.png"),
                                               size=(20, 20))
        self.icon_image4 = customtkinter.CTkImage(Image.open(current_path + "/icon_images/04d@2x.png"),
                                               size=(20, 20))
        self.icon_image5 = customtkinter.CTkImage(Image.open(current_path + "/icon_images/09d@2x.png"),
                                               size=(20, 20))
        self.icon_image6 = customtkinter.CTkImage(Image.open(current_path + "/icon_images/10d@2x.png"),
                                               size=(20, 20))
        self.icon_image7 = customtkinter.CTkImage(Image.open(current_path + "/icon_images/11d@2x.png"),
                                               size=(20, 200))
        self.icon_image8 = customtkinter.CTkImage(Image.open(current_path + "/icon_images/13d@2x.png"),
                                               size=(20, 20))
        self.icon_image9 = customtkinter.CTkImage(Image.open(current_path + "/icon_images/50d@2x.png"),
                                               size=(20, 20))

        self.icon_images =[self.icon_image1, self.icon_image2, self.icon_image3, self.icon_image4, self.icon_image5, self.icon_image6, self.icon_image7, self.icon_image8, self.icon_image9] 

        # Main page development

        self.bg_frame = customtkinter.CTkFrame(master=self)
        self.bg_frame.grid(row=0, column=0, columnspan=3, rowspan=6)
        self.dinamic_bg()
        self.label = customtkinter.CTkLabel(master=self, text="Tino's weather app", font=('Apoc', 38), fg_color='#fff4e6',  text_color='#523023')
        self.label.grid(row=0, column=0, pady=12, padx=10, sticky='nw')

        self.search_entry =customtkinter.CTkEntry(master=self, placeholder_text='Enter city', fg_color='#fff4e6', text_color='#523023', bg_color='#2f1c14', \
                                                  border_color='#2f1c14', placeholder_text_color='#523023', font=('Apoc', 16))
        self.search_entry.grid(row=0, column=0, pady=12, padx=10,sticky='se')

        self.search_button = customtkinter.CTkButton(master=self, text='Search', command=self.search_location, fg_color='#fff4e6', bg_color='#2f1c14', \
                                                     border_color='#2f1c14', hover_color='#2f1c14',  text_color='#2f1c14', font=('Apoc', 16))
        self.search_button.grid(row=0, column=1, pady=12, padx=10, sticky='s')

        self.about_me_button = customtkinter.CTkButton(master=self, text='About me', command=self.about_me, fg_color='#00ff7f', bg_color='#00ff7f', \
                                                       text_color='black', hover_color='#00ff7f', font=('Apoc', 16))
        self.about_me_button.grid(row=0, column=2, pady=12, padx=10, sticky='ne')

    def search_location(self): # Method to find weather conditions of the location given by the user.
        try:
            # Collection of the data through an API.

            api_key = 'bafc2506ebf850f112d2fc75ad92def8'
            complete_api_link = 'https://api.openweathermap.org/data/2.5/weather?q='+ self.search_entry.get()+ '&appid='+str(api_key)
            api_link = requests.get(complete_api_link)
            api_data = api_link.json()

            city_temp = ((api_data["main"]["temp"]) - 273.15)
            temp_like = ((api_data['main']['feels_like']) - 273.15)
            pressure = ((api_data['main']['pressure']))
            weather_main = api_data['weather'][0]['main']
            weather_description = api_data['weather'][0]['description']
            weather_id = api_data['weather'][0]['id']
            hmdt = api_data['main']['humidity']
            wind_speed = api_data['wind']['speed']
            visibility = api_data['visibility']
            sunrise = datetime.utcfromtimestamp(api_data['sys']['sunrise'] + 3600).strftime('%H:%M')
            sunset = datetime.utcfromtimestamp(api_data['sys']['sunset'] + 3600).strftime('%H:%M')
            date_and_time = datetime.now().strftime('%d %b %Y | %H:%M (+01:00 UTC)')

            # Background display after first search and onwards.

            self.label.destroy
            self.configure(background = '#00ff7f')
            self.weather_bg = customtkinter.CTkFrame(master=self)
            self.weather_bg.grid(row=0, column=0, columnspan=3, rowspan=6)

            if weather_main == 'Thunderstorm':
                self.bg_image_label = customtkinter.CTkLabel(master=self, image=self.images[7])
                self.bg_image_label.grid(row=0, column=0, columnspan=3, rowspan=6, sticky='swe')
                icon_label = customtkinter.CTkLabel(master=self, image=self.icon_images[6], text='')
                icon_label.grid(row=2, column=0, columnspan=1, pady=12, padx=10, sticky='ne')

                self.search_entry =customtkinter.CTkEntry(master=self, placeholder_text='Enter city', fg_color='white', text_color='black', bg_color='#00ff7f', \
                                                          border_color='#00ff7f', placeholder_text_color='black', font=('Apoc', 16))
                self.search_entry.grid(row=0, column=0, pady=12, padx=10,sticky='se')

                self.search_button = customtkinter.CTkButton(master=self, text='Search', command=self.search_location, fg_color='#00ff7f', bg_color='#00ff7f', \
                                                             hover_color='#00ff7f', text_color='black', font=('Apoc', 16))
                self.search_button.grid(row=0, column=1, pady=12, padx=10, sticky='sw')

                self.about_me_button = customtkinter.CTkButton(master=self, text='About me', command=self.about_me, fg_color='#00ff7f', bg_color='#00ff7f', \
                                                               text_color='black', hover_color='#00ff7f', font=('Apoc', 16))
                self.about_me_button.grid(row=0, column=2, pady=12, padx=10, sticky='se')

            elif weather_main == 'Drizzle':
                self.bg_image_label = customtkinter.CTkLabel(master=self, image=self.images[5])
                self.bg_image_label.grid(row=0, column=0, columnspan=3, rowspan=6, sticky='swe')
                icon_label = customtkinter.CTkLabel(master=self, image=self.icon_images[4], text='')
                icon_label.grid(row=2, column=0, columnspan=1, pady=12, padx=10, sticky='ne')

                self.search_entry =customtkinter.CTkEntry(master=self, placeholder_text='Enter city', fg_color='white', text_color='black', bg_color='#00ff7f', \
                                                          border_color='#00ff7f', placeholder_text_color='black', font=('Apoc', 16))
                self.search_entry.grid(row=0, column=0, pady=12, padx=10,sticky='se')

                self.search_button = customtkinter.CTkButton(master=self, text='Search', command=self.search_location, fg_color='#00ff7f', bg_color='#00ff7f', \
                                                             hover_color='#00ff7f', text_color='black', font=('Apoc', 16))
                self.search_button.grid(row=0, column=1, pady=12, padx=10, sticky='sw')

                self.about_me_button = customtkinter.CTkButton(master=self, text='About me', command=self.about_me, fg_color='#00ff7f', bg_color='#00ff7f', \
                                                               text_color='black', hover_color='#00ff7f', font=('Apoc', 16))
                self.about_me_button.grid(row=0, column=2, pady=12, padx=10, sticky='se')

            elif weather_main == 'Rain':
                self.bg_image_label = customtkinter.CTkLabel(master=self, image=self.images[2])
                self.bg_image_label.grid(row=0, column=0, columnspan=3, rowspan=6, sticky='swe')
                icon_label = customtkinter.CTkLabel(master=self, image=self.icon_images[5], text='')
                icon_label.grid(row=2, column=0, columnspan=1, pady=12, padx=10, sticky='ne')

                self.search_entry =customtkinter.CTkEntry(master=self, placeholder_text='Enter city', fg_color='white', text_color='black', bg_color='#00ff7f', \
                                                          border_color='#00ff7f', placeholder_text_color='black', font=('Apoc', 16))
                self.search_entry.grid(row=0, column=0, pady=12, padx=10,sticky='se')

                self.search_button = customtkinter.CTkButton(master=self, text='Search', command=self.search_location, fg_color='#00ff7f', bg_color='#00ff7f', \
                                                             hover_color='#00ff7f', text_color='black', font=('Apoc', 16))
                self.search_button.grid(row=0, column=1, pady=12, padx=10, sticky='sw')

                self.about_me_button = customtkinter.CTkButton(master=self, text='About me', command=self.about_me, fg_color='#00ff7f', bg_color='#00ff7f', \
                                                               text_color='black', hover_color='#00ff7f', font=('Apoc', 16))
                self.about_me_button.grid(row=0, column=2, pady=12, padx=10, sticky='se')

            elif weather_main == 'Snow':
                self.bg_image_label = customtkinter.CTkLabel(master=self, image=self.images[1])
                self.bg_image_label.grid(row=0, column=0, columnspan=3, rowspan=6, sticky='swe')
                icon_label = customtkinter.CTkLabel(master=self, image=self.icon_images[7], text='')
                icon_label.grid(row=2, column=0, columnspan=1, pady=12, padx=10, sticky='ne')

                self.search_entry =customtkinter.CTkEntry(master=self, placeholder_text='Enter city', fg_color='white', text_color='black', bg_color='#00ff7f', \
                                                          border_color='#00ff7f', placeholder_text_color='black', font=('Apoc', 16))
                self.search_entry.grid(row=0, column=0, pady=12, padx=10,sticky='se')

                self.search_button = customtkinter.CTkButton(master=self, text='Search', command=self.search_location, fg_color='#00ff7f', bg_color='#00ff7f', \
                                                             hover_color='#00ff7f', text_color='black', font=('Apoc', 16))
                self.search_button.grid(row=0, column=1, pady=12, padx=10, sticky='sw')

                self.about_me_button = customtkinter.CTkButton(master=self, text='About me', command=self.about_me, fg_color='#00ff7f', bg_color='#00ff7f', \
                                                               text_color='black', hover_color='#00ff7f', font=('Apoc', 16))
                self.about_me_button.grid(row=0, column=2, pady=12, padx=10, sticky='se')
            
            elif weather_main == 'Atmosphere':
                self.bg_image_label = customtkinter.CTkLabel(master=self, image=self.images[3])
                self.bg_image_label.grid(row=0, column=0, columnspan=3, rowspan=6, sticky='swe')
                icon_label = customtkinter.CTkLabel(master=self, image=self.icon_images[8], text='')
                icon_label.grid(row=2, column=0, columnspan=1, pady=12, padx=10, sticky='ne')

                self.search_entry =customtkinter.CTkEntry(master=self, placeholder_text='Enter city', fg_color='white', text_color='black', bg_color='#00ff7f', \
                                                          border_color='#00ff7f', placeholder_text_color='black', font=('Apoc', 16))
                self.search_entry.grid(row=0, column=0, pady=12, padx=10,sticky='se')

                self.search_button = customtkinter.CTkButton(master=self, text='Search', command=self.search_location, fg_color='#00ff7f', bg_color='#00ff7f', \
                                                             hover_color='#00ff7f', text_color='black', font=('Apoc', 16))
                self.search_button.grid(row=0, column=1, pady=12, padx=10, sticky='sw')

                self.about_me_button = customtkinter.CTkButton(master=self, text='About me', command=self.about_me, fg_color='#00ff7f', bg_color='#00ff7f', \
                                                               text_color='black', hover_color='#00ff7f', font=('Apoc', 16))
                self.about_me_button.grid(row=0, column=2, pady=12, padx=10, sticky='se')

            elif weather_main == 'Clear':
                self.bg_image_label = customtkinter.CTkLabel(master=self, image=self.images[0])
                self.bg_image_label.grid(row=0, column=0, columnspan=3, rowspan=6, sticky='swe')
                icon_label = customtkinter.CTkLabel(master=self, image=self.icon_images[0], text='')
                icon_label.grid(row=2, column=0, columnspan=1, pady=12, padx=10, sticky='ne')

                self.search_entry =customtkinter.CTkEntry(master=self, placeholder_text='Enter city', fg_color='white', text_color='black', bg_color='#00ff7f', \
                                                          border_color='#00ff7f', placeholder_text_color='black', font=('Apoc', 16))
                self.search_entry.grid(row=0, column=0, pady=12, padx=10,sticky='se')

                self.search_button = customtkinter.CTkButton(master=self, text='Search', command=self.search_location, fg_color='#00ff7f', bg_color='#00ff7f', \
                                                             hover_color='#00ff7f', text_color='black', font=('Apoc', 16))
                self.search_button.grid(row=0, column=1, pady=12, padx=10, sticky='sw')

                self.about_me_button = customtkinter.CTkButton(master=self, text='About me', command=self.about_me, fg_color='#00ff7f', bg_color='#00ff7f', \
                                                               text_color='black', hover_color='#00ff7f', font=('Apoc', 16))
                self.about_me_button.grid(row=0, column=2, pady=12, padx=10, sticky='se')

            elif weather_main == 'Clouds':
                self.bg_image_label = customtkinter.CTkLabel(master=self, image=self.images[3])
                self.bg_image_label.grid(row=0, column=0, columnspan=4, rowspan=6, sticky='swe')
                icon_label = customtkinter.CTkLabel(master=self, image=self.icon_images[3], text='')
                icon_label.grid(row=2, column=0, columnspan=1, pady=12, padx=10, sticky='ne')

                self.search_entry =customtkinter.CTkEntry(master=self, placeholder_text='Enter city', fg_color='white', text_color='black', bg_color='#00ff7f', \
                                                          border_color='#00ff7f', placeholder_text_color='black', font=('Apoc', 16))
                self.search_entry.grid(row=0, column=0, pady=12, padx=10,sticky='se')

                self.search_button = customtkinter.CTkButton(master=self, text='Search', command=self.search_location, fg_color='#00ff7f', bg_color='#00ff7f', \
                                                             hover_color='#00ff7f', text_color='black', font=('Apoc', 16))
                self.search_button.grid(row=0, column=1, pady=12, padx=10, sticky='sw')

                self.about_me_button = customtkinter.CTkButton(master=self, text='About me', command=self.about_me, fg_color='#00ff7f', bg_color='#00ff7f', \
                                                               text_color='black', hover_color='#00ff7f', font=('Apoc', 16))
                self.about_me_button.grid(row=0, column=2, pady=12, padx=10, sticky='se')

            
            # Weather description display

            date_label = customtkinter.CTkLabel(self, text=str(date_and_time), font=('Apoc', 14), text_color='black', bg_color='#00ff7f', fg_color='#b4eeb4')
            date_label.grid(row=2, column=1, columnspan=1, pady=12, padx=10, sticky='nwe')

            
            temp_frame = customtkinter.CTkFrame(master=self, height=150, width=225, bg_color='#00ff7f', fg_color='#b4eeb4')
            temp_frame.grid(row=3, column=0, pady=12, padx=20, sticky='nesw')
            temp_title_label = customtkinter.CTkLabel(master=temp_frame, text="Temperature (ºC)", font=('Apoc', 14), fg_color='#00ff7f', text_color='black')
            temp_title_label.grid(row=0, column=0, pady=12, padx=0, sticky='nw')
            temp_label = customtkinter.CTkLabel(temp_frame, text='{0:.0f}ºC'.format(city_temp), font=('Apoc', 14), text_color='black')
            temp_label.grid(row=1, column=0, pady=12, padx=10, sticky='e')

            feels_frame = customtkinter.CTkFrame(master=self, height=150, width=225, bg_color='#00ff7f', fg_color='#b4eeb4')
            feels_frame.grid(row=3, column=1, pady=12, padx=10, sticky='nesw')
            feels_title_label = customtkinter.CTkLabel(master=feels_frame, text="Feels like (ºC)", font=('Apoc', 14), fg_color='#00ff7f', text_color='black')
            feels_title_label.grid(row=0, column=0, pady=12, padx=0, sticky='nw')
            feels_label = customtkinter.CTkLabel(feels_frame, text='{0:.0f}ºC'.format(temp_like), font=('Apoc', 14), text_color='black')
            feels_label.grid(row=1, column=0, pady=12, padx=10, sticky='e')

            description_frame = customtkinter.CTkFrame(master=self, height=150, width=225, bg_color='#00ff7f', fg_color='#b4eeb4')
            description_frame.grid(row=4, column=0, pady=12, padx=20, sticky='nesw')
            description_title_label = customtkinter.CTkLabel(master=description_frame, text="Weather description", font=('Apoc', 14), fg_color='#00ff7f', \
                                                             text_color='black')
            description_title_label.grid(row=0, column=0, pady=12, padx=0, sticky='nw')
            description_label = customtkinter.CTkLabel(description_frame, text='{0}'.format(weather_description), font=('Apoc', 14), text_color='black')
            description_label.grid(row=1, column=0, pady=12, padx=10, sticky='e')

            pressure_frame = customtkinter.CTkFrame(master=self, height=150, width=225, bg_color='#00ff7f', fg_color='#b4eeb4')
            pressure_frame.grid(row=4, column=1, pady=12, padx=10, sticky='nesw')
            pressure_title_label = customtkinter.CTkLabel(master=pressure_frame, text="Pressure (Pa)", font=('Apoc', 14), fg_color='#00ff7f', text_color='black')
            pressure_title_label.grid(row=0, column=0, pady=12, padx=0, sticky='w')
            pressure_label = customtkinter.CTkLabel(pressure_frame, text='{0} Pa'.format(pressure), font=('Apoc', 14), text_color='black')
            pressure_label.grid(row=1, column=0, pady=12, padx=10, sticky='e')

            humidity_frame = customtkinter.CTkFrame(master=self, height=150, width=225, bg_color='#00ff7f', fg_color='#b4eeb4')
            humidity_frame.grid(row=5, column=0, pady=12, padx=20, sticky='nesw')
            humidity_title_label = customtkinter.CTkLabel(master=humidity_frame, text="Humidity (%)", font=('Apoc', 14), fg_color='#00ff7f', text_color='black')
            humidity_title_label.grid(row=0, column=0, pady=12, padx=0, sticky='w')
            humidity_label = customtkinter.CTkLabel(humidity_frame, text='{0}%'.format(hmdt), font=('Apoc', 14), text_color='black')
            humidity_label.grid(row=1, column=0, pady=12, padx=10, sticky='e')

            wind_frame = customtkinter.CTkFrame(master=self, height=150, width=225, bg_color='#00ff7f', fg_color='#b4eeb4')
            wind_frame.grid(row=5, column=1, pady=12, padx=10, sticky='nesw')
            wind_title_label = customtkinter.CTkLabel(master=wind_frame, text="Wind speed (Km/h)", font=('Apoc', 14), fg_color='#00ff7f', text_color='black')
            wind_title_label.grid(row=0, column=0, pady=12, padx=0, sticky='nw')
            wind_label = customtkinter.CTkLabel(wind_frame, text='{0:.0f} Km/h'.format(wind_speed), font=('Apoc', 14), text_color='black')
            wind_label.grid(row=1, column=0, pady=12, padx=10, sticky='e')

            visibility_frame = customtkinter.CTkFrame(master=self, height=150, width=225, bg_color='#00ff7f', fg_color='#b4eeb4')
            visibility_frame.grid(row=3, column=2, pady=12, padx=10, sticky='nesw')
            visibility_title_label = customtkinter.CTkLabel(master=visibility_frame, text="Visibility (Km)", font=('Apoc', 14), fg_color='#00ff7f', text_color='black')
            visibility_title_label.grid(row=0, column=0, pady=12, padx=0, sticky='nw')
            visibility_label = customtkinter.CTkLabel(visibility_frame, text='{0:.0f} Km'.format(visibility/1000), font=('Apoc', 14), text_color='black')
            visibility_label.grid(row=1, column=0, pady=12, padx=10, sticky='e')

            sunrise_frame = customtkinter.CTkFrame(master=self, height=150, width=225, bg_color='#00ff7f', fg_color='#b4eeb4')
            sunrise_frame.grid(row=4, column=2, pady=12, padx=10, sticky='nesw')
            sunrise_title_label = customtkinter.CTkLabel(master=sunrise_frame, text="Sunrise", font=('Apoc', 14), fg_color='#00ff7f', text_color='black')
            sunrise_title_label.grid(row=0, column=0, pady=12, padx=0, sticky='nw')
            sunrise_label = customtkinter.CTkLabel(sunrise_frame, text=sunrise, font=('Apoc', 14), text_color='black')
            sunrise_label.grid(row=1, column=0, pady=12, padx=10, sticky='e')

            sunset_frame = customtkinter.CTkFrame(master=self, height=150, width=225, bg_color='#00ff7f', fg_color='#b4eeb4')
            sunset_frame.grid(row=5, column=2, pady=12, padx=10, sticky='nesw')
            sunset_title_label = customtkinter.CTkLabel(master=sunset_frame, text="Sunset", font=('Apoc', 14), fg_color='#00ff7f', text_color='black')
            sunset_title_label.grid(row=0, column=0, pady=12, padx=0, sticky='nw')
            sunset_label = customtkinter.CTkLabel(sunset_frame, text=sunset, font=('Apoc', 14), text_color='black')
            sunset_label.grid(row=1, column=0, pady=12, padx=10, sticky='e')

        except Exception:
            messagebox.showerror('Error message', 'Excuse us, we do not have data for {0} yet.'.format(self.search_entry.get()))

    # Definition of 'about me' space 
    def about_me(self):
        my_text = "Hi, I'm Tino!\
 \nI'm an ambitious, hard-working and naturally curious individual with a  passion for science,  computing and \ndefence technology.\
 \nWith a background in \nPhysics and a strong foundation in Software \nEngineering, I enjoy diving \ninto creative projects that \nchallenge me to learn new programming languages\
 \nand frameworks, while \napplying and refining my \nexisting skills."
        about_me_frame = customtkinter.CTkFrame(master=self, height=800, width=80, bg_color='#00ff7f', fg_color='#00ff7f')
        about_me_frame.grid(row=0, column=2, columnspan=3, rowspan=6, pady=12, padx=10, sticky='nwe')
        close_button = customtkinter.CTkButton(master=about_me_frame, text='close',height=40, width=50, command=about_me_frame.destroy, fg_color='#00ff7f', \
                                                  text_color='black', hover_color='#00ff7f')
        close_button.grid(row=0, column=1, pady=12, padx=10, sticky='e')
        about_me_textbox= customtkinter.CTkTextbox(master=about_me_frame, font=('Apoc', 12), text_color='black', fg_color='#00ff7f', bg_color='#00ff7f', width=175)
        about_me_textbox.insert("0.0", my_text)
        about_me_textbox.grid(row=1, column=0,columnspan=2, pady=12, padx=10, sticky='nwes')

    # Definitonn of the dinamic background when the app is launched  
    global count
    count = -1
    def dinamic_bg(self):
        global count
        if count == 7:
            self.bg_image_label = customtkinter.CTkLabel(master=self.bg_frame, text='', image=self.images[0])
            self.bg_image_label.grid(row=0, column=0, columnspan=3, rowspan=6)
            count = 0
        else:
            self.bg_image_label = customtkinter.CTkLabel(master=self.bg_frame, text='', image=self.images[count+1])
            self.bg_image_label.grid(row=0, column=0, columnspan=3, rowspan=6)
            count += 1            
        self.after(5000, self.dinamic_bg)

Weather_App().mainloop()