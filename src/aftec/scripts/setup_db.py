#!/usr/bin/env python3
"""Initialize the SQLite database for AFTEC.

Creates tables and indexes for storing soil samples.
Can optionally populate with mock data for testing.
"""

import sqlite3
import sys
from pathlib import Path
from datetime import datetime, timedelta
import random

# Add project root to path (for standalone execution)
sys.path.insert(0, str(Path(__file__).parent.parent))
from src.aftec.core.models import SoilSample

DB_PATH = Path(__file__).parent.parent / "aftec.db"

def get_connection():
    """Return a connection to the SQLite database."""
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row  # access columns by name
    return conn

def create_tables():
    """Create the soil_samples table if it doesn't exist."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS soil_samples (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor_id TEXT NOT NULL,
            temperature_c REAL NOT NULL,
            ph REAL NOT NULL,
            timestamp TEXT NOT NULL,
            is_anomaly INTEGER DEFAULT 0
        )
    """)
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_timestamp 
        ON soil_samples(timestamp DESC)
    """)
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_sensor_id 
        ON soil_samples(sensor_id)
    """)
    conn.commit()
    conn.close()
    print("✓ Tables created/indexed.")

def drop_tables():
    """Drop all tables (caution: deletes all data)."""
    confirm = input("⚠️  This will delete ALL data. Type 'yes' to continue: ")
    if confirm.lower() != 'yes':
        print("Aborted.")
        return
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS soil_samples")
    conn.commit()
    conn.close()
    print("✓ Tables dropped.")

def insert_mock_data(num_samples=100):
    """Insert random realistic samples for the last N hours."""
    conn = get_connection()
    cursor = conn.cursor()
    now = datetime.now()
    for i in range(num_samples):
        # simulate time going backwards
        timestamp = now - timedelta(minutes=i * 5)
        sample = SoilSample(
            sensor_id="mock_sensor_01",
            temperature_c=round(random.uniform(15, 30), 1),
            ph=round(random.uniform(6.0, 7.5), 1),
            timestamp=timestamp
        )
        cursor.execute("""
            INSERT INTO soil_samples (sensor_id, temperature_c, ph, timestamp, is_anomaly)
            VALUES (?, ?, ?, ?, ?)
        """, (sample.sensor_id, sample.temperature_c, sample.ph, 
              sample.timestamp.isoformat(), 0))
    conn.commit()
    conn.close()
    print(f"✓ Inserted {num_samples} mock samples.")

def show_stats():
    """Print basic statistics from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) as total FROM soil_samples")
    total = cursor.fetchone()["total"]
    cursor.execute("SELECT MIN(timestamp) as oldest, MAX(timestamp) as newest FROM soil_samples")
    row = cursor.fetchone()
    oldest = row["oldest"]
    newest = row["newest"]
    print(f"Total samples: {total}")
    print(f"Date range: {oldest} → {newest}")
    conn.close()

def main():
    import argparse
    parser = argparse.ArgumentParser(description="AFTEC database setup tool")
    parser.add_argument("--drop", action="store_true", help="Drop existing tables")
    parser.add_argument("--mock", type=int, nargs="?", const=100, 
                        help="Insert mock data (optional number of samples, default 100)")
    parser.add_argument("--stats", action="store_true", help="Show database statistics")
    args = parser.parse_args()

    if args.drop:
        drop_tables()
    else:
        create_tables()

    if args.mock:
        insert_mock_data(args.mock)

    if args.stats:
        show_stats()

    if not any([args.drop, args.mock, args.stats]):
        # default behaviour: just ensure tables exist and print stats
        create_tables()
        show_stats()

if __name__ == "__main__":
    main()
