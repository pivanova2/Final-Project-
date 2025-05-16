import pandas as pd
import matplotlib.pyplot as plt


def load_and_filter_data(path):
    # Load CSV and filter to only non-domestic arrests
    df = pd.read_csv(
        path,
        parse_dates=["Date"],
        date_format="%m/%d/%Y %I:%M:%S %p"
    )
    return df[(df["Arrest"] == True) & (df["Domestic"] == False)]

def get_crime_type_counts(df):
    # Return count of each crime type
    return df["Primary Type"].value_counts()


def get_top_crime_locations(df, top_n=10):
    # Return top N most frequent locations for crimes
    return df["Location Description"].value_counts().head(top_n)

def get_arrests_by_month(df):
    # Add a Month column and return arrest counts per month
    df["Month"] = df["Date"].dt.month
    return df["Month"].value_counts().sort_index()

def get_top_wards(df, top_n=5):
    # Return top N wards with the most arrests
    return df["Ward"].value_counts().head(top_n)

def plot_crime_type_counts(df):
    # Plot bar graph of number of reported crimes by type
    crime_counts = df["Primary Type"].value_counts()

    plt.figure(figsize=(12, 6))
    crime_counts.plot(kind='bar', color='skyblue')
    plt.title("Reported Crimes by Type (Non-Domestic Arrests)")
    plt.xlabel("Crime Type")
    plt.ylabel("Number of Reports")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def search_crime_by_type_and_location(df, crime_type, location):
    """
    Search for a specific crime type in a specific location.
    Raise error if crime type or location doesn't exist.
    """
    # Get available types and locations
    available_crimes = df["Primary Type"].unique()
    available_locations = df["Location Description"].unique()

    # Check if inputs are valid (case-insensitive)
    if crime_type.upper() not in map(str.upper, available_crimes):
        raise ValueError(f"Error: Crime type '{crime_type}' not found in the dataset.")
    
    if location.upper() not in map(str.upper, available_locations):
        raise ValueError(f"Error: Location '{location}' not found in the dataset.")

    # Filter for exact match (case-insensitive)
    matches = df[
        (df["Primary Type"].str.upper() == crime_type.upper()) &
        (df["Location Description"].str.upper() == location.upper())
    ]

    # Return number of matches found
    return len(matches)

