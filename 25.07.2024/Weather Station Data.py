#Scenario:
#You are working on a weather station data analysis project. 
#Each record contains temperature, humidity, and wind speed.
#Implement a function to find the average temperature.

#Code:
class WeatherRecord:
    def __init__(self, temperature, humidity, wind_speed):
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed

def average_temperature(records):
    total_temp = sum(record.temperature for record in records)
    return total_temp / len(records)

records = [WeatherRecord(30, 65, 10), WeatherRecord(25, 70, 12)]
print(average_temperature(records))  
