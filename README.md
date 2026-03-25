# Delhi Metro Network Analysis

**Author:** Kacper Potaczała

## Basic Info

This project serves as a learning exercise and a reimplementation of an existing analysis with a modified code infrastructure, based on:
https://medium.com/@theelucidate365/delhi-metro-network-analysis-3a534b203746

## Table of Contents

* [Folders & Files](#folders--files)
* [Installation](#installation)
* [Usage](#usage)
* [Charts](#charts)

---

## Folders & Files

The project structure is organized into the following directories:

* **Data** - 
  Contains input data used for further analysis.

* **Output** - 
  Includes the compiled executable file and all HTML representations of the charts.

* **src/DelhiMetroNetworkAnalysis** - 
  Main source directory of the project.

* **src/DelhiMetroNetworkAnalysis/Helpers** - 
  Utility module for handling tasks such as file path management.

* **src/DelhiMetroNetworkAnalysis/Visuals** - 
  Modules responsible for generating HTML files and displaying maps and charts.

* **src/DelhiMetroNetworkAnalysis/Visuals/ChartsGeneration** - 
  Modules dedicated to generating charts based on Delhi metro data.

* **src/DelhiMetroNetworkAnalysis/Visuals/MapsGeneration** - 
  Module focused on creating map visualizations.

---

## Installation

Clone the repository:

```
git clone https://github.com/QG1414/Delhi-Metro-Network-Analysis.git
```

Create and activate a virtual environment:

```
python -m venv .venv
.\.venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Usage

Make sure your working directory is set to `src`.

To start the application, run the following command while the virtual environment is active:

```
python -m DelhiMetroNetworkAnalysis.main
```

After launching, four subpages will automatically open in your default browser, each displaying different maps or charts.

---

## Charts

The project is based on data collected from Delhi metro stations.

It includes one map and four charts representing various aspects of the dataset:

* **Map**
  Displays station locations on an interactive map, with colors indicating different metro lines.

* **Histogram (by year)**
  Shows the number of new stations opened each year.

* **Two horizontal histograms**
  Represent the number of stations and the total length of each metro line.

* **Histogram (by station layout)**
  Illustrates the number of stations by station layout (elevated, underground, or at-grade).
