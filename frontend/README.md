# Restaurant Finder Frontend

A modern React + TypeScript frontend for finding and filtering restaurants by location and tags.

## Features

- 🗺️ **Map Placeholder**: Visual interface for location selection (placeholder for future map integration)
- 🔍 **Location Search**: Search for restaurants by latitude, longitude, and radius
- 🏷️ **Tag-Based Filtering**: Click on restaurant tags to dynamically filter results
- ✨ **Beautiful UI**: Modern, responsive design with smooth animations
- 🎨 **Dark Mode Support**: Automatically adapts to system color scheme
- ⚡ **Fast & Responsive**: Built with Vite for optimal performance

## Getting Started

### Prerequisites

- Node.js (v18 or higher recommended)
- npm or yarn
- Backend server running on `http://localhost:5001`

### Installation

```bash
# Install dependencies
npm install
```

### Running the Application

```bash
# Start development server
npm run dev
```

The application will be available at `http://localhost:5173` (or another port if 5173 is in use).

### Building for Production

```bash
# Build the application
npm run build

# Preview the production build
npm run preview
```

## How to Use

1. **Enter Coordinates**: 
   - Input latitude and longitude values
   - Set the search radius in meters
   - Default values are provided for San Francisco

2. **Search**: 
   - Click the "🔍 Search" button to fetch restaurants
   - A beautiful loading animation will appear while fetching

3. **Filter by Tags**:
   - Each restaurant displays tags as colorful badges
   - Click any tag to exclude restaurants with that tag
   - Excluded tags appear at the top with a red background
   - Click an excluded tag to re-include those restaurants

4. **View Results**:
   - Restaurant cards display name, coordinates, and tags
   - Hover over cards for a subtle lift effect
   - The counter shows how many restaurants are currently visible

## Technology Stack

- **React 19**: Latest React with hooks
- **TypeScript**: Type-safe development
- **Vite**: Fast build tool and dev server
- **CSS3**: Modern styling with animations
- **Fetch API**: For backend communication

## Project Structure

```
frontend/
├── src/
│   ├── App.tsx          # Main application component
│   ├── App.css          # Application styles
│   ├── types.ts         # TypeScript type definitions
│   ├── main.tsx         # Application entry point
│   └── index.css        # Global styles
├── public/              # Static assets
├── package.json         # Dependencies and scripts
└── vite.config.ts       # Vite configuration
```

## API Integration

The frontend connects to the backend API at:
- **Endpoint**: `http://localhost:5001/api/restaurants`
- **Method**: GET
- **Query Parameters**:
  - `lat` (required): Latitude
  - `long` (required): Longitude
  - `radius` (optional): Search radius in meters (default: 1500)

**Response Format**:
```typescript
Restaurant[] where Restaurant = {
  name: string;
  tags: string[];
  lat: number;
  long: number;
}
```

## Future Enhancements

- 🗺️ Interactive map integration (Google Maps, Mapbox, etc.)
- 📍 Click-to-select location on map
- 🎯 Geolocation support (use current location)
- 💾 Save favorite restaurants
- 🔗 Share search results via URL
- 📱 Progressive Web App (PWA) support

## Development

### Linting

```bash
npm run lint
```

### Type Checking

TypeScript will automatically check types during development. The build process will fail if there are type errors.

## License

This project is part of the restaurant-lists application.
