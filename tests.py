import pandas as pd
import pytest
from analysis import (
    load_and_filter_data,
    get_crime_type_counts,
    search_crime_by_type_and_location
)

# Sample data to simulate a tiny CSV
sample_data = {
    "Date": ["05/04/2024 12:00:00 AM", "05/05/2024 01:00:00 PM"],
    "Primary Type": ["THEFT", "BATTERY"],
    "Location Description": ["STREET", "GAS STATION"],
    "Arrest": [True, True],
    "Domestic": [False, False],
}

@pytest.fixture
def sample_df(tmp_path):
    # Create a temporary CSV file
    test_csv = tmp_path / "test.csv"
    pd.DataFrame(sample_data).to_csv(test_csv, index=False)
    return load_and_filter_data(test_csv)

def test_load_and_filter_data(sample_df):
    # Should return 2 rows (since both are True arrests and non-domestic)
    assert len(sample_df) == 2
    assert "Date" in sample_df.columns
    assert sample_df["Arrest"].all()
    assert not sample_df["Domestic"].any()

def test_get_crime_type_counts(sample_df):
    counts = get_crime_type_counts(sample_df)
    assert counts["THEFT"] == 1
    assert counts["BATTERY"] == 1

def test_search_success(sample_df):
    count = search_crime_by_type_and_location(sample_df, "THEFT", "STREET")
    assert count == 1

def test_search_invalid_crime(sample_df):
    with pytest.raises(ValueError) as e:
        search_crime_by_type_and_location(sample_df, "HACKING", "STREET")
    assert "Crime type 'HACKING' not found" in str(e.value)

def test_search_invalid_location(sample_df):
    with pytest.raises(ValueError) as e:
        search_crime_by_type_and_location(sample_df, "THEFT", "MOONBASE")
    assert "Location 'MOONBASE' not found" in str(e.value)

