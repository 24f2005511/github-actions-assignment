from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import numpy as np
import json

app = FastAPI()

# Enable CORS for POST from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.options("/api/latency")
async def options_handler():
    return Response(status_code=200)

TELEMETRY_DATA = json.loads("""
[
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 160.1,
    "uptime_pct": 98.362,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 226.89,
    "uptime_pct": 99.002,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 121.57,
    "uptime_pct": 98.447,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 151.12,
    "uptime_pct": 99.405,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 219.55,
    "uptime_pct": 98.097,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 120.73,
    "uptime_pct": 98.844,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 168.11,
    "uptime_pct": 97.316,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 135.55,
    "uptime_pct": 97.329,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 176.56,
    "uptime_pct": 98.586,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 126.94,
    "uptime_pct": 98.023,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 123.67,
    "uptime_pct": 98.794,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 165.5,
    "uptime_pct": 98.495,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 197.75,
    "uptime_pct": 98.918,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 164.06,
    "uptime_pct": 97.437,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 169.16,
    "uptime_pct": 97.497,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 216.74,
    "uptime_pct": 98.515,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 216.3,
    "uptime_pct": 97.826,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 152.23,
    "uptime_pct": 97.536,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 187.11,
    "uptime_pct": 97.977,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 109.58,
    "uptime_pct": 97.779,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 201.24,
    "uptime_pct": 98.65,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 234.12,
    "uptime_pct": 97.744,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 134.82,
    "uptime_pct": 98.281,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 208.89,
    "uptime_pct": 99.438,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 220.71,
    "uptime_pct": 97.398,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 157.66,
    "uptime_pct": 97.21,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 132.62,
    "uptime_pct": 98.82,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 203.27,
    "uptime_pct": 97.225,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 208.45,
    "uptime_pct": 99.464,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 186.97,
    "uptime_pct": 98.709,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 177,
    "uptime_pct": 97.5,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 142.19,
    "uptime_pct": 98.516,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 118.25,
    "uptime_pct": 98.206,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 133.09,
    "uptime_pct": 99.241,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 214.62,
    "uptime_pct": 97.794,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 223.14,
    "uptime_pct": 98.682,
    "timestamp": 20250312
  }
]
""")

@app.post("/api/latency")
async def latency_analytics(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 180)

    results = []
    for region in regions:
        records   = [r for r in TELEMETRY_DATA if r["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes   = [r["uptime_pct"]  for r in records]
        results.append({
            "region":      region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime":  round(float(np.mean(uptimes)), 3),
            "breaches":    int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}
