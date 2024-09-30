# GeoJSON Boundary Checker

A Python Flask application that checks whether a given latitude/longitude point is inside or outside a boundary defined in a GeoJSON file. This project is designed to handle various types of geographical boundaries (such as `Polygon` and `MultiPolygon`) and can be easily integrated into web-based applications for spatial queries.

## Features
- **Boundary-based Point Checking**: Determine if a point (latitude, longitude) is inside or outside a geographical boundary.
- **Supports GeoJSON**: Load boundaries from standard GeoJSON files, including `Polygon` and `MultiPolygon` geometries.
- **Flask-based API**: Simple web-based API that can be integrated with other systems or used for testing.
- **Dynamic Map View**: Automatically adjusts the map view to fit the boundary.

## Dependencies

You will need the following Python libraries for this project:

- **Flask**: A lightweight WSGI web application framework.
- **Shapely**: A library for geometric objects and operations.
- **GeoJSON**: A Python library for handling GeoJSON data.

You can install them using `pip`:

```bash
pip install Flask shapely geojson
```

## Usage
Checking if a Point is Inside the Boundary
To check whether a specific point is inside or outside the boundary, you can send a GET request to the /check_point endpoint with the latitude (lat) and longitude (lon) as query parameters.

Example:

```bash
http://127.0.0.1:5000/check_point?lat=23.8103&lon=90.4125
```

Response:
If the point is inside the boundary, you will get the following response:

```bash
{
    "status": "inside"
}
```

If the point is outside the boundary:

```bash
{
    "status": "outside"
}
```

Displaying the Boundary on a Map
To visualize the boundary on a map, navigate to the root URL of the Flask app (http://127.0.0.1:5000/). The map will automatically adjust to fit the boundary defined in the boundary.json file.

## Folder Structure
bash
Copy code
geojson-boundary-checker/
│
├── app.py               # Main Flask application
├── boundary.json        # GeoJSON file containing the boundary (you must add this file)
├── templates/           # HTML templates for map rendering
│   └── index.html       # Map view showing boundary data
├── static/              # Static files like CSS and JS
└── README.md            # Documentation for the project

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributions
Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

## Author
Zahidul Ripon