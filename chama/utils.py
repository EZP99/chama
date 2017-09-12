"""
The utils module contains a collection of utility functions.
"""


def _scalar_or_list_to_list(data):
        if isinstance(data, list):
            return [i for i in data]
        else:
            return [data]


def df_columns_required(df_name, df, col_type_dict):
    """ 
    Internal function that raises an exception if DataFrame does not 
    contain the expected columns with expected types
    """
    for k,v in col_type_dict.items():
        if not df_columns_exist(df, {k:v}):
            raise TypeError('Expected column "{0}" of type {1} in DataFrame \
                            "{2}."'.format(k, v, df_name))


def df_columns_exist(df, col_type_dict):
    """ 
    Internal function that returns False if a column in the DataFrame does
    not exist or is not of the expected type
    """
    for name, dtypes in col_type_dict.items():
        if name not in df:
            return False

        new_dtypes = _scalar_or_list_to_list(dtypes)
        if df[name].dtype not in new_dtypes:
            return False

    return True


def df_nans_not_allowed(df_name, df):
    """ 
    Internal function that raises an exception if a user passed a DataFrame 
    with NANs when not allowed.
    """
    if df.isnull().values.any():
        raise TypeError('Found unexpected NaN values in DataFrame "{0}"\
                        .'.format(df_name))


def df_columns_nans_not_allowed(df_name, df, col_list):
    """ 
    Internal function that raises an exception if user passed in a DataFrame 
    with NANs in a particular column (where col names are in col_list)
    """
    new_col_list = _scalar_or_list_to_list(col_list)
    for name in new_col_list:
        if df_columns_has_nans(df, [name]):
            raise TypeError('Found unexpected NaN values in column "{0}" of \
                            DataFrame "{1}".'.format(name, df_name))


def df_columns_has_nans(df, col_list):
    """ 
    Internal function that returns true if a column in col_list has NANs
    """
    new_col_list = _scalar_or_list_to_list(col_list)
    for name in new_col_list:
        if name not in df.keys():
            raise TypeError('Test for NAN in column %s that does not exist in \
                            DataFrame' % (name))
        if df[name].isnull().values.any():
            return True
    
    return False
