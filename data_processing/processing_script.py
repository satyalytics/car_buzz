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
        Find the mode of the dataframe means length of the most of the lists
        Args: 
            num_df: The numeric dataframe which holds length of the arrays
        Returns:
            mode: Length of most of the elements present in the dataframe, if same for all column
            None: If above condition is not satisfied
    """

    mode_ls = []
    for i in num_df:
        model_ls = mode_ls.append(num_df[i].mode())
    mode = list(set(mode_ls))

    if len(mode) == 1:
        c = mode[0]
    else:
        c = None
    return c


def filter_idx(df):
    """
        filter the index which has less or more elements than rest of the dataframe
        Args:
            df: The dataframe which will be filtered.
        Returns:
            filtered_df: The dataframe has all elements of same length
    """
    # convert the dataframe of string elements into list elements
    conv_df = convert_list(df)
    # create another df to keep count
    count_df = get_len(conv_df)
    # get the mode of the count df
    mode = get_mode(count_df)

    if mode is None:
        print("The raw dataset needs to be visited")
    else:
        fault_idx = []
        for i in count_df:
            ls = count_df[count_df[i]!=mode].index
            fault_idx.extend(ls)

    # drop the faulty indices
    filtered_df = conv_df.drop(fault_idx)
    return filtered_df


def make_df(filtered_df):
    """
        Prepare and return analysis ready dataset
        Args:
            filtered_df: The dataset of elements as lists of equal length
        Return:
            df: The dataframe ready for analysis, a single element in each cell
    """
    dict_d = {}
    for i in full_df:
        dict_d[i] = [j for sub in full_df[i].tolist() for j in sub]
    df = pd.DataFrame(dict_d)
    return df