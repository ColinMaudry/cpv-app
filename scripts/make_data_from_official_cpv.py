import pandas as pd

df: pd.DataFrame = pd.read_csv('../data/cpv_2008.csv')

def getParent(code: str) -> str:
    """
    Returns the parent CPV code of a given CPV code
    :param code: The code for which we retrieve the parent
    :return:
    """

    # 12345600-3
    codeRoot = code[:-2]
    # => 12345600

    codeBase = codeRoot.rstrip('0')
    # => 123456

    parentCodeBase = codeBase[:-1].ljust(8, '0')
    # => 12345000

    # Search in the df another code that starts with 12345000 (without '-[0-9]')
    parentCodeRow: pd.DataFrame = df.loc[df['CODE'].str.startswith(parentCodeBase)].values

    # If the code exists
    if len(parentCodeRow) > 0:
        return parentCodeRow[0][0]
    # Otherwise
    else:
        return ''


df['parent'] = df['CODE'].apply(getParent)
df.rename(columns = {'CODE': 'id', 'FR': 'name'}, inplace= True)
df.to_csv('../data/cpv_2008_parent.csv')
