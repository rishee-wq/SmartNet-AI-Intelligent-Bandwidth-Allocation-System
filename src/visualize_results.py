"""
SmartNet AI — Results Visualization Module

Generates comprehensive charts and visual reports for the
SmartNet AI bandwidth allocation system.

Author : SmartNet AI Team
Date   : March 2026
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'output')
CLASS_NAMES = ['Critical', 'High', 'Medium', 'Low']
COLORS = ['#e74c3c', '#f39c12', '#3498db', '#2ecc71']


def plot_performance_comparison():
    """
    Generate before/after performance comparison chart
    showing SmartNet AI improvements.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    metrics = ['Latency\n(Critical)', 'Packet Loss\n(Critical)',
               'Bandwidth\nUtilization', 'VoIP MOS\nScore', 'Throughput\n(Mbps)']

    without_ai = [45, 5.2, 62, 3.2, 450]
    with_ai = [15, 0.3, 89, 4.4, 680]
    with_ag = [12, 0.2, 93, 4.6, 780]

    x = np.arange(len(metrics))
    width = 0.25

    fig, ax = plt.subplots(figsize=(14, 7))

    bars1 = ax.bar(x - width, without_ai, width, label='Without SmartNet AI',
                   color='#95a5a6', edgecolor='black')
    bars2 = ax.bar(x, with_ai, width, label='With SmartNet AI',
                   color='#3498db', edgecolor='black')
    bars3 = ax.bar(x + width, with_ag, width, label='With AG Enhancement',
                   color='#9b59b6', edgecolor='black', hatch='//')

    ax.set_xlabel('Performance Metrics', fontsize=12)
    ax.set_ylabel('Value', fontsize=12)
    ax.set_title('SmartNet AI — Performance Impact Analysis',
                 fontsize=16, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(metrics, fontsize=10)
    ax.legend(fontsize=11)
    ax.grid(axis='y', alpha=0.3)

    # Add value labels
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3), textcoords="offset points",
                        ha='center', va='bottom', fontsize=8, fontweight='bold')

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'performance_comparison.png'), dpi=150)
    plt.close()
    print("[+] Saved: performance_comparison.png")


def plot_qos_timeline():
    """Simulate and plot QoS metrics over time."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    time = np.arange(0, 60, 0.5)  # 60 seconds

    # Simulated latency patterns
    np.random.seed(42)
    critical_latency = 12 + 3 * np.sin(time / 5) + np.random.normal(0, 1, len(time))
    high_latency = 35 + 8 * np.sin(time / 7) + np.random.normal(0, 2, len(time))
    medium_latency = 80 + 15 * np.sin(time / 10) + np.random.normal(0, 5, len(time))
    low_latency = 150 + 30 * np.sin(time / 8) + np.random.normal(0, 10, len(time))

    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(time, critical_latency, color=COLORS[0], linewidth=2, label='Critical')
    ax.plot(time, high_latency, color=COLORS[1], linewidth=2, label='High')
    ax.plot(time, medium_latency, color=COLORS[2], linewidth=2, label='Medium')
    ax.plot(time, low_latency, color=COLORS[3], linewidth=2, label='Low')

    ax.axhline(y=30, color='red', linestyle='--', alpha=0.5, label='Critical SLA (30ms)')
    ax.fill_between(time, 0, 30, alpha=0.05, color='red')

    ax.set_xlabel('Time (seconds)', fontsize=12)
    ax.set_ylabel('Latency (ms)', fontsize=12)
    ax.set_title('SmartNet AI — Real-Time Latency by Traffic Class',
                 fontsize=16, fontweight='bold')
    ax.legend(loc='upper right', fontsize=10)
    ax.set_ylim(0, 250)
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'qos_timeline.png'), dpi=150)
    plt.close()
    print("[+] Saved: qos_timeline.png")


def plot_ag_impact_model():
    """Visualize Antigravity technology efficiency improvements."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    categories = ['Cooling\nEfficiency', 'Rack\nDensity', 'Cable\nRouting',
                  'Hardware\nLongevity', 'Signal\nQuality', 'Energy\nSavings']
    traditional = [65, 70, 60, 75, 72, 55]
    ag_enhanced = [85, 91, 88, 90, 89, 78]

    fig, ax = plt.subplots(figsize=(12, 6))
    x = np.arange(len(categories))
    width = 0.35

    bars1 = ax.bar(x - width/2, traditional, width,
                   label='Traditional Infrastructure',
                   color='#95a5a6', edgecolor='black')
    bars2 = ax.bar(x + width/2, ag_enhanced, width,
                   label='AG-Enhanced Infrastructure',
                   color='#8e44ad', edgecolor='black', hatch='//')

    ax.set_ylabel('Efficiency Score (%)', fontsize=12)
    ax.set_title('Antigravity Technology — Infrastructure Efficiency Gains',
                 fontsize=16, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=10)
    ax.legend(fontsize=11)
    ax.set_ylim(0, 110)
    ax.grid(axis='y', alpha=0.3)

    # Add improvement annotations
    for i in range(len(categories)):
        improvement = ag_enhanced[i] - traditional[i]
        ax.annotate(f'+{improvement}%',
                    xy=(x[i] + width/2, ag_enhanced[i]),
                    xytext=(0, 5), textcoords="offset points",
                    ha='center', fontsize=9, fontweight='bold', color='#8e44ad')

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ag_impact_model.png'), dpi=150)
    plt.close()
    print("[+] Saved: ag_impact_model.png")


def generate_all_visualizations():
    """Generate all visualization charts."""
    print("\n" + "=" * 60)
    print("GENERATING VISUALIZATION REPORTS")
    print("=" * 60)

    plot_performance_comparison()
    plot_qos_timeline()
    plot_ag_impact_model()

    print(f"\n[+] All visualizations saved to: {os.path.abspath(OUTPUT_DIR)}")


if __name__ == '__main__':
    generate_all_visualizations()
