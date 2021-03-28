def YearSongsDF(DF):

    # import dependencies
    import pandas as pd
    
    # Create dataframe of year and number of songs released
    year_songs_df = DF.groupby(['Year'])['Song'].count().reset_index()
    year_songs_df['Year'] = year_songs_df['Year'].astype(int)
    
    return year_songs_df