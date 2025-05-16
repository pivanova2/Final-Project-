Project Description:
The Chicago Crime Analyzer is a Python-based command-line application designed to help users analyze patterns in non-domestic arrests in Chicago over the past year. The dataset it works with includes various crime types such as:
Weapons violations


Theft


Assault


Criminal damage


Trespass


Robbery


Burglary


Motor vehicle theft


Sex offenses


Homicide


Arson


Sexual assault


Stalking


Kidnapping


The program presents an interactive menu through which users can explore crime data using multiple options. The main features include:
Show number of each crime type: Displays how many times each crime type occurred.


Show top 10 crime locations: Lists the ten locations in the city with the highest number of crimes.


Show arrests by month: Provides a breakdown of arrests by month to observe trends over time.


Show top 5 wards with most arrests: Identifies which of Chicago's wards had the most arrests.


Plot crime types bar graph: Visualizes the frequency of different crime types using a bar graph.


Search for a crime type in a location: Allows users to look up specific crimes within chosen neighborhoods or areas.


Exit: Closes the program.


This tool is useful for analyzing crime patterns, identifying high-risk areas, and observing changes in criminal activity over time within Chicago.
One challenge I encountered during development was parsing the CSV file containing the crime data. Initially, I ran into issues with inconsistent formatting, missing values, and handling special characters. These problems caused errors when trying to extract and analyze information. I resolved the issue by using Python’s csv and pandas libraries, implementing error handling, and cleaning the data to ensure it could be read and processed correctly.
