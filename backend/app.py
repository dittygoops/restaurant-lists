from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os

from controllers.restaurant_controller import get_restaurants

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/api/restaurants', methods=['GET'])
def restaurants():
    try:
        # Get query parameters
        lat = request.args.get('lat', type=float)
        long = request.args.get('long', type=float)
        radius = request.args.get('radius', type=int, default=1500)
        
        # Validate parameters
        if lat is None or long is None:
            return jsonify({'error': 'Missing required parameters: lat and long'}), 400
        
        # Get restaurants with tags
        result = get_restaurants(lat, long, radius)
        
        return jsonify(result), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)

