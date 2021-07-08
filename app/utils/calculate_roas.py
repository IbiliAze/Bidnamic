def calculate_roas(row):
    '''
    Function will calculate the ROAS and handle exceptions:
        - ROAS = conversion value/ cost

    If the division fails, 0 will be returned.\n

    '''
    # Get informational values
    roas = 'ROAS'
    search_term = row[0]
    clicks = row[5]
    impressions = row[8]
    conv_value = row[10]
    cost = row[7]

    try:
        # Calculate ROAS
        roas = float(conv_value) / float(cost)
    except Exception as ex:
        roas = 'ROAS'

    return [ search_term, clicks, impressions, conv_value, roas ]