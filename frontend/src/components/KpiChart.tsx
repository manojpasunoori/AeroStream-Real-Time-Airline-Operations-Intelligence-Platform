import { LineChart, Line, XAxis, YAxis, Tooltip } from 'recharts';
import { FlightKpi } from '../types';

export function KpiChart({ data }: { data: FlightKpi[] }) {
  return (
    <LineChart width={700} height={300} data={data}>
      <XAxis dataKey="flightNumber" />
      <YAxis />
      <Tooltip />
      <Line type="monotone" dataKey="reliabilityScore" stroke="#2c7" />
    </LineChart>
  );
}
