import pandas as pd
from maps.DelhiMap import MapGeneration
from charts.StationsOpenedChart import StationsOpenedDataChart
from charts.StationsLengthChart import StationsLengthDataChart
from charts.StationsTypesChart import StationsTypesDataChart

def main():
    metro_data = pd.read_csv("Delhi-Metro-Network_Data.csv")
    missing_values = metro_data.isnull().sum()

    if missing_values.sum() > 0:
        print("Some values are missing !!!")

    metro_data["Opening Date"] = pd.to_datetime(metro_data["Opening Date"])

    #Making chart with how many stations were opened each year
    stations_opened_data = StationsOpenedDataChart(metro_data)
    stations_opened_data.display_chart()

    #Making chart to see length of each station
    stations_length_data = StationsLengthDataChart(metro_data)
    stations_length_data.display_chart()

    #Visualization of station types
    stations_types_data = StationsTypesDataChart(metro_data)
    stations_types_data.display_chart()

    #Visualization of stations on map
    map_data = MapGeneration(metro_data)
    map_data.generate_map()

if __name__ == "__main__":
    main()