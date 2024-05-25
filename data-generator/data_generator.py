import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Number of samples to generate
num_samples = 1000

# Function to generate random date within a range
def random_date(start, end):
    return fake.date_between(start_date=start, end_date=end)

# Function to generate random symptoms
def random_symptoms():
    symptoms_list = ['Fever', 'Cough', 'Fatigue', 'Shortness of breath', 'Loss of taste', 'Loss of smell', 'Sore throat']
    return ', '.join(random.sample(symptoms_list, random.randint(1, 4)))

# Generating sample data
data = {
    'PatientID': [fake.uuid4() for _ in range(num_samples)],
    'Age': [random.randint(0, 100) for _ in range(num_samples)],
    'Gender': [random.choice(['Male', 'Female', 'Other']) for _ in range(num_samples)],
    'Symptoms': [random_symptoms() for _ in range(num_samples)],
    'TestResult': [random.choice(['Positive', 'Negative']) for _ in range(num_samples)],
    'Hospitalized': [random.choice([True, False]) for _ in range(num_samples)],
    'Recovered': [random.choice([True, False]) for _ in range(num_samples)],
    'DateTested': [random_date(datetime(2020, 1, 1), datetime(2023, 12, 31)) for _ in range(num_samples)]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Saving the data to a CSV file
csv_file = 'covid19_sample_data.csv'
df.to_csv(csv_file, index=False)

print(f"Sample COVID-19 data generated and saved to {csv_file}")

# This script uses the Faker library to generate realistic names, dates, and other attributes. The generated data includes:

# PatientID: A unique identifier for each patient.
# Age: Random age between 0 and 100.
# Gender: Randomly chosen from 'Male', 'Female', and 'Other'.
# Symptoms: A random selection of symptoms.
# TestResult: Either 'Positive' or 'Negative'.
# Hospitalized: Boolean indicating whether the patient was hospitalized.
# Recovered: Boolean indicating whether the patient recovered.
# DateTested: Random date between January 1, 2020, and December 31, 2023.
# This data is then saved to a CSV file named covid19_sample_data.csv. You can run this script locally to generate the sample data and save it to your machine.