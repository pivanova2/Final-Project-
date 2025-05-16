from analysis import (
    load_and_filter_data,
    get_crime_type_counts,
    get_top_crime_locations,
    get_arrests_by_month,
    get_top_wards,
    plot_crime_type_counts,
    search_crime_by_type_and_location  # NEW
)


def main():
    # Path to the CSV data file
    path = "Crimes_-_2001_to_Present_20250513.csv"

    # Load and filter the data for non-domestic arrests only
    df = load_and_filter_data(path)

    # Intro message about the dataset
    print("="*70)
    print("Chicago Crime Analyzer")
    print("This dataset includes NON-DOMESTIC ARRESTS from the past year.")
    print("It covers crimes such as:")
    print("- Weapons violations, theft, assault, criminal damage, trespass,")
    print("  robbery, burglary, motor vehicle theft, sex offenses, homicide,")
    print("  arson, sexual assault, stalking, and kidnapping.")
    print("="*70)

    # Main menu loop
    while True:
        # Display menu options
        print("\n--- Menu ---")
        print("1. Show number of each crime type")
        print("2. Show top 10 crime locations")
        print("3. Show arrests by month")
        print("4. Show top 5 wards with most arrests")
        print("5. Plot crime types bar graph")
        print("6. Search for a crime type in a location")
        print("7. Exit")

        # Get user's choice
        choice = input("Enter your choice: ")

        # Option 1: Count of each crime type
        if choice == "1":
            print("\nCrime Type Counts:\n")
            print(get_crime_type_counts(df).to_string())

        # Option 2: Top 10 locations with most crimes
        elif choice == "2":
            print("\nTop 10 Crime Locations:\n")
            print(get_top_crime_locations(df).to_string())

        # Option 3: Number of arrests by month
        elif choice == "3":
            print("\nArrests by Month:\n")
            print(get_arrests_by_month(df).to_string())

        # Option 4: Top 5 wards with most arrests
        elif choice == "4":
            print("\nTop 5 Wards with Most Arrests:\n")
            print(get_top_wards(df).to_string())

        # Option 5: Display a bar graph of crime types
        elif choice == "5":
            plot_crime_type_counts(df)

        # Option 6: Search for specific crime type at a location
        elif choice == "6":
            crime = input("Enter crime type (e.g., THEFT, BATTERY): ")
            location = input("Enter location (e.g., STREET, GAS STATION): ")
            try:
                count = search_crime_by_type_and_location(df, crime, location)
                print(f"\nFound {count} cases of '{crime.upper()}' at '{location.upper()}'.")
            except ValueError as e:
                print(e)

        # Option 7: Exit program
        elif choice == "7":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()