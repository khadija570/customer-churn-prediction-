print("PROGRAM_STARTED")
import sys
sys.stdout.reconfigure(encoding='utf-8')
# ============================================
#   CUSTOMER CHURN PREDICTION - Telco Dataset
# ============================================
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # <- fixes Windows display issue
import matplotlib.pyplot as plt
import os 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, roc_auc_score, confusion_matrix,
    roc_curve, ConfusionMatrixDisplay
)

# -- 1. LOAD DATA
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, "WA_Fn-UseC_-Telco-Customer-Churn.csv")

df = pd.read_csv(csv_path)
# -- 2. CLEAN DATA
df = df.drop(columns=["customerID"])
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df = df.dropna()

# -- 3. ENCODE CATEGORICAL COLUMNS
le = LabelEncoder()
for col in df.select_dtypes(include="object").columns:
    df[col] = le.fit_transform(df[col])

# -- 4. SPLIT FEATURES & TARGET
X = df.drop(columns=["Churn"])
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# -- 5. STANDARD SCALER
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

# -- 6. TRAIN MODELS
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
    "Random Forest":       RandomForestClassifier(n_estimators=100, random_state=42),
    "XGBoost":             XGBClassifier(n_estimators=100, random_state=42, verbosity=0),
}

for name, model in models.items():
    model.fit(X_train, y_train)

# -- 7. EVALUATE METRICS
print(f"\n{'Model':<25} {'Accuracy':>10} {'Precision':>10} {'Recall':>10} {'F1':>10} {'AUC-ROC':>10}")
print("-" * 80)

results = {}
for name, model in models.items():
    y_pred  = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    acc  = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec  = recall_score(y_test, y_pred)
    f1   = f1_score(y_test, y_pred)
    auc  = roc_auc_score(y_test, y_proba)

    results[name] = [acc, prec, rec, f1, auc]
    print(f"{name:<25} {acc:>10.4f} {prec:>10.4f} {rec:>10.4f} {f1:>10.4f} {auc:>10.4f}")

# -- 8. CONFUSION MATRICES
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle("Confusion Matrices", fontsize=14, fontweight="bold")

for ax, (name, model) in zip(axes, models.items()):
    cm = confusion_matrix(y_test, model.predict(X_test))
    ConfusionMatrixDisplay(cm, display_labels=["Retained", "Churned"]).plot(ax=ax, colorbar=False)
    ax.set_title(name, fontweight="bold")

plt.tight_layout()
plt.savefig("confusion_matrices.png", dpi=150, bbox_inches="tight")
plt.close()  # <- pas de plt.show()
print("confusion_matrices.png saved!")

# -- 9. ROC CURVES
plt.figure(figsize=(8, 6))
colors = ["#3498db", "#2ecc71", "#e74c3c"]

for (name, model), color in zip(models.items(), colors):
    y_proba = model.predict_proba(X_test)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_proba)
    auc = roc_auc_score(y_test, y_proba)
    plt.plot(fpr, tpr, color=color, lw=2, label=f"{name}  (AUC = {auc:.3f})")

plt.plot([0,1],[0,1], "k--", lw=1, label="Random")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curves", fontweight="bold")
plt.legend()
plt.grid(alpha=0.3)
plt.savefig("roc_curves.png", dpi=150, bbox_inches="tight")
plt.close()  # <- pas de plt.show()
print("roc_curves.png saved!")

# -- 10. METRIC COMPARISON
metrics_df = pd.DataFrame(results, index=["Accuracy","Precision","Recall","F1","AUC-ROC"]).T

metrics_df.plot(kind="bar", figsize=(10, 6), colormap="Set2", edgecolor="white")
plt.title("Model Comparison - All Metrics", fontweight="bold")
plt.ylabel("Score")
plt.xticks(rotation=15)
plt.ylim(0, 1.1)
plt.legend(loc="lower right")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("metric_comparison.png", dpi=150, bbox_inches="tight")
plt.close()  # <- pas de plt.show()
print("metric_comparison.png saved!")

print("\nDone! Ouvre ton dossier CHURN_PREDICTION pour voir les 3 images PNG.")
print("PROGRAM_FINISHED")
print("PROGRAM_STARTED")
import sys
sys.stdout.reconfigure(encoding='utf-8')
# ============================================
#   CUSTOMER CHURN PREDICTION - Telco Dataset
# ============================================
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # <- fixes Windows display issue
import matplotlib.pyplot as plt
import os 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, roc_auc_score, confusion_matrix,
    roc_curve, ConfusionMatrixDisplay
)

# -- 1. LOAD DATA
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, "WA_Fn-UseC_-Telco-Customer-Churn.csv")

df = pd.read_csv(csv_path)
# -- 2. CLEAN DATA
df = df.drop(columns=["customerID"])
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df = df.dropna()

# -- 3. ENCODE CATEGORICAL COLUMNS
le = LabelEncoder()
for col in df.select_dtypes(include="object").columns:
    df[col] = le.fit_transform(df[col])

# -- 4. SPLIT FEATURES & TARGET
X = df.drop(columns=["Churn"])
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# -- 5. STANDARD SCALER
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

# -- 6. TRAIN MODELS
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
    "Random Forest":       RandomForestClassifier(n_estimators=100, random_state=42),
    "XGBoost":             XGBClassifier(n_estimators=100, random_state=42, verbosity=0),
}

for name, model in models.items():
    model.fit(X_train, y_train)

# -- 7. EVALUATE METRICS
print(f"\n{'Model':<25} {'Accuracy':>10} {'Precision':>10} {'Recall':>10} {'F1':>10} {'AUC-ROC':>10}")
print("-" * 80)

results = {}
for name, model in models.items():
    y_pred  = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    acc  = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec  = recall_score(y_test, y_pred)
    f1   = f1_score(y_test, y_pred)
    auc  = roc_auc_score(y_test, y_proba)

    results[name] = [acc, prec, rec, f1, auc]
    print(f"{name:<25} {acc:>10.4f} {prec:>10.4f} {rec:>10.4f} {f1:>10.4f} {auc:>10.4f}")

# -- 8. CONFUSION MATRICES
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle("Confusion Matrices", fontsize=14, fontweight="bold")

for ax, (name, model) in zip(axes, models.items()):
    cm = confusion_matrix(y_test, model.predict(X_test))
    ConfusionMatrixDisplay(cm, display_labels=["Retained", "Churned"]).plot(ax=ax, colorbar=False)
    ax.set_title(name, fontweight="bold")

plt.tight_layout()
plt.savefig("confusion_matrices.png", dpi=150, bbox_inches="tight")
plt.close()  # <- pas de plt.show()
print("confusion_matrices.png saved!")

# -- 9. ROC CURVES
plt.figure(figsize=(8, 6))
colors = ["#3498db", "#2ecc71", "#e74c3c"]

for (name, model), color in zip(models.items(), colors):
    y_proba = model.predict_proba(X_test)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_proba)
    auc = roc_auc_score(y_test, y_proba)
    plt.plot(fpr, tpr, color=color, lw=2, label=f"{name}  (AUC = {auc:.3f})")

plt.plot([0,1],[0,1], "k--", lw=1, label="Random")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curves", fontweight="bold")
plt.legend()
plt.grid(alpha=0.3)
plt.savefig("roc_curves.png", dpi=150, bbox_inches="tight")
plt.close()  # <- pas de plt.show()
print("roc_curves.png saved!")

# -- 10. METRIC COMPARISON
metrics_df = pd.DataFrame(results, index=["Accuracy","Precision","Recall","F1","AUC-ROC"]).T

metrics_df.plot(kind="bar", figsize=(10, 6), colormap="Set2", edgecolor="white")
plt.title("Model Comparison - All Metrics", fontweight="bold")
plt.ylabel("Score")
plt.xticks(rotation=15)
plt.ylim(0, 1.1)
plt.legend(loc="lower right")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("metric_comparison.png", dpi=150, bbox_inches="tight")
plt.close()  # <- pas de plt.show()
print("metric_comparison.png saved!")

print("\nDone! Ouvre ton dossier CHURN_PREDICTION pour voir les 3 images PNG.")
print("PROGRAM_FINISHED")
print("PROGRAM_STARTED")
import sys
sys.stdout.reconfigure(encoding='utf-8')
# ============================================
#   CUSTOMER CHURN PREDICTION - Telco Dataset
# ============================================
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # <- fixes Windows display issue
import matplotlib.pyplot as plt
import os 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, roc_auc_score, confusion_matrix,
    roc_curve, ConfusionMatrixDisplay
)

# -- 1. LOAD DATA
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, "WA_Fn-UseC_-Telco-Customer-Churn.csv")

df = pd.read_csv(csv_path)
# -- 2. CLEAN DATA
df = df.drop(columns=["customerID"])
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df = df.dropna()

# -- 3. ENCODE CATEGORICAL COLUMNS
le = LabelEncoder()
for col in df.select_dtypes(include="object").columns:
    df[col] = le.fit_transform(df[col])

# -- 4. SPLIT FEATURES & TARGET
X = df.drop(columns=["Churn"])
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# -- 5. STANDARD SCALER
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

# -- 6. TRAIN MODELS
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
    "Random Forest":       RandomForestClassifier(n_estimators=100, random_state=42),
    "XGBoost":             XGBClassifier(n_estimators=100, random_state=42, verbosity=0),
}

for name, model in models.items():
    model.fit(X_train, y_train)

# -- 7. EVALUATE METRICS
print(f"\n{'Model':<25} {'Accuracy':>10} {'Precision':>10} {'Recall':>10} {'F1':>10} {'AUC-ROC':>10}")
print("-" * 80)

results = {}
for name, model in models.items():
    y_pred  = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    acc  = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec  = recall_score(y_test, y_pred)
    f1   = f1_score(y_test, y_pred)
    auc  = roc_auc_score(y_test, y_proba)

    results[name] = [acc, prec, rec, f1, auc]
    print(f"{name:<25} {acc:>10.4f} {prec:>10.4f} {rec:>10.4f} {f1:>10.4f} {auc:>10.4f}")

# -- 8. CONFUSION MATRICES
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle("Confusion Matrices", fontsize=14, fontweight="bold")

for ax, (name, model) in zip(axes, models.items()):
    cm = confusion_matrix(y_test, model.predict(X_test))
    ConfusionMatrixDisplay(cm, display_labels=["Retained", "Churned"]).plot(ax=ax, colorbar=False)
    ax.set_title(name, fontweight="bold")

plt.tight_layout()
plt.savefig("confusion_matrices.png", dpi=150, bbox_inches="tight")
plt.close()  # <- pas de plt.show()
print("confusion_matrices.png saved!")

# -- 9. ROC CURVES
plt.figure(figsize=(8, 6))
colors = ["#3498db", "#2ecc71", "#e74c3c"]

for (name, model), color in zip(models.items(), colors):
    y_proba = model.predict_proba(X_test)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_proba)
    auc = roc_auc_score(y_test, y_proba)
    plt.plot(fpr, tpr, color=color, lw=2, label=f"{name}  (AUC = {auc:.3f})")

plt.plot([0,1],[0,1], "k--", lw=1, label="Random")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curves", fontweight="bold")
plt.legend()
plt.grid(alpha=0.3)
plt.savefig("roc_curves.png", dpi=150, bbox_inches="tight")
plt.close()  # <- pas de plt.show()
print("roc_curves.png saved!")

# -- 10. METRIC COMPARISON
metrics_df = pd.DataFrame(results, index=["Accuracy","Precision","Recall","F1","AUC-ROC"]).T

metrics_df.plot(kind="bar", figsize=(10, 6), colormap="Set2", edgecolor="white")
plt.title("Model Comparison - All Metrics", fontweight="bold")
plt.ylabel("Score")
plt.xticks(rotation=15)
plt.ylim(0, 1.1)
plt.legend(loc="lower right")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("metric_comparison.png", dpi=150, bbox_inches="tight")
plt.close()  # <- pas de plt.show()
print("metric_comparison.png saved!")

print("\nDone! Ouvre ton dossier CHURN_PREDICTION pour voir les 3 images PNG.")
print("PROGRAM_FINISHED")
