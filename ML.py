import pandas as pd
import numpy as np
import sklearn

weather = pd.read_csv('data/NOAA_Hourly_Weather_Data_by_Station__Virginia_.csv')
weather = weather.drop(columns = ["Station", "ICAO", "ReportType", "Source", "SkyConditions", "Visibility", "VisibilityIndicator", "PresentWeatherType", "DryBulbTemperature", "DryBulbTemperatureIndicator", "WetBulbTemperature", "WetBulbTemperatureNumber", "WetBulbTemperatureIndicator", "DewPointTemperature", "DewPointTemperatureIndicator", "RelativeHumidity", "RelativeHumidityIndicator", "WindDirectionIndicator", "WindSpeed", "WindSpeedIndicator", "WindGustSpeed", "WindGustSpeedNumber", "WindGustSpeedIndicator", "StationPressure", "StationPressureIndicator", "PressureTendency", "PressureChange", "SeaLevelPressure", "SeaLevelPressureNumber", "SeaLevelPressureIndicator", "Precipitation", "PrecipitationNumber", "PrecipitationIndicator", "AltimeterSetting", "AltimeterSettingNumber", "AltimeterSettingIndicator", "RowIdentifier", "GeocodedLocation"])
print(weather.info())