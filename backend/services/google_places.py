import os
import requests
from dotenv import load_dotenv

load_dotenv()
    
def get_nearby_restaurants(lat, long, radius):
    """
    Get nearby restaurants using Google Places API.
    
    Args:
        lat (float): Latitude
        long (float): Longitude
        radius (int): Search radius in meters
    
    Returns:
        list: List of restaurant objects from Google Places
    """
    api_key = os.getenv('GOOGLE_PLACES_API_KEY')
    
    if not api_key:
        raise ValueError('GOOGLE_PLACES_API_KEY not found in environment variables')
    
    # Google Places API Nearby Search endpoint
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    
    params = {
        'location': f'{lat},{long}',
        'radius': radius,
        'type': 'restaurant',
        'key': api_key
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        if data.get('status') != 'OK':
            print(f"Google Places API returned status: {data.get('status')}")
            print(f"Error message: {data.get('error_message', 'No error message provided')}")
            return []
        
        restaurants = data.get('results', [])
        return restaurants
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching from Google Places API: {e}")
        return []

