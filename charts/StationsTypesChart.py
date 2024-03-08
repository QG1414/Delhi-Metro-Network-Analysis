import pandas as pd
import plotly.express as px

class StationsTypesDataChart:
    def __init__(self, metro_data : pd.DataFrame) -> None:
        self.__create_usable_data(metro_data)

    def __create_usable_data(self, metro_data : pd.DataFrame) -> None:
        self.__stations_types_count = metro_data["Station Layout"].value_counts()

    def display_chart(self):
        fig = px.bar(x=self.__stations_types_count.index, y=self.__stations_types_count.values,
             labels = {"x":"Station Layout", "y":"Number of Stations"},
             title="Distribution of Delhi Metro Station Layouts",
             color=self.__stations_types_count.index,
             color_continuous_scale = "pastel")

        fig.update_layout(xaxis_title = "Station Layout",
                yaxis_title = "Number of Stations",
                  coloraxis_showscale=False,
                  template="plotly_white")

        fig.show()



