import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file
df = pd.read_csv('My_Data.csv')

# Step 2: Clean up the 'AI Impact' column and convert to numeric
df['AI Impact'] = df['AI Impact'].str.replace('%', '').astype(float)

# Step 3: Calculate the average 'AI Impact' for each job title
avg_impact_by_job = df.groupby('Job titiles')['AI Impact'].mean().reset_index()

# Step 4: Select the top 10 job titles based on average AI impact
top_10_job_titles = avg_impact_by_job.nlargest(10, 'AI Impact')

# Step 5: Create a bar plot
plt.figure(figsize=(12, 6))  # Adjust the figure size as needed
plt.bar(top_10_job_titles['Job titiles'], top_10_job_titles['AI Impact'])
plt.xlabel('Job Titles')
plt.ylabel('Average AI Impact')
plt.title('Top 10 Job Titles with Highest Average AI Impact')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()
p