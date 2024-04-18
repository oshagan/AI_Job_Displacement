import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file into a DataFrame
df = pd.read_csv('My_Data.csv')

# Step 2: Explore the data
print(df.head())  # Check the first few rows of the DataFrame
print(df.info())  # Get information about the DataFrame, such as data types and missing values

# Step 3: Analyze the data (example: calculate some statistics)
summary_stats = df.describe()
print(summary_stats)

# Step 4: Make plots
# For example, let's say you want to create a histogram of a numerical column
plt.hist(df['AI Impact'], bins=20)
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of YourNumericColumn')
plt.show()
