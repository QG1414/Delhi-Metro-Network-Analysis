from typing import override

import plotly.express as px

from ..BaseVisualGen import BaseVisual


class StationsTypesDataChart(BaseVisual):
    def __init__(self, metro_data):
        super().__init__(metro_data, "stationTypes.html")

    @override
    def create_visuals(self) -> None:
        stations_types_count = self._metro_data["Station Layout"].value_counts()

        self._fig = px.bar(
            x=stations_types_count.index,
            y=stations_types_count.values,
            labels={"x": "Station Layout", "y": "Number of Stations"},
            title="Distribution of Delhi Metro Station Layouts",
            color=stations_types_count.index,
            color_continuous_scale="pastel",
        )

        self._fig.update_layout(
            xaxis_title="Station Layout",
            yaxis_title="Number of Stations",
            coloraxis_showscale=False,
            template="plotly_white",
        )

        super().create_visuals()
