import pandas as pd
from maps.DelhiMap import MapGeneration
from charts.StationsOpenedChart import StationsOpenedDataChart
from charts.StationsLengthChart import StationsLengthDataChart
from charts.StationsTypesChart import StationsTypesDataChart
import sys
import os
import time

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def main():
    metro_data = pd.read_csv(resource_path("Delhi-Metro-Network_Data.csv"))
    metro_data["Opening Date"] = pd.to_datetime(metro_data["Opening Date"])
    # missing_values = metro_data.isnull().sum()

    # if missing_values.sum() > 0:
    #     print("Some values are missing !!!")

    #Visualization of stations on map
    map_data = MapGeneration(metro_data)
    map_data.generate_map()

    #Making chart with how many stations were opened each year
    stations_opened_data = StationsOpenedDataChart(metro_data)
    stations_opened_data.display_chart()

    #Making chart to see length of each station
    stations_length_data = StationsLengthDataChart(metro_data)
    stations_length_data.display_chart()

    #Visualization of station types
    stations_types_data = StationsTypesDataChart(metro_data)
    stations_types_data.display_chart()



def create_data():
    metro_data = pd.read_csv(resource_path("Delhi-Metro-Network_Data.csv"))
    metro_data["Opening Date"] = pd.to_datetime(metro_data["Opening Date"])

    map_data = MapGeneration(metro_data)
    map_data.generate_map_file()

if __name__ == "__main__":
    main()
    #create_data() Debug only to generate necessary files