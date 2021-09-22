class CurrentWeather:

    def __init__(self):
        self.temp = 0.
        self.feels_like = 0.
        self.temp_min = 0.
        self.temp_max = 0.
        self.pressure = 0.
        self.humidity = 0.
        self.sky_description = None
        self.wind_speed = 0.
        
    def __str__(self):
        return f"{self.temp}, {self.feels_like}, {self.temp_min}, {self.temp_max}, {self.pressure}, {self.humidity}, {self.sky_description}, {self.wind_speed}"

    def setMain(self, main):
        self.temp = main['temp']
        self.feels_like = main['feels_like']
        self.temp_min = main['temp_min']
        self.temp_max = main['temp_max']
        self.pressure = main['pressure']
        self.humidity = main['humidity']
        self.__convertTemperature()

    
    def __convertTemperature(self):
        temperature_list = [self.temp, self.feels_like, self.temp_min, self.temp_max]
        temperature_list = [round(x-273.15,3) for x in temperature_list]
        self.temp, self.feels_like, self.temp_min, self.temp_max = temperature_list
        # print(temperature_list)


if __name__ == "main":
    pass