import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

class StationsLengthDataChart:
    def __init__(self, metro_data : pd.DataFrame) -> None:
        self.__create_usable_data(metro_data)

    def __create_usable_data(self, metro_data : pd.DataFrame) -> None:

        stations_per_line = metro_data["Line"].value_counts()
        total_distance_per_line = metro_data.groupby("Line")["Distance from Start (km)"].max()
        avg_distance_per_line = total_distance_per_line / (stations_per_line - 1)

        self.__line_analysis = pd.DataFrame({
            "Line":stations_per_line.index,
            "Number of Stations":stations_per_line.values,
            "Avarage Distance Between Stations (km)" : avg_distance_per_line
        })

        self.__line_analysis = self.__line_analysis.sort_values(by="Number of Stations", ascending=False)
        self.__line_analysis.reset_index(drop=True,inplace=True)

    def display_chart(self):

        fig = make_subplots(rows=1, cols=2, 
                            subplot_titles=("Number of Stations Per Metro Line",
                                            "Avarage Distance Beetweeen Stations Per Metro Line"),
                            horizontal_spacing=0.2)

        fig.add_trace(
            go.Bar(y=self.__line_analysis["Line"], x = self.__line_analysis["Number of Stations"], orientation="h", name = "Number of Stations", marker_color="crimson"),
            row=1, col=1
        )

        fig.add_trace(
            go.Bar(y=self.__line_analysis["Line"], x = self.__line_analysis["Avarage Distance Between Stations (km)"],
                orientation="h", name= "Avarage Distance (km)", marker_color="navy"),
            row = 1, col = 2
        )

        fig.update_xaxes(title_text = "Number of Stations", row=1, col=1,dtick=5)
        fig.update_xaxes(title_text = "Avarage Distance Between Stations (km)", row=1, col=2,dtick=0.5)

        fig.update_yaxes(title_text="Metro Line", row=1, col=1)
        fig.update_yaxes(title_text="Metro Line",row=1,col=2)

        fig.update_layout(height=600, width=1200, title_text="Metro Line Analysis", template="plotly_white")

        fig.show()