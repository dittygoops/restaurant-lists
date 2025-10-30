from services.google_places import get_nearby_restaurants
from services.database import get_restaurant_tags, store_restaurant_tags
from services.groq_api import generate_restaurant_tags

def get_restaurants(lat, long, radius):
    """
    Main controller function to get restaurants with tags.
    
    Args:
        lat (float): Latitude
        long (float): Longitude
        radius (int): Search radius in meters
    
    Returns:
        list: List of restaurant objects with tags
    """
    result = []
    
    # Get nearby restaurants from Google Places API
    restaurants = get_nearby_restaurants(lat, long, radius)
    
    # Process each restaurant
    for restaurant in restaurants:
        restaurant_name = restaurant.get('name')
        
        # Try to get tags from database
        tags = get_restaurant_tags(restaurant_name)
        
        # If tags don't exist, generate them using Groq
        if not tags:
            # Generate tags using AI
            tags = generate_restaurant_tags(restaurant)
            
            # Store the restaurant and tags in database
            store_restaurant_tags(restaurant_name, tags)
        
        # Extract location data
        location = restaurant.get('geometry', {}).get('location', {})
        
        # Add restaurant with tags to result
        restaurant_data = {
            'name': restaurant_name,
            'place_id': restaurant.get('place_id'),
            'address': restaurant.get('vicinity'),
            'lat': location.get('lat'),
            'long': location.get('lng'),  # Google Places API uses 'lng', we map it to 'long'
            'rating': restaurant.get('rating'),
            'user_ratings_total': restaurant.get('user_ratings_total'),
            'tags': tags
        }
        
        result.append(restaurant_data)
    
    return result

