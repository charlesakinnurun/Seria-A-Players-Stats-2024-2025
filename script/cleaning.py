import pandas as pd

# Load the dataset
df = pd.read_csv("datasets/seria.csv")
print(df.head())
print(df.info())

# Replace commas with periods and convert to float in "Pass Completion %" column
df["Pass Completion %"] = df["Pass Completion %"].str.replace(",",".",regex=True).astype(float)
print(df.head())

# Replace commas with and in "Postion" column
df["Position"] = df["Position"].str.replace(","," and ",regex=True)
print(df.head())

# Fill missing values in "Pass Completion %" with the mean
df['Pass Completion %'] = df['Pass Completion %'].fillna(df['Pass Completion %'].mean())
print(df.head())

# Clean the "Age" Column
# The 'Age' column is in 'YY-DDD' format, so we extract the years and convert to integer
df['Age'] = df['Age'].apply(lambda x: int(x.split('-')[0]))
print(df.head())

# Convert "Date" Column to datetime objects
df["Date"] = pd.to_datetime(df["Date"])
print(df.head())

# Check for missing values
df_missing = df.isnull().sum()
print(df_missing)

# Check for duplicates
df_duplicated = df.duplicated()
print(df_duplicated)

df_duplicates = df.drop_duplicates()
print(df_duplicates.head())

# Rename columns for Clarity and Consistency
df.rename(columns={
    "Player":"player",
    "Team":"team",
    "Shirt Number":"shirt_number",
    "Nation":"nation",
    "Position":"position",
    "Age":"age",
    "Minutes":"minutes",
    "Goals":"goals",
    "Assists":"assists",
    "Penalty Shoot on Goal":"penalty_shoot_on_goal",
    "Penalty Shoot":"penalty_shoot",
    "Total Shoot":"total_shoot",
    "Shoot on Target ":"shoot_on_target",
    "Yellow Cards":"yellow_cards",
    "Red Cards":"red_cards",
    "Touches":"touches",
    "Dribbles":"dribbles",
    "Tackles":"tackles",
    "Blocks":"blocks",
    "Expected Goals (xG)":"expected_goals_xg",
    "Non-Penalty xG (npxG)":"non_penalty_xg_npxg",
    "Expected Assists (xAG)":"expected_assists_xag",
    "Shot-Creating Actions":"shot_creating_actions",
    "Goal-Creating Actions":"goal_creating_actions",
    "Passes Completed":"passes_completed",
    "Passes Attempted":"passes_attempted",
    "Pass Completion %":"pass_completed_%",
    "Progressive Passes":"progressive_passes",
    "Carries":"carries",
    "Progressive Carries":"progressive_carries",
    "Dribble Attempts":"dribble_attempts",
    "Successful Dribbles":"successful_dribbles",
    "Date":"date"
},inplace=True)
print(df.head())

# Save the Cleaned data
df.to_csv("datasets/seria_cleaned.csv",index=False)
print("Saved Successfully")