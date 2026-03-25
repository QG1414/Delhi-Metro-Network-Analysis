import webbrowser
from pathlib import Path
from typing import final

import pandas as pd
from folium import Map
from plotly.graph_objects import Figure

from ..Helpers import resource_path


class BaseVisual:

    __visualPath: Path = Path("Output")
    _metro_data: pd.DataFrame
    _fig: Figure
    _map: Map

    def __init__(self, metro_data: pd.DataFrame, sub_path: Path | str) -> None:
        self._metro_data = metro_data

        if sub_path is not None:
            self.__visualPath = self.__visualPath / sub_path

    def create_visuals(self) -> None:
        if hasattr(self, "_fig"):
            self._fig.write_html(resource_path(self.__visualPath))
        elif hasattr(self, "_map"):
            self._map.save(resource_path(self.__visualPath))

    @final
    def display_visual(self) -> None:
        if self.output_file_exits():
            webbrowser.open(str(resource_path(self.__visualPath)), 2)

    @final
    def output_file_exits(self) -> bool:
        return resource_path(self.__visualPath).exists()
