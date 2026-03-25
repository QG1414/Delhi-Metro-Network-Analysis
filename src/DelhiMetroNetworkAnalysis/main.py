from pathlib import Path

import pandas as pd

from .Helpers import resource_path
from .Visuals import (
    BaseVisual,
    MapGeneration,
    StationsLengthDataChart,
    StationsOpenedDataChart,
    StationsTypesDataChart,
)


def main():
    metro_data = pd.read_csv(resource_path(Path("Data/Delhi-Metro-Network_Data.csv")))
    metro_data["Opening Date"] = pd.to_datetime(metro_data["Opening Date"])

    visuals: tuple[BaseVisual] = (
        MapGeneration(metro_data),
        StationsOpenedDataChart(metro_data),
        StationsLengthDataChart(metro_data),
        StationsTypesDataChart(metro_data),
    )

    for visual in visuals:
        create_and_display(visual)


def create_and_display(baseData: BaseVisual):
    if not baseData.output_file_exits():
        baseData.create_visuals()
    baseData.display_visual()


if __name__ == "__main__":
    main()
