import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

# Lazy initialization of Supabase client
_supabase_client = None

def get_supabase_client():
    """
    Get or create the Supabase client instance.
    Uses lazy initialization to ensure .env is loaded first.
    """
    global _supabase_client
    
    if _supabase_client is None:
        supabase_url = os.getenv('SUPABASE_URL')
        supabase_key = os.getenv('SUPABASE_KEY')
        
        if supabase_url and supabase_key:
            _supabase_client = create_client(supabase_url, supabase_key)
        else:
            print("Warning: Supabase credentials not found in environment variables")
            return None
    
    return _supabase_client

def get_restaurant_tags(restaurant_name):
    """
    Get tags for a restaurant from the database.
    
    Args:
        restaurant_name (str): Name of the restaurant
    
    Returns:
        list: List of tags, or None if restaurant not found
    """
    supabase = get_supabase_client()
    if not supabase:
        return None
    
    try:
        response = supabase.table('Restaurant').select('tags').eq('name', restaurant_name).execute()
        
        if response.data and len(response.data) > 0:
            tags = response.data[0].get('tags')
            return tags if tags else None
        
        return None
    
    except Exception as e:
        print(f"Error fetching restaurant tags from database: {e}")
        return None

def store_restaurant_tags(restaurant_name, tags):
    """
    Store restaurant and tags in the database.
    
    Args:
        restaurant_name (str): Name of the restaurant
        tags (list): List of tags
    
    Returns:
        bool: True if successful, False otherwise
    """
    supabase = get_supabase_client()
    if not supabase:
        return False
    
    try:
        # Check if restaurant already exists
        existing = supabase.table('Restaurant').select('id').eq('name', restaurant_name).execute()
        
        if existing.data and len(existing.data) > 0:
            # Update existing restaurant
            supabase.table('Restaurant').update({
                'tags': tags
            }).eq('name', restaurant_name).execute()
        else:
            # Insert new restaurant
            supabase.table('Restaurant').insert({
                'name': restaurant_name,
                'tags': tags
            }).execute()
        
        return True
    
    except Exception as e:
        print(f"Error storing restaurant tags in database: {e}")
        return False

