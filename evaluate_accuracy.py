import csv
from collections import Counter, defaultdict
from pathlib import Path
import argparse


def compute_metrics(rows):
    # rows: list of dicts with keys: predicted_label, true_label
    total = 0
    correct = 0
    per_class = defaultdict(lambda: {"tp": 0, "fp": 0, "fn": 0})
    for r in rows:
        pred = r.get("predicted_label", "none")
        true = r.get("true_label", "")
        if true == "":
            continue
        total += 1
        if pred == true:
            correct += 1
            per_class[true]["tp"] += 1
        else:
            per_class[pred]["fp"] += 1
            per_class[true]["fn"] += 1
    accuracy = correct / total if total else 0.0
    return accuracy, per_class, total


def print_report(accuracy, per_class, total):
    print(f"Total labeled samples: {total}")
    print(f"Overall accuracy: {accuracy:.4f}")
    print("Per-class stats:")
    for cls, stats in per_class.items():
        tp = stats.get("tp", 0)
        fp = stats.get("fp", 0)
        fn = stats.get("fn", 0)
        prec = tp / (tp + fp) if (tp + fp) else 0.0
        rec = tp / (tp + fn) if (tp + fn) else 0.0
        print(f"  {cls}: TP={tp} FP={fp} FN={fn} Precision={prec:.3f} Recall={rec:.3f}")


def load_csv(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)
    return rows


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate gesture prediction accuracy from CSV.")
    parser.add_argument("--csv", type=str, default="gesture_logs/log.csv", help="Path to the CSV file produced by main.py")
    args = parser.parse_args()

    csv_path = Path(args.csv)
    if not csv_path.exists():
        print(f"CSV file not found: {csv_path}")
        raise SystemExit(1)

    rows = load_csv(csv_path)
    # CSV currently has columns: timestamp, frame_index, predicted_label, image_path
    # To compute accuracy, add a `true_label` column to the CSV (manually or via a small labeling tool)

    accuracy, per_class, total = compute_metrics(rows)
    print_report(accuracy, per_class, total)
