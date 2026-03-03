export type FlightKpi = {
  id?: number;
  flightNumber: string;
  routeKey: string;
  delayMinutes: number;
  status: string;
  reliabilityScore: number;
};
