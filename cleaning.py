# %% [markdown]
# Data Preprocessing

# %% [markdown]
# Import the neccessary libraries

# %%
import pandas as pd

# %% [markdown]
# Load the dataset

# %%
df = pd.read_csv("seria.csv")

# %% [markdown]
# Replace commas with periods and convert to float in "Pass Completion %" column

# %%
df["Pass Completion %"] = df["Pass Completion %"].str.replace(",",".",regex=True).astype(float)

# %% [markdown]
# Replace commas with and in "Postion" column

# %%
df["Position"] = df["Position"].str.replace(","," and ",regex=True)

# %% [markdown]
# Fill missing values in "Pass Completion %" with the mean

# %%
df['Pass Completion %'] = df['Pass Completion %'].fillna(df['Pass Completion %'].mean())

# %% [markdown]
# The 'Age' column is in 'YY-DDD' format, so we extract the years and convert to integer

# %%
df['Age'] = df['Age'].apply(lambda x: int(x.split('-')[0]))

# %% [markdown]
# Convert "Date" Column to datetime objects

# %%
df["Date"] = pd.to_datetime(df["Date"])

# %% [markdown]
# Check for missing values

# %%
df_missing = df.isnull().sum()

# %% [markdown]
# Check for duplicates

# %%
df_duplicated = df.duplicated()

# %% [markdown]
# Drop duplicates

# %%
df_duplicates = df.drop_duplicates()

# %% [markdown]
# Rename columns for Clarity and Consistency

# %%
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

# %% [markdown]
# Save the Cleaned data

# %%
df.to_csv("seria_cleaned.csv",index=False)
print("Saved Successfully")


