import { useEffect, useState } from 'react';
import { analyticsClient } from '../api/client';
import { FlightKpi } from '../types';
import { KpiChart } from './KpiChart';

export function FlightDashboard() {
  const [kpis, setKpis] = useState<FlightKpi[]>([]);
  const [query, setQuery] = useState('');

  useEffect(() => {
    analyticsClient.get('/analytics').then((res) => setKpis(res.data));
  }, []);

  const filtered = query
    ? kpis.filter((item) => item.flightNumber.includes(query) || item.routeKey.includes(query))
    : kpis;

  return (
    <div>
      <h1>AeroStream Dashboard</h1>
      <input placeholder="Search by flight or airport" value={query} onChange={(e) => setQuery(e.target.value)} />
      <KpiChart data={filtered} />
      <table>
        <thead><tr><th>Flight</th><th>Route</th><th>Delay</th><th>Status</th></tr></thead>
        <tbody>
          {filtered.map((kpi) => (
            <tr key={`${kpi.flightNumber}-${kpi.id}`}><td>{kpi.flightNumber}</td><td>{kpi.routeKey}</td><td>{kpi.delayMinutes}</td><td>{kpi.status}</td></tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
