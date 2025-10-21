#  Input Data Format

## 1. CSV File: `Input/data_sample.csv`

This CSV file contains synthetic data used to test statistical, visualization, and vector analysis modules.

| Column Name | Type | Description |
|--------------|------|--------------|
| `id` | int | Unique identifier for each record |
| `age` | int | Person's age in years (18–70) |
| `income` | float | Annual income in USD |
| `height_cm` | float | Height in centimeters |
| `weight_kg` | float | Weight in kilograms |
| `category` | str | Category label ∈ {A, B, C} |
| `city` | str | City name ∈ {Baton Rouge, New Orleans, Hammond, Lafayette, Shreveport} |
| `gender` | str | Gender ∈ {Male, Female, Other} |
| `score1` | float | Random performance score (0–100) |
| `score2` | float | Correlated score derived from `score1` |
| `u_x`, `u_y`, `u_z` | float | Components of vector **u** |
| `v_x`, `v_y`, `v_z` | float | Components of vector **v** |

### Example Row

---

## 2. Pickle File: `Input/data_sample.pkl`

This file contains the same dataset stored as a serialized Python dictionary.

**Structure:**
```python
{
    "meta": {
        "source": "synthetic",
        "rows": 300,
        "created_with": "Python"
    },
    "dataframe": pandas.DataFrame
}
import pickle
with open("Input/data_sample.pkl", "rb") as f:
    data = pickle.load(f)
df = data["dataframe"]


