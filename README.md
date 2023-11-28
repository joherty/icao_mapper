# Airport Route Plotter

This Python script reads airport data from a CSV file and plots a route on a map using the Folium library. The route is specified by a list of ICAO codes provided in a text file.

## Prerequisites

- Python 3
- `pip` (Python package installer)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/airport-route-plotter.git
    ```

2. Navigate to the project directory:

    ```bash
    cd airport-route-plotter
    ```

3. Install required dependencies:

    ```bash
    pip install folium
    ```

## Usage

### 1. Prepare Data

- Use the included (`airports.csv`) containing airport data. The CSV file should have the following columns: `ident`, `latitude_deg`, and `longitude_deg`.  

- Updated file available at https://ourairports.com/data/

    Example CSV format:

    ```csv
    "id","ident","type","name","latitude_deg","longitude_deg","elevation_ft","continent","iso_country","iso_region","municipality","scheduled_service","gps_code","iata_code","local_code","home_link","wikipedia_link","keywords"
    6523,"00A","heliport","Total RF Heliport",40.070985,-74.933689,11,"NA","US","US-PA","Bensalem","no","K00A",,"00A","https://www.penndot.pa.gov/TravelInPA/airports-pa/Pages/Total-RF-Heliport.aspx",,
    323361,"00AA","small_airport","Aero B Ranch Airport",38.704022,-101.473911,3435,"NA","US","US-KS","Leoti","no","00AA",,"00AA",,,
    ```

- Create a text file (`current_route.txt`) containing a list of ICAO codes, with each code on a new line.

    Example text file:

    ```plaintext
    KJFK
    EGLL
    RJTT
    ZBAA
    ```

### 2. Run the Script

Run the script using the following command:

```bash
python airport_route_plotter.py
```

### 3. Output

The script will read the airport data from airports.csv and the list of ICAO codes from current_route.txt, then plot the route on a map using Folium.  
The resulting map will be saved as route_map.html in the project directory. Open this with your browser.  