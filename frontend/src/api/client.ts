import axios from 'axios';

export const analyticsClient = axios.create({
  baseURL: import.meta.env.VITE_ANALYTICS_API ?? 'http://localhost:8080/api/v1',
});
