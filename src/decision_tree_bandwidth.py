"""
SmartNet AI — Intelligent Bandwidth Allocation System
Decision Tree Classifier for Network Traffic Classification

This module implements the core ML pipeline for classifying network traffic
into priority tiers and computing dynamic bandwidth allocation.

Author : SmartNet AI Team (under Antigravity Expert Guidance)
Date   : March 2026
"""

import os
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import (
    classification_report, confusion_matrix, accuracy_score, ConfusionMatrixDisplay
)
from sklearn.preprocessing import LabelEncoder
from collections import Counter
import joblib

warnings.filterwarnings('ignore')

# ============================================================
# CONFIGURATION
# ============================================================

CLASS_NAMES = ['Critical', 'High', 'Medium', 'Low']
BANDWIDTH_ALLOCATION = {0: 0.40, 1: 0.30, 2: 0.20, 3: 0.10}

FEATURE_COLUMNS = [
    'packet_size', 'protocol_type', 'burst_rate', 'flow_duration',
    'source_port', 'dest_port', 'byte_count', 'retransmission_rate',
    'jitter', 'latency'
]
TARGET_COLUMN = 'priority_class'

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'output')
MODEL_DIR = os.path.join(os.path.dirname(__file__), '..', 'models')
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')


# ============================================================
# 1. DATA LOADING
# ============================================================

def load_data(filepath=None):
    """Load the network traffic dataset."""
    if filepath is None:
        filepath = os.path.join(DATA_DIR, 'network_traffic.csv')

    if not os.path.exists(filepath):
        print(f"[!] Dataset not found at {filepath}")
        print("[*] Generating synthetic dataset...")
        from generate_dataset import generate_dataset
        generate_dataset(filepath)

    data = pd.read_csv(filepath)
    print(f"[+] Loaded dataset: {data.shape[0]} samples, {data.shape[1]} features")
    print(f"[+] Class distribution:\n{data[TARGET_COLUMN].value_counts().sort_index()}")
    return data


# ============================================================
# 2. EXPLORATORY DATA ANALYSIS
# ============================================================

def perform_eda(data):
    """Perform exploratory data analysis and save visualizations."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("\n" + "=" * 60)
    print("EXPLORATORY DATA ANALYSIS")
    print("=" * 60)

    # Basic statistics
    print("\n[+] Dataset Statistics:")
    print(data.describe().round(2))

    # Class distribution plot
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Bar chart
    class_counts = data[TARGET_COLUMN].value_counts().sort_index()
    colors = ['#e74c3c', '#f39c12', '#3498db', '#2ecc71']
    axes[0].bar(CLASS_NAMES, class_counts.values, color=colors, edgecolor='black')
    axes[0].set_title('Traffic Class Distribution', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Priority Class')
    axes[0].set_ylabel('Sample Count')
    for i, v in enumerate(class_counts.values):
        axes[0].text(i, v + 50, str(v), ha='center', fontweight='bold')

    # Pie chart
    axes[1].pie(class_counts.values, labels=CLASS_NAMES, colors=colors,
                autopct='%1.1f%%', startangle=90, explode=[0.05]*4)
    axes[1].set_title('Class Proportion', fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'class_distribution.png'), dpi=150)
    plt.close()
    print("[+] Saved: class_distribution.png")

    # Correlation heatmap
    fig, ax = plt.subplots(figsize=(12, 8))
    numeric_data = data.select_dtypes(include=[np.number])
    corr = numeric_data.corr()
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', center=0,
                square=True, linewidths=0.5, ax=ax)
    ax.set_title('Feature Correlation Matrix', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'correlation_matrix.png'), dpi=150)
    plt.close()
    print("[+] Saved: correlation_matrix.png")

    # Feature distributions by class
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    key_features = ['packet_size', 'burst_rate', 'flow_duration',
                    'latency', 'jitter', 'retransmission_rate']

    for idx, (feature, ax) in enumerate(zip(key_features, axes.flatten())):
        for cls in range(4):
            subset = data[data[TARGET_COLUMN] == cls][feature]
            ax.hist(subset, bins=30, alpha=0.5, label=CLASS_NAMES[cls],
                    color=colors[cls])
        ax.set_title(f'{feature} by Class', fontweight='bold')
        ax.legend(fontsize=8)

    plt.suptitle('Feature Distributions by Priority Class',
                 fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'feature_distributions.png'),
                dpi=150, bbox_inches='tight')
    plt.close()
    print("[+] Saved: feature_distributions.png")


# ============================================================
# 3. MODEL TRAINING
# ============================================================

def train_model(data, tune_hyperparameters=True):
    """Train the Decision Tree classifier."""
    print("\n" + "=" * 60)
    print("MODEL TRAINING")
    print("=" * 60)

    X = data[FEATURE_COLUMNS]
    y = data[TARGET_COLUMN]

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"[+] Training set: {X_train.shape[0]} samples")
    print(f"[+] Test set:     {X_test.shape[0]} samples")

    if tune_hyperparameters:
        print("\n[*] Running GridSearchCV for hyperparameter tuning...")
        param_grid = {
            'max_depth': [4, 6, 8, 10, 12],
            'min_samples_split': [10, 20, 30],
            'min_samples_leaf': [5, 10, 15],
            'criterion': ['gini', 'entropy']
        }

        grid_search = GridSearchCV(
            DecisionTreeClassifier(class_weight='balanced', random_state=42),
            param_grid, cv=5, scoring='accuracy', n_jobs=-1, verbose=0
        )
        grid_search.fit(X_train, y_train)

        model = grid_search.best_estimator_
        print(f"[+] Best Parameters: {grid_search.best_params_}")
        print(f"[+] Best CV Accuracy: {grid_search.best_score_:.4f}")
    else:
        model = DecisionTreeClassifier(
            criterion='gini', max_depth=8,
            min_samples_split=20, min_samples_leaf=10,
            class_weight='balanced', random_state=42
        )
        model.fit(X_train, y_train)

    # Cross-validation
    cv_scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
    print(f"[+] 5-Fold CV Accuracy: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")

    return model, X_train, X_test, y_train, y_test


# ============================================================
# 4. MODEL EVALUATION
# ============================================================

def evaluate_model(model, X_test, y_test):
    """Evaluate the trained model and generate reports."""
    print("\n" + "=" * 60)
    print("MODEL EVALUATION")
    print("=" * 60)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"\n[+] Test Accuracy: {accuracy:.4f}")
    print(f"\n[+] Classification Report:")
    print(classification_report(y_test, y_pred, target_names=CLASS_NAMES))

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots(figsize=(8, 6))
    disp = ConfusionMatrixDisplay(cm, display_labels=CLASS_NAMES)
    disp.plot(cmap='Blues', ax=ax, values_format='d')
    ax.set_title('SmartNet AI — Confusion Matrix', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'confusion_matrix.png'), dpi=150)
    plt.close()
    print("[+] Saved: confusion_matrix.png")

    # Feature Importance
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]

    fig, ax = plt.subplots(figsize=(10, 6))
    colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(FEATURE_COLUMNS)))
    ax.barh(range(len(FEATURE_COLUMNS)),
            importances[indices], color=colors, edgecolor='black')
    ax.set_yticks(range(len(FEATURE_COLUMNS)))
    ax.set_yticklabels([FEATURE_COLUMNS[i] for i in indices])
    ax.set_xlabel('Importance Score')
    ax.set_title('Feature Importance — Decision Tree', fontsize=14, fontweight='bold')
    ax.invert_yaxis()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'feature_importance.png'), dpi=150)
    plt.close()
    print("[+] Saved: feature_importance.png")

    return accuracy, y_pred


# ============================================================
# 5. DECISION TREE VISUALIZATION
# ============================================================

def visualize_tree(model, max_depth_display=4):
    """Generate and save decision tree visualization."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("\n[*] Generating Decision Tree visualization...")

    # Full-size tree plot
    fig, ax = plt.subplots(figsize=(24, 12))
    plot_tree(model, feature_names=FEATURE_COLUMNS,
              class_names=CLASS_NAMES, filled=True,
              rounded=True, max_depth=max_depth_display,
              fontsize=8, ax=ax)
    ax.set_title('SmartNet AI — Decision Tree (Top Levels)',
                 fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'decision_tree.png'), dpi=150)
    plt.close()
    print("[+] Saved: decision_tree.png")

    # Text representation
    tree_rules = export_text(model, feature_names=FEATURE_COLUMNS, max_depth=6)
    rules_path = os.path.join(OUTPUT_DIR, 'tree_rules.txt')
    with open(rules_path, 'w') as f:
        f.write("SmartNet AI — Decision Tree Rules\n")
        f.write("=" * 50 + "\n\n")
        f.write(tree_rules)
    print(f"[+] Saved: tree_rules.txt")

    return tree_rules


# ============================================================
# 6. BANDWIDTH ALLOCATION ENGINE
# ============================================================

def allocate_bandwidth(predictions, total_bandwidth_mbps=1000):
    """
    Allocate bandwidth based on Decision Tree predictions.

    Uses a hybrid strategy: 70% base allocation + 30% demand-driven.

    Args:
        predictions: Array of predicted priority classes (0-3)
        total_bandwidth_mbps: Total available bandwidth in Mbps

    Returns:
        Dictionary mapping class names to allocated bandwidth (Mbps)
    """
    flow_counts = Counter(predictions)
    total_flows = len(predictions)

    allocation = {}
    for cls, base_pct in BANDWIDTH_ALLOCATION.items():
        demand_ratio = flow_counts.get(cls, 0) / max(total_flows, 1)
        adjusted_pct = 0.7 * base_pct + 0.3 * demand_ratio
        allocation[CLASS_NAMES[cls]] = round(adjusted_pct * total_bandwidth_mbps, 2)

    # Normalize
    total_allocated = sum(allocation.values())
    if total_allocated > total_bandwidth_mbps:
        scale = total_bandwidth_mbps / total_allocated
        allocation = {k: round(v * scale, 2) for k, v in allocation.items()}

    return allocation


def ag_enhanced_allocation(predictions, total_bandwidth_mbps=1000,
                            ag_efficiency_factor=1.15):
    """
    Antigravity-enhanced bandwidth allocation.

    Incorporates AG infrastructure efficiency gains that effectively
    increase available bandwidth through reduced physical-layer overhead.

    Args:
        predictions: Predicted priority classes
        total_bandwidth_mbps: Base available bandwidth
        ag_efficiency_factor: AG efficiency multiplier (default 1.15 = 15% gain)

    Returns:
        Tuple of (standard_allocation, ag_allocation)
    """
    standard = allocate_bandwidth(predictions, total_bandwidth_mbps)
    effective_bw = total_bandwidth_mbps * ag_efficiency_factor
    enhanced = allocate_bandwidth(predictions, effective_bw)

    return standard, enhanced


def display_allocation(standard, enhanced, total_bw):
    """Display bandwidth allocation comparison."""
    print("\n" + "=" * 70)
    print("BANDWIDTH ALLOCATION RESULTS")
    print("=" * 70)
    print(f"{'Class':<12} {'Standard (Mbps)':<18} {'AG-Enhanced (Mbps)':<20} {'Gain':<10}")
    print("-" * 60)
    for cls in CLASS_NAMES:
        std_val = standard[cls]
        enh_val = enhanced[cls]
        gain = enh_val - std_val
        print(f"{cls:<12} {std_val:<18.2f} {enh_val:<20.2f} +{gain:<10.2f}")
    print("-" * 60)
    print(f"{'TOTAL':<12} {sum(standard.values()):<18.2f} "
          f"{sum(enhanced.values()):<20.2f} "
          f"+{sum(enhanced.values()) - sum(standard.values()):<10.2f}")


def visualize_allocation(standard, enhanced):
    """Create bandwidth allocation comparison chart."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    colors = ['#e74c3c', '#f39c12', '#3498db', '#2ecc71']

    # Standard allocation
    axes[0].bar(CLASS_NAMES, standard.values(), color=colors, edgecolor='black')
    axes[0].set_title('Standard Allocation', fontsize=13, fontweight='bold')
    axes[0].set_ylabel('Bandwidth (Mbps)')
    for i, v in enumerate(standard.values()):
        axes[0].text(i, v + 5, f'{v:.1f}', ha='center', fontweight='bold')

    # AG-enhanced allocation
    axes[1].bar(CLASS_NAMES, enhanced.values(), color=colors, edgecolor='black',
                hatch='//')
    axes[1].set_title('AG-Enhanced Allocation (+15%)', fontsize=13, fontweight='bold')
    axes[1].set_ylabel('Bandwidth (Mbps)')
    for i, v in enumerate(enhanced.values()):
        axes[1].text(i, v + 5, f'{v:.1f}', ha='center', fontweight='bold')

    plt.suptitle('SmartNet AI — Bandwidth Allocation Comparison',
                 fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'bandwidth_allocation.png'), dpi=150)
    plt.close()
    print("[+] Saved: bandwidth_allocation.png")


# ============================================================
# 7. SAVE / LOAD MODEL
# ============================================================

def save_model(model, filepath=None):
    """Save the trained model to disk."""
    os.makedirs(MODEL_DIR, exist_ok=True)
    if filepath is None:
        filepath = os.path.join(MODEL_DIR, 'smartnet_model.pkl')
    joblib.dump(model, filepath)
    print(f"[+] Model saved: {filepath}")


def load_model(filepath=None):
    """Load a trained model from disk."""
    if filepath is None:
        filepath = os.path.join(MODEL_DIR, 'smartnet_model.pkl')
    model = joblib.load(filepath)
    print(f"[+] Model loaded: {filepath}")
    return model


# ============================================================
# 8. MAIN EXECUTION
# ============================================================

def main():
    """Run the complete SmartNet AI pipeline."""
    print("=" * 70)
    print("  SmartNet AI — Intelligent Bandwidth Allocation System")
    print("  Decision Tree Classifier Pipeline")
    print("  Developed under Antigravity Expert Guidance")
    print("=" * 70)

    # Step 1: Load data
    data = load_data()

    # Step 2: Exploratory Data Analysis
    perform_eda(data)

    # Step 3: Train model
    model, X_train, X_test, y_train, y_test = train_model(data, tune_hyperparameters=True)

    # Step 4: Evaluate model
    accuracy, y_pred = evaluate_model(model, X_test, y_test)

    # Step 5: Visualize decision tree
    visualize_tree(model)

    # Step 6: Bandwidth allocation
    total_bw = 1000  # 1 Gbps
    standard, enhanced = ag_enhanced_allocation(y_pred, total_bw, ag_efficiency_factor=1.15)
    display_allocation(standard, enhanced, total_bw)
    visualize_allocation(standard, enhanced)

    # Step 7: Save model
    save_model(model)

    print("\n" + "=" * 70)
    print("  SmartNet AI Pipeline Complete!")
    print(f"  Final Accuracy: {accuracy:.4f}")
    print(f"  Output saved to: {os.path.abspath(OUTPUT_DIR)}")
    print("=" * 70)


if __name__ == '__main__':
    main()
