import pandas as pd


class DataCleaner:

    def __init__(self, file_name):
        self.file_name = file_name
        self.data = pd.read_csv(file_name)

    def show_missing_values(self):
        missing = self.data.isnull().sum()

        print("\n===== MISSING VALUES =====")
        print(missing)

    def fill_missing_values(self):
        self.data["Age"] = self.data["Age"].fillna(
            self.data["Age"].mean()
        )

        self.data["Salary"] = self.data["Salary"].fillna(
            self.data["Salary"].mean()
        )

        print("\n===== MISSING VALUES FILLED =====")
        print(self.data)

    def remove_duplicates(self):
        duplicates = self.data.duplicated().sum()

        print("\n===== DUPLICATE CHECK =====")
        print(f"Duplicates Found: {duplicates}")

        self.data = self.data.drop_duplicates()

        print("\n===== AFTER REMOVING DUPLICATES =====")
        print(self.data)

    def clean_text_data(self):
        self.data["Name"] = (
            self.data["Name"]
            .str.strip()
            .str.title()
        )

        self.data["Department"] = (
            self.data["Department"]
            .str.strip()
            .str.upper()
        )

        print("\n===== TEXT DATA CLEANED =====")
        print(self.data)

    def validate_data(self):
        invalid_age = self.data["Age"] <= 0
        invalid_salary = self.data["Salary"] <= 0

        invalid_rows = invalid_age | invalid_salary

        print("\n===== DATA VALIDATION =====")
        print(f"Invalid Records: {invalid_rows.sum()}")

        self.data = self.data[~invalid_rows].copy()

        print("\n===== AFTER VALIDATION =====")
        print(self.data)

    def show_final_summary(self):
        print("\n===== FINAL DATA SUMMARY =====")
        print(f"Total Records : {len(self.data)}")
        print(f"Average Age   : {self.data['Age'].mean():.2f}")
        print(f"Average Salary: ₹{self.data['Salary'].mean():.2f}")

    def export_cleaned_data(self):
        output_file = "cleaned_employees.csv"

        self.data.to_csv(output_file, index=False)

        print("\n===== DATA EXPORTED =====")
        print(f"Cleaned data saved to {output_file}")

    def run_pipeline(self):
        print("\n🚀 STARTING DATA CLEANING PIPELINE")

        self.show_missing_values()
        self.fill_missing_values()
        self.remove_duplicates()
        self.clean_text_data()
        self.validate_data()
        self.show_final_summary()
        self.export_cleaned_data()

        print("\n✅ DATA CLEANING PIPELINE COMPLETED")