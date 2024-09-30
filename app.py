from flask import Flask, jsonify, request
from shapely.geometry import shape, Point
import json

app = Flask(__name__)

# Load the GeoJSON boundary file
with open('boundary.json') as f:
    boundary_data = json.load(f)

# Since your GeoJSON contains a single Feature, we directly extract the geometry
boundary_shape = shape(boundary_data['geometry'])

@app.route('/check_point', methods=['GET'])
def check_point():
    # Get lat and long from query parameters
    lat = float(request.args.get('lat'))
    lon = float(request.args.get('lon'))
    
    # Create a point from the given latitude and longitude
    point = Point(lon, lat)
    
    # Check if the point is within the boundary
    if boundary_shape.contains(point):
        return jsonify({"status": "inside"})
    else:
        return jsonify({"status": "outside"})

if __name__ == '__main__':
    app.run(debug=True)

# http://127.0.0.1:5000/check_point?lat=23.78422245591749&lon=90.41522262031697
# 23.989142971970015, 90.51896589631149
# 23.78422245591749, 90.41522262031697