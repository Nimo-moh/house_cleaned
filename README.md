# Housing Data Cleaning Project  

This repository demonstrates the process of cleaning and preprocessing a housing dataset. The focus is on improving data quality by handling missing values, encoding categorical variables, removing outliers, and standardizing column names.

---

## *Project Description*  
The project involves cleaning a raw housing dataset to make it ready for analysis or machine learning tasks.  
Key steps include:  
1. Standardizing column names for consistency.  
2. Encoding categorical variables using LabelEncoder.  
3. Detecting and handling outliers using the Interquartile Range (IQR) method.  
4. Saving the cleaned dataset for downstream applications.  
## Dataset
The cleaned dataset used for this project is available for download:
[house_clean.csv]https://www.dropbox.com/scl/fi/swevfkuqfvqgbot1fzyoi/Housing_Cleaned.csv?rlkey=rj5wtafsbxi7co9717vcqhsie&st=sd9q9ccd&dl=0


## *Repository Contents*  

- **Housing.csv**: The original dataset (optional).  
- **Housing_Cleaned.csv**: The cleaned version of the dataset.  
- **clean_housing_data.py**: The Python script used to clean the data.  
- **README.md**: Documentation for the repository.  

---

## *Usage*  

### 1. *Requirements*  
Install the required Python libraries:  
```bash
pip install pandas scikit-learn
