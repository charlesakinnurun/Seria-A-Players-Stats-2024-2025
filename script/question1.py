import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/seria_cleaned.csv")

# Which player has the highest ratio of successful dribbles to dribble attempts among those who have attempted at least 50 dribbles?

# Filter for players with at least 50 dribble attempts
dribblers = df[df["dribble_attempts"] >= 50].copy()

# Calculate the dribble success ratio
dribblers["dribble_success_ratio"] = dribblers["successful_dribbles"] / dribblers["dribble_attempts"]

# Find the player with the highest ratio
best_dribbler = dribblers.sort_values(by="dribble_success_ratio",ascending=False).iloc[0]
print(f"The player with the highest successful dribble ratio (attempting >= 50 dribbles) is {best_dribbler['player']} from {best_dribbler['team']} with a ratio of {best_dribbler['dribble_success_ratio']:.2f}.")

