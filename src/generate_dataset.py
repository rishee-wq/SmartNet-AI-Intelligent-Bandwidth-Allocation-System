"""
SmartNet AI — Synthetic Network Traffic Dataset Generator

Generates realistic network traffic data with labeled priority classes
for training the Decision Tree bandwidth allocation model.

Author : SmartNet AI Team
Date   : March 2026
"""

import os
import numpy as np
import pandas as pd

# Reproducibility
np.random.seed(42)


def generate_dataset(output_path=None, n_samples=10000):
    """
    Generate a synthetic network traffic dataset.

    Traffic classes:
        0 = Critical  (VoIP, emergency)     — 15%
        1 = High      (video, ERP)          — 25%
        2 = Medium    (web, email)           — 35%
        3 = Low       (backups, updates)     — 25%

    Args:
        output_path: Path to save the CSV file
        n_samples: Total number of samples to generate
    """
    if output_path is None:
        data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        os.makedirs(data_dir, exist_ok=True)
        output_path = os.path.join(data_dir, 'network_traffic.csv')

    # Class distribution
    class_sizes = {
        0: int(n_samples * 0.15),   # Critical: 15%
        1: int(n_samples * 0.25),   # High:     25%
        2: int(n_samples * 0.35),   # Medium:   35%
        3: int(n_samples * 0.25),   # Low:      25%
    }

    records = []

    for priority_class, count in class_sizes.items():
        for _ in range(count):
            record = _generate_sample(priority_class)
            record['priority_class'] = priority_class
            records.append(record)

    df = pd.DataFrame(records)
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    df.to_csv(output_path, index=False)

    print(f"[+] Generated {len(df)} samples → {output_path}")
    print(f"[+] Class distribution:")
    print(df['priority_class'].value_counts().sort_index())

    return df


def _generate_sample(priority_class):
    """Generate a single traffic sample based on priority class."""

    if priority_class == 0:  # Critical — VoIP, emergency
        return {
            'packet_size':         np.random.randint(64, 300),
            'protocol_type':       np.random.choice([1, 1, 1, 0], p=[0.7, 0.1, 0.1, 0.1]),  # Mostly UDP
            'burst_rate':          np.random.randint(500, 5000),
            'flow_duration':       round(np.random.uniform(0.1, 30.0), 2),
            'source_port':         np.random.randint(16384, 32767),
            'dest_port':           np.random.choice([5060, 5061, 4000, 5004]),
            'byte_count':          np.random.randint(1000, 500000),
            'retransmission_rate': round(np.random.uniform(0.0, 2.0), 2),
            'jitter':              round(np.random.uniform(0.1, 10.0), 2),
            'latency':             round(np.random.uniform(1.0, 30.0), 2),
        }

    elif priority_class == 1:  # High — Video conference, ERP
        return {
            'packet_size':         np.random.randint(300, 1200),
            'protocol_type':       np.random.choice([0, 1, 3, 4], p=[0.3, 0.2, 0.25, 0.25]),
            'burst_rate':          np.random.randint(200, 2000),
            'flow_duration':       round(np.random.uniform(5.0, 120.0), 2),
            'source_port':         np.random.randint(1024, 65535),
            'dest_port':           np.random.choice([80, 443, 8080, 3389, 5900]),
            'byte_count':          np.random.randint(100000, 10000000),
            'retransmission_rate': round(np.random.uniform(0.5, 5.0), 2),
            'jitter':              round(np.random.uniform(5.0, 30.0), 2),
            'latency':             round(np.random.uniform(10.0, 80.0), 2),
        }

    elif priority_class == 2:  # Medium — Web, email
        return {
            'packet_size':         np.random.randint(200, 1400),
            'protocol_type':       np.random.choice([0, 3, 4, 5], p=[0.2, 0.3, 0.3, 0.2]),
            'burst_rate':          np.random.randint(50, 800),
            'flow_duration':       round(np.random.uniform(1.0, 180.0), 2),
            'source_port':         np.random.randint(1024, 65535),
            'dest_port':           np.random.choice([80, 443, 25, 587, 53, 110]),
            'byte_count':          np.random.randint(5000, 5000000),
            'retransmission_rate': round(np.random.uniform(1.0, 8.0), 2),
            'jitter':              round(np.random.uniform(10.0, 50.0), 2),
            'latency':             round(np.random.uniform(20.0, 200.0), 2),
        }

    else:  # Low — Backups, updates
        return {
            'packet_size':         np.random.randint(800, 1500),
            'protocol_type':       np.random.choice([0, 0, 3, 3], p=[0.4, 0.1, 0.25, 0.25]),
            'burst_rate':          np.random.randint(10, 300),
            'flow_duration':       round(np.random.uniform(30.0, 300.0), 2),
            'source_port':         np.random.randint(1024, 65535),
            'dest_port':           np.random.choice([21, 22, 69, 443, 8443]),
            'byte_count':          np.random.randint(1000000, 50000000),
            'retransmission_rate': round(np.random.uniform(2.0, 15.0), 2),
            'jitter':              round(np.random.uniform(20.0, 100.0), 2),
            'latency':             round(np.random.uniform(50.0, 500.0), 2),
        }


if __name__ == '__main__':
    generate_dataset()
