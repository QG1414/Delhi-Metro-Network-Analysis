import folium
import pandas as pd

class MapGeneration:
    
    def __init__(self, metro_data : pd.DataFrame) -> None:
        self.__metro_data = metro_data
        self.__line_color = {
            "Red line" : "red",
            "Blue line" : "blue",
            "Yellow line" : "beige",
            "Green line" : "green",
            "Voilet line" : "purple",
            "Pink line" : "pink",
            "Magenta line" : "darkred",
            "Orange line" : "orange",
            "Rapid Metro" : "cadetblue",
            "Aqua line" : "black",
            "Green line branch" : "lightgreen",
            "Blue line branch" : "lightblue",
            "Gray line" : "lightgray",
        }

    def generate_map(self):
        delhiMap = folium.Map(location=[28.7041, 77.1025], zoom_start=11)

        for _,row in self.__metro_data.iterrows():
            line = row["Line"]
            color = self.__line_color.get(line, "black")
            folium.Marker(
                location=[row["Latitude"], row["Longitude"]],
                popup=f"{row["Station Name"]}",
                tooltip=f"{row["Station Name"]}, {line}",
                icon = folium.Icon(color=color)
            ).add_to(delhiMap)

        delhiMap.show_in_browser()


