import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the dataset
file_path = 'path_to_your_file/Housing.csv'  # Replace with your file path
housing_data = pd.read_csv(file_path)

# Step 1: Standardize column names
housing_data.columns = [col.lower().replace(" ", "_") for col in housing_data.columns]

# Step 2: Encode categorical variables
# Columns to encode: mainroad, guestroom, basement, hotwaterheating, airconditioning, prefarea, furnishingstatus
categorical_cols = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea', 'furnishingstatus']
label_encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    housing_data[col] = le.fit_transform(housing_data[col])
    label_encoders[col] = le

# Step 3: Detect and handle outliers using IQR method
numeric_cols = housing_data.select_dtypes(include=['int64', 'float64']).columns

for col in numeric_cols:
    Q1 = housing_data[col].quantile(0.25)
    Q3 = housing_data[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    # Clip values to remove extreme outliers
    housing_data[col] = housing_data[col].clip(lower_bound, upper_bound)

# Step 4: Save the cleaned dataset
cleaned_file_path = 'path_to_save/Housing_Cleaned.csv'  # Replace with your desired path
housing_data.to_csv(cleaned_file_path, index=False)

print(f"Cleaned dataset saved to: {cleaned_file_path}")
