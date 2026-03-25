# SmartNet AI — Intelligent Bandwidth Allocation System

> **AI-driven network bandwidth allocation using Decision Trees and Cisco Packet Tracer**
> Developed under the guidance of Antigravity technology experts

---

## Overview

SmartNet AI classifies network traffic into four priority tiers using a **Decision Tree classifier** and dynamically allocates bandwidth via **Cisco QoS policies**. The system also models the impact of **Antigravity (AG) technology** on infrastructure efficiency.

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Generate Dataset
```bash
python src/generate_dataset.py
```

### 3. Run Full Pipeline
```bash
python src/decision_tree_bandwidth.py
```

### 4. Generate Visualizations
```bash
python src/visualize_results.py
```

## Project Structure

```
├── SmartNet_AI_Technical_Report.md    # Full technical report
├── cisco_topology_guide.md            # Packet Tracer setup guide
├── requirements.txt                   # Python dependencies
├── README.md                          # This file
├── src/
│   ├── decision_tree_bandwidth.py     # Main ML pipeline
│   ├── generate_dataset.py            # Synthetic data generator
│   └── visualize_results.py           # Charts & visual reports
├── data/                              # Generated datasets
├── models/                            # Trained models (.pkl)
├── output/                            # Charts & visualizations
└── cisco/
    └── qos_config.txt                 # Cisco IOS QoS commands
```

## Traffic Priority Classes

| Class      | Bandwidth | Traffic Examples             |
|------------|-----------|------------------------------|
| Critical   | 40%       | VoIP, Emergency systems      |
| High       | 30%       | Video conferencing, ERP      |
| Medium     | 20%       | Web browsing, Email          |
| Low        | 10%       | Backups, Software updates    |

## Key Features

- **Decision Tree Classification** with GridSearchCV hyperparameter tuning
- **Dynamic bandwidth allocation** (70% base + 30% demand-driven)
- **Cisco Packet Tracer** topology with VLANs and QoS policies
- **Antigravity enhancement layer** (+15% effective bandwidth)
- **Comprehensive visualizations** (confusion matrix, feature importance, allocation charts)

## License

This project is developed for academic and research purposes.

---

*© 2026 SmartNet AI Team — Under Antigravity Expert Guidance*
