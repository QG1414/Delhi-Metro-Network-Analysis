from typing import override

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from ..BaseVisualGen import BaseVisual


class StationsLengthDataChart(BaseVisual):

    def __init__(self, metro_data):
        super().__init__(metro_data, "stationsLength.html")

    @override
    def create_visuals(self) -> None:
        stations_per_line = self._metro_data["Line"].value_counts()
        total_distance_per_line = self._metro_data.groupby("Line")[
            "Distance from Start (km)"
        ].max()
        avg_distance_per_line = total_distance_per_line / (stations_per_line - 1)

        line_analysis = pd.DataFrame(
            {
                "Line": stations_per_line.index,
                "Number of Stations": stations_per_line.values,
                "Avarage Distance Between Stations (km)": avg_distance_per_line,
            }
        )

        line_analysis = line_analysis.sort_values(
            by="Number of Stations", ascending=False
        )
        line_analysis.reset_index(drop=True, inplace=True)

        self._fig = make_subplots(
            rows=1,
            cols=2,
            subplot_titles=(
                "Number of Stations Per Metro Line",
                "Avarage Distance Beetweeen Stations Per Metro Line",
            ),
            horizontal_spacing=0.2,
        )

        self._fig.add_trace(
            go.Bar(
                y=line_analysis["Line"],
                x=line_analysis["Number of Stations"],
                orientation="h",
                name="Number of Stations",
                marker_color="crimson",
            ),
            row=1,
            col=1,
        )

        self._fig.add_trace(
            go.Bar(
                y=line_analysis["Line"],
                x=line_analysis["Avarage Distance Between Stations (km)"],
                orientation="h",
                name="Avarage Distance (km)",
                marker_color="navy",
            ),
            row=1,
            col=2,
        )

        self._fig.update_xaxes(title_text="Number of Stations", row=1, col=1, dtick=5)
        self._fig.update_xaxes(
            title_text="Avarage Distance Between Stations (km)", row=1, col=2, dtick=0.5
        )

        self._fig.update_yaxes(title_text="Metro Line", row=1, col=1)
        self._fig.update_yaxes(title_text="Metro Line", row=1, col=2)

        self._fig.update_layout(
            height=600,
            width=1200,
            title_text="Metro Line Analysis",
            template="plotly_white",
        )

        super().create_visuals()
