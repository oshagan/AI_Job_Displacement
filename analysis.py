# import pandas as pd
# import matplotlib.pyplot as plt

# # Step 1: Load the CSV file
# df = pd.read_csv('My_Data.csv')

# # Step 2: Clean up the 'AI Impact' column and convert to numeric
# df['AI Impact'] = df['AI Impact'].str.replace('%', '').astype(float)

# # Step 3: Calculate the average 'AI Impact' for each job title
# avg_impact_by_job = df.groupby('Job titiles')['AI Impact'].mean().reset_index()

# # Step 4: Select the top 10 job titles based on average AI impact
# top_10_job_titles = avg_impact_by_job.nlargest(10, 'AI Impact')

# # Step 4b: Select the bottom 10 job titles based on average AI impact
# bottom_10_job_titles = avg_impact_by_job.nsmallest(10, 'AI Impact')

# # Step 5: Create a bar plot
# plt.figure(figsize=(12, 6))  # Adjust the figure size as needed

# # Plot the top 10 most exposed jobs
# top_bars = plt.bar(top_10_job_titles['Job titiles'], top_10_job_titles['AI Impact'], color='b', label='Top 10 Exposed')

# # Plot the bottom 10 least exposed jobs
# bottom_bars = plt.bar(bottom_10_job_titles['Job titiles'], bottom_10_job_titles['AI Impact'], color='r', label='Bottom 10 Exposed')

# # Function to add text labels on top of each bar
# def add_labels(bars):
#     for bar in bars:
#         yval = bar.get_height()
#         plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.1f}%', va='bottom', ha='center')

# add_labels(top_bars)
# add_labels(bottom_bars)

# plt.xlabel('Job Titles')
# plt.ylabel('Average AI Impact')
# plt.title('Top and Bottom 10 Job Titles with Highest and Lowest Average AI Impact')
# plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
# plt.legend()
# plt.tight_layout()  # Adjust layout to prevent clipping of labels
# plt.show()












# import pandas as pd
# import matplotlib.pyplot as plt

# # Step 1: Load the CSV file
# df = pd.read_csv('My_Data.csv')

# # Step 2: Clean up the 'AI Impact' column and convert to numeric
# df['AI Impact'] = df['AI Impact'].str.replace('%', '').astype(float)

# # Step 3: Group the data by 'Domain' and calculate the average AI impact for each domain
# avg_impact_by_domain = df.groupby('Domain')['AI Impact'].mean().reset_index()

# # Step 4: Select the domains with the least average AI impact
# bottom_domains = avg_impact_by_domain.nsmallest(10, 'AI Impact')

# # Step 5: Create a bar plot
# plt.figure(figsize=(12, 6))  # Adjust the figure size as needed

# # Plot the domains with the least average AI impact
# plt.bar(bottom_domains['Domain'], bottom_domains['AI Impact'], color='g')

# plt.xlabel('Domain')
# plt.ylabel('Average AI Impact')
# plt.title('Domains with the Least Average AI Impact')
# plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
# plt.tight_layout()  # Adjust layout to prevent clipping of labels
# plt.show()


















import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file
df = pd.read_csv('My_Data.csv')

# Step 2: Calculate the number of AI models and tasks for each domain
domain_stats = df.groupby('Domain').agg({'AI models': 'sum', 'Tasks': 'count'}).reset_index()

# Step 3: Create the scatter plot
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed

# Plot the scatter points for each domain
plt.scatter(domain_stats['AI models'], domain_stats['Tasks'], c=range(len(domain_stats)), cmap='viridis', s=100)

# Plot the scatter points for each job title
for index, row in df.iterrows():
    plt.scatter(row['AI models'], row['Tasks'], c=row['Domain'], cmap='viridis', alpha=0.7)

plt.xlabel('Number of AI Models')
plt.ylabel('Number of Tasks')
plt.title('AI Models vs Tasks for Each Job Title')
plt.grid(True)
plt.colorbar(label='Domain')
plt.tight_layout()
plt.show()

