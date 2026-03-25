from typing import override

import folium
import pandas as pd

from ..BaseVisualGen import BaseVisual


class MapGeneration(BaseVisual):

    __line_color = {
        "Red line": "red",
        "Blue line": "blue",
        "Yellow line": "beige",
        "Green line": "green",
        "Voilet line": "purple",
        "Pink line": "pink",
        "Magenta line": "darkred",
        "Orange line": "orange",
        "Rapid Metro": "cadetblue",
        "Aqua line": "black",
        "Green line branch": "lightgreen",
        "Blue line branch": "lightblue",
        "Gray line": "lightgray",
    }

    def __init__(self, metro_data: pd.DataFrame) -> None:
        super().__init__(metro_data, "delhiMap.html")

    @override
    def create_visuals(self) -> None:
        self._map = folium.Map(location=[28.7041, 77.1025], zoom_start=11)

        for _, row in self._metro_data.iterrows():
            line = row["Line"]
            color = self.__line_color.get(line, "black")
            folium.Marker(
                location=[row["Latitude"], row["Longitude"]],
                popup=f"{row["Station Name"]}",
                tooltip=f"{row["Station Name"]}, {line}",
                icon=folium.Icon(color=color),
            ).add_to(self._map)

        super().create_visuals()
