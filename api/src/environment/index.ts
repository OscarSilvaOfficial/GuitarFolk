import { config } from 'dotenv';

config();

export const ENVIRONMENT = {
  MONGO_URL: process.env.MONGO_URL,
};
