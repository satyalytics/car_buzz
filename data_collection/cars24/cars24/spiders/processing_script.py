import pandas as pandas
import numpy as np

path = ""

df = pd.read_csv(path)


def get_list(x):
    """
        Extract data from fuel and create a list from string, splitting by (,). It can work with cells from fuel,
        location, model, owner, and url columns.
        
        Args:
            a comma separated string.
        Return:
            A list from the argument.
    """
    x = x.split(',')
    return x


def get_km(x):
    """
        Extract the km drove. 
        
        Args:
            A string, more likely an element from the km_drove
        Returns:
            A list of elements
    """
    x = x.replace(',','') # as there is comma inside number also
    x = x.lower().strip('km')
    x = x.split('km')
    return x


def get_price(x):
    
    """
        Converts price string into price list.
        
        Args:
            string, more preferably from price column
        Returns:
            A list of prices
    """
    x = x.replace('\n','')
    x = x.replace(' ','')
    x = x.replace(',,','A')
    x = x.replace(',','')
    x = x.split('A')
    return x


def convert_list(df):
	"""
		Convert from string element to list
		Args:
			df: Dataframe, of which columns will be converted.
		Return:
			df2: df, elements are in the list form
	"""
	df2 = pd.DataFrame()
	for i in df:
		if i == 'price':
			df2[i] = df[i].apply(get_price)
		elif i == 'km_drove':
			df2[i] = df[i].apply(get_km)
		else:
			df2[i] = df[i].apply(get_list)
	return df2


def get_len(conv_df):

	"""
		create a dataframe of numbers, those numbers are the length of the lists in converted list
		Args:
			conv_df: The dataframe, which cells are lists of items.
		Returns:
			num_df: dataframe of numbers which are mostly length of the lists present at cell level
	"""

	num_df = pd.DataFrame()
	for i in conv_df:
		num_df[i] = conv_df[i].apply(len)
	return num_df

def get_mode(num_df):
	"""
		Get the mode of all the lengths present in the num_df
	"""
	pass