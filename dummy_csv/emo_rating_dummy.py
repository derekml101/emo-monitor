import pandas as pd
import numpy as np
import time

# Set the random seed for reproducibility
np.random.seed(42)

# Define the number of samples
num_samples = 2000

# Generate random timestamps with millisecond precision within a specific date range
start_timestamp = int(time.mktime(time.strptime('2023-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')))
end_timestamp = int(time.mktime(time.strptime('2023-12-31 23:59:59', '%Y-%m-%d %H:%M:%S')))

# Generate random timestamps within the date range
random_timestamps = [start_timestamp + np.random.randint(0, (end_timestamp - start_timestamp)) for _ in range(num_samples)]
# Add milliseconds
random_timestamps = [ts + np.random.random() for ts in random_timestamps]
# Convert to datetime format
random_timestamps = [pd.to_datetime(ts, unit='s') for ts in random_timestamps]

# Generate random one-hot encoded ratings for the emotions
emotion_columns = ['Very Happy', 'Happy', 'Neutral', 'Sad', 'Very Sad']
ratings = np.zeros((num_samples, len(emotion_columns)), dtype=int)

for i in range(num_samples):
    ratings[i, np.random.randint(0, len(emotion_columns))] = 1

# Create a DataFrame with the ratings
ratings_df = pd.DataFrame(ratings, columns=emotion_columns)

# Add the sorted random timestamps to the DataFrame
ratings_df['Timestamp'] = sorted(random_timestamps)

# Save the DataFrame to a CSV file
csv_file_path = 'dummy_emotions_ratings_one_hot_pi_pico.csv'
ratings_df.to_csv(csv_file_path, index=False)

print(f"CSV file has been created and saved as {csv_file_path}")
