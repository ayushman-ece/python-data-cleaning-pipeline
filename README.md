# 🧹 Python Data Cleaning Pipeline

A practical Python data-cleaning pipeline built with **Pandas** that takes a messy employee CSV dataset, cleans and validates the data, and exports a clean CSV file.

This project demonstrates important data-preprocessing techniques used before data analysis and machine learning.

---

## 🎯 Project Goal

Real-world datasets are rarely perfect.

They may contain:

- Missing values
- Duplicate records
- Inconsistent text
- Invalid numerical values
- Unnecessary formatting differences

This project demonstrates how to build a reusable pipeline to handle these problems automatically.

---

## 🔄 Data Cleaning Pipeline

```text
Raw CSV
   ↓
Load Dataset
   ↓
Check Missing Values
   ↓
Fill Missing Values
   ↓
Remove Duplicates
   ↓
Clean Text Data
   ↓
Validate Data
   ↓
Generate Summary
   ↓
Export Clean CSV
```

---

## ✨ Features

- 📂 Load employee data from CSV
- 🔍 Detect missing values
- 🧮 Fill missing numerical values using averages
- ♻️ Detect duplicate records
- 🗑️ Remove duplicate records
- ✨ Clean employee names
- 🏢 Standardize department names
- ⚠️ Detect invalid Age and Salary values
- 📊 Generate final data summary
- 💾 Export cleaned dataset
- 🔄 Run the entire process as one pipeline

---

## 🛠️ Technologies Used

- Python
- Pandas
- CSV
- Data Cleaning
- Data Preprocessing
- Object-Oriented Programming

---

## 📁 Project Structure

```text
python-data-cleaning-pipeline/
│
├── main.py
├── data_cleaner.py
├── employees.csv
├── cleaned_employees.csv
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📄 Input Dataset

The original `employees.csv` contains intentionally messy data:

```csv
Name,Age,Department,Salary
Rahul,21,IT,50000
Aman,,HR,42000
Priya,22,IT,
Neha,21,Sales,48000
Arjun,23,IT,58000
Simran,,HR,45000
Riya,22,Sales,52000
Rahul,21,IT,50000
```

The dataset contains:

- Missing Age
- Missing Salary
- A duplicate Rahul record

These problems allow the cleaning pipeline to demonstrate real data-preprocessing techniques.

---

# 🧠 Concepts Learned

## 1. Pandas DataFrame

The CSV is loaded using:

```python
pd.read_csv(file_name)
```

This creates a Pandas DataFrame containing rows and columns.

---

## 2. Detecting Missing Values

```python
self.data.isnull().sum()
```

This counts missing values in every column.

Example:

```text
Name          0
Age           2
Department    0
Salary        1
```

---

## 3. Filling Missing Values

Missing Age values are replaced using the average Age:

```python
self.data["Age"] = self.data["Age"].fillna(
    self.data["Age"].mean()
)
```

Missing Salary values are handled similarly.

This is called **imputation**.

---

## 4. Detecting Duplicates

```python
self.data.duplicated().sum()
```

This counts duplicate rows.

---

## 5. Removing Duplicates

```python
self.data = self.data.drop_duplicates()
```

This removes duplicate records from the DataFrame.

---

## 6. Cleaning Text

Employee names are cleaned using:

```python
.str.strip().str.title()
```

Example:

```text
" rahul tiwari " → "Rahul Tiwari"
```

Departments are standardized using:

```python
.str.strip().str.upper()
```

Example:

```text
" it " → "IT"
```

---

## 7. Data Validation

The pipeline checks for invalid numerical values:

```python
invalid_age = self.data["Age"] <= 0
invalid_salary = self.data["Salary"] <= 0
```

The conditions are combined:

```python
invalid_rows = invalid_age | invalid_salary
```

The `|` operator means **OR**.

---

## 8. Boolean Filtering

Invalid rows are removed using:

```python
self.data = self.data[~invalid_rows]
```

The `~` operator means **NOT**.

Therefore, only valid rows remain.

---

## 9. Exporting Data

The cleaned DataFrame is exported using:

```python
self.data.to_csv(
    "cleaned_employees.csv",
    index=False
)
```

`index=False` prevents Pandas from adding its DataFrame index as an extra CSV column.

---

# 🚀 Installation

Install the required dependency:

```bash
pip install -r requirements.txt
```

Or:

```bash
pip install pandas
```

---

# ▶️ Running the Project

Run:

```bash
python main.py
```

The complete cleaning pipeline will execute automatically.

---

# 📊 Final Pipeline Output

The program performs:

```text
1. Missing-value analysis
2. Missing-value imputation
3. Duplicate detection
4. Duplicate removal
5. Text cleaning
6. Data validation
7. Final statistics
8. CSV export
```

---

# 📚 What I Learned

Through this project, I learned:

- Pandas DataFrames
- CSV data processing
- Missing-value detection
- `isnull()`
- `fillna()`
- `mean()`
- Duplicate detection
- `duplicated()`
- `drop_duplicates()`
- String cleaning
- `strip()`
- `title()`
- `upper()`
- Boolean filtering
- `&` and `|`
- `~` operator
- Data validation
- CSV export
- Data preprocessing
- Building reusable data pipelines

---

# 🔮 Future Improvements

Possible future improvements:

- Automatic detection of numerical columns
- Automatic detection of categorical columns
- Median-based missing-value imputation
- Outlier detection
- Data-quality reports
- Support for multiple CSV files
- Excel file support
- Visualization of data-quality problems
- Machine-learning preprocessing
- Streamlit dashboard

---

# 🎓 Project Status

✅ Completed

This project is part of my Python → Data Science → AI learning journey.

---

# 👨‍💻 Author

**Ayushman Tiwari**

GitHub:

https://github.com/ayushman-ece