import type { VercelRequest, VercelResponse } from '@vercel/node';
import { getRestaurants } from './_lib/controllers/restaurantController';

export default async function handler(req: VercelRequest, res: VercelResponse) {
  const lat = parseFloat(req.query.lat as string);
  const long = parseFloat(req.query.long as string);
  const radius = parseInt(req.query.radius as string) || 1500;

  if (isNaN(lat) || isNaN(long)) {
    return res.status(400).json({ error: 'Missing required parameters: lat and long' });
  }

  try {
    const result = await getRestaurants(lat, long, radius);
    res.status(200).json(result);
  } catch (e) {
    res.status(500).json({ error: (e as Error).message });
  }
}
