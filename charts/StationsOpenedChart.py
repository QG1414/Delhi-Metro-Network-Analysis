import pandas as pd
import plotly.express as px

class StationsOpenedDataChart:
    def __init__(self, metro_data : pd.DataFrame) -> None:
        self.__create_usable_data(metro_data)

    def __create_usable_data(self, metro_data : pd.DataFrame) -> None:

        metro_data["Opening Year"] = metro_data["Opening Date"].dt.year
        stations_per_year = metro_data["Opening Year"].value_counts().sort_index()
        self.__stations_per_year_df = stations_per_year.reset_index()
        self.__stations_per_year_df.columns = ["Year", "Number of Stations"]

    def display_chart(self):
        fig = px.bar(self.__stations_per_year_df, x = "Year", y = "Number of Stations",
                    title="Number of metro stations opened each year in delhi",
                    labels={"Year":"Year","Number of Stations" : "Number of Stations Opened"})

        fig.update_layout(xaxis_tickangle=-45, xaxis=dict(tickmode="linear"),
                        yaxis=dict(title="Number of Stations Opened"),
                        xaxis_title="Year")

        fig.update_traces(marker_color="#8ed9ed",)

        fig.show()