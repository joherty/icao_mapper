import csv
import folium

def read_airport_data(file_path):
    airport_data = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            icao_code = row['ident']
            lat = float(row['latitude_deg'])
            lon = float(row['longitude_deg'])
            airport_data[icao_code] = (lat, lon)
    return airport_data

def read_icao_codes_from_file(file_path):
    with open(file_path, 'r') as file:
        icao_codes = [line.strip() for line in file]
    return icao_codes

def plot_route(icao_codes, airport_data):
    # Initialize the map
    map_center = (0, 0)  # Set the initial map center
    map_route = folium.Map(location=map_center, zoom_start=3)

    # Plot the route waypoints
    for icao_code in icao_codes:
        if icao_code in airport_data:
            location = airport_data[icao_code]
            folium.Marker(location, popup=icao_code).add_to(map_route)

    # Draw lines between waypoints to represent the route
    folium.PolyLine(locations=[airport_data[icao_code] for icao_code in icao_codes if icao_code in airport_data], color='blue').add_to(map_route)

    # Save the map to an HTML file
    map_route.save("route_map.html")

if __name__ == "__main__":
    # Use the relative path to the CSV file
    csv_file_path = "airports.csv"

    # Use the relative path to the text file containing ICAO codes
    icao_codes_file_path = "current_route.txt"
    
    # Read ICAO codes from the text file
    icao_codes = read_icao_codes_from_file(icao_codes_file_path)

    # Read airport data from the CSV file
    airport_data = read_airport_data(csv_file_path)

    # Plot the route on the map
    plot_route(icao_codes, airport_data)
