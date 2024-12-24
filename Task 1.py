
'''Create a histogram to visualize the distribution of a categorical or continuous variable, such as the#-
 distribution of ages or genders in a population. from a excel file with name "API_SP.POP.TOTL_DS2_en_excel_v2_9.xls"#-
 tables with column names Country Name,	Country Code,	Indicator Name	,Indicator Code,	1960	,1961,	1962,	1963	,1964	#-
 1965,	1966,	1967	,1968,	1969,	1970,	1971,	1972,	19āāāā3,	1974,	1975,	1976,	1977,	1978,	1979,#-
    	1980	1981	1982	1983	1984	1985	1986	1987	1988	1989	1990	1991	1992	1993	#-
        1994	1995	1996	1997	1998	1999	2000	2001	2002	2003	2004	2005	2006	2007	2008	2009	2010	2011	2012	2013	2014	2015	2016	2017	2018	2019	2020	2021	2022	2023#-
'''#-
import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file and skip the first 4 rows
data = pd.read_excel("C:\\Users\\Sri Nithilan\\Downloads\\API_SP.POP.TOTL_DS2_en_excel_v2_9.xls", skiprows=4)

# Get the column names from the first row
column_names = data.columns.tolist()

# Get the column names for 'Country Name', 'Indicator Name', and the last year (2020)
required_columns = [column_names[0], column_names[2], column_names[-1]]

# Filter the DataFrame using the required columns
filtered_data = data[required_columns]

# Rename the columns to 'country', 'indicator', and 'population'
filtered_data.columns = ['country', 'indicator', 'population']

# Drop any rows with missing values
filtered_data = filtered_data.dropna()

# Create a histogram of the population column
filtered_data['population'].hist(bins=100)

# Display the histogram
plt.show()