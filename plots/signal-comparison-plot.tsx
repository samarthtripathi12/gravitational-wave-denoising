import React, { useEffect, useRef } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const SignalPlot = () => {
  // Generate signals
  const generateSignals = (length = 1000, noiseLevel = 0.3, seed = 42) => {
    // Simple seeded random number generator
    let randomSeed = seed;
    const seededRandom = () => {
      randomSeed = (randomSeed * 9301 + 49297) % 233280;
      return randomSeed / 233280;
    };
    
    // Box-Muller transform for Gaussian random numbers
    const gaussianRandom = (mean = 0, stdev = 1) => {
      const u = 1 - seededRandom();
      const v = seededRandom();
      const z = Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
      return z * stdev + mean;
    };
    
    const data = [];
    for (let i = 0; i < length; i++) {
      const t = (i / (length - 1)) * 4 * Math.PI;
      const clean = Math.sin(t);
      const noise = gaussianRandom(0, noiseLevel);
      const noisy = clean + noise;
      
      data.push({
        time: i,
        Clean: clean,
        Noisy: noisy
      });
    }
    
    return data;
  };
  
  const data = generateSignals();
  
  return (
    <div className="w-full h-screen flex items-center justify-center bg-gray-50 p-8">
      <div className="w-full max-w-6xl bg-white rounded-lg shadow-lg p-6">
        <h2 className="text-2xl font-bold text-center mb-6 text-gray-800">
          Clean vs Noisy Signal
        </h2>
        <ResponsiveContainer width="100%" height={500}>
          <LineChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
            <CartesianGrid strokeDasharray="3 3" stroke="#e0e0e0" />
            <XAxis 
              dataKey="time" 
              label={{ value: 'Time', position: 'insideBottom', offset: -5 }}
              stroke="#666"
            />
            <YAxis 
              label={{ value: 'Amplitude', angle: -90, position: 'insideLeft' }}
              stroke="#666"
              domain={[-2, 2]}
            />
            <Tooltip 
              contentStyle={{ backgroundColor: 'rgba(255, 255, 255, 0.95)', border: '1px solid #ccc' }}
              formatter={(value) => value.toFixed(3)}
            />
            <Legend 
              wrapperStyle={{ paddingTop: '20px' }}
              iconType="line"
            />
            <Line 
              type="monotone" 
              dataKey="Clean" 
              stroke="#2563eb" 
              strokeWidth={2}
              dot={false}
              name="Clean"
            />
            <Line 
              type="monotone" 
              dataKey="Noisy" 
              stroke="#dc2626" 
              strokeWidth={1.5}
              dot={false}
              name="Noisy"
            />
          </LineChart>
        </ResponsiveContainer>
        <div className="mt-4 text-sm text-gray-600 text-center">
          <p>Blue line: Clean sine wave signal | Red line: Noisy signal (Gaussian noise, σ = 0.3)</p>
        </div>
      </div>
    </div>
  );
};

export default SignalPlot;