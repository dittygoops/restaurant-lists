# Restaurant Lists Backend

A Flask API that fetches nearby restaurants using Google Places API, generates tags using Groq AI, and stores data in Supabase.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables in `.env`:
   - `GOOGLE_PLACES_API_KEY`: Your Google Places API key
   - `SUPABASE_URL`: Your Supabase project URL
   - `SUPABASE_KEY`: Your Supabase anon/public key
   - `GROQ_API_KEY`: Your Groq API key (using free tier model: llama-3.3-70b-versatile)

3. Run the application:
```bash
python app.py
```

The server will start on `http://localhost:5000`

## API Endpoints

### GET /api/restaurants

Get nearby restaurants with AI-generated tags.

**Query Parameters:**
- `lat` (required): Latitude
- `long` (required): Longitude
- `radius` (optional): Search radius in meters (default: 1500)

**Example:**
```
GET http://localhost:5000/api/restaurants?lat=37.7749&long=-122.4194&radius=1000
```

**Response:**
```json
[
  {
    "name": "Restaurant Name",
    "place_id": "ChIJxxxx",
    "address": "123 Main St",
    "location": {
      "lat": 37.7749,
      "lng": -122.4194
    },
    "rating": 4.5,
    "user_ratings_total": 234,
    "tags": ["italian", "fine dining", "romantic"]
  }
]
```

### GET /api/health

Health check endpoint.

## Project Structure

```
backend/
├── app.py                          # Main Flask application
├── controllers/
│   └── restaurant_controller.py   # Business logic for restaurants
├── services/
│   ├── google_places.py           # Google Places API integration
│   ├── database.py                # Supabase database operations
│   └── groq_api.py                # Groq AI integration
├── .env                           # Environment variables
├── .gitignore                     # Git ignore rules
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## How It Works

1. Client requests restaurants near a specific location
2. Backend fetches nearby restaurants from Google Places API
3. For each restaurant:
   - Check if tags exist in Supabase database
   - If not, generate tags using Groq AI (llama-3.3-70b-versatile)
   - Store restaurant and tags in database for future use
4. Return complete list with tags to client

## Database Schema

**Table: Restaurant**
- `id` (int8): Primary key
- `name` (text): Restaurant name
- `tags` (text[]): Array of descriptive tags

