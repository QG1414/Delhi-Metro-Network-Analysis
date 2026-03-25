from typing import override

import plotly.express as px
from pandas import DataFrame, Series

from ..BaseVisualGen import BaseVisual


class StationsOpenedDataChart(BaseVisual):

    def __init__(self, metro_data):
        super().__init__(metro_data, "stationsOpened.html")

    @override
    def create_visuals(self) -> None:
        self._metro_data["Opening Year"] = self._metro_data["Opening Date"].dt.year
        stations_per_year_series: Series[int] = (
            self._metro_data["Opening Year"].value_counts().sort_index()
        )
        stations_per_year_df: DataFrame = stations_per_year_series.reset_index()
        stations_per_year_df.columns = ["Year", "Number of Stations"]

        self._fig = px.bar(
            stations_per_year_df,
            x="Year",
            y="Number of Stations",
            title="Number of metro stations opened each year in delhi",
            labels={"Year": "Year", "Number of Stations": "Number of Stations Opened"},
        )

        self._fig.update_layout(
            xaxis_tickangle=-45,
            xaxis=dict(tickmode="linear"),
            yaxis=dict(title="Number of Stations Opened"),
            xaxis_title="Year",
        )

        self._fig.update_traces(
            marker_color="#8ed9ed",
        )

        super().create_visuals()
