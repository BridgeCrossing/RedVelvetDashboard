def CreateSongGenreDF(DF):

    # import dependencies
    import pandas as pd

    # Create dataframe of Song and all its genres
    song_name_list = []
    single_genre_list = []
    for i, row in DF.iterrows():
        song = row[0]
        genre = row[5]
        
        genre_split = genre.split(', ')
        genre_split_list_length = len(genre_split)
        
        for i in range(genre_split_list_length):
            song_name_list.append(song)
            single_genre_list.append(genre_split[i])
    
    song_genre_df = pd.DataFrame({'Song': song_name_list, 'Genre': single_genre_list})

    # Clean genre column
    genre_clean_list = []
    for i, row in song_genre_df.iterrows():
        genre = row[1]
        genre_cap = genre.upper()
        genre_nodash = genre_cap.replace('-', ' ')
        
        if genre_nodash in ['ELECTRO POP', 'ELECTROPOP']:
            genre_clean = 'ELECTRO POP'
        elif genre_nodash == 'EUROPOP':
            genre_clean = 'EURO POP'
        elif genre_nodash in ['POP PUNK', 'PUNK POP']:
            genre_clean = 'PUNK POP'
        elif genre_nodash in ['TROPICAL', 'TROPICAL HOUSE']:
            genre_clean = 'TROPICAL HOUSE'
        elif genre_nodash in ['CHIP MUSIC', 'CHIP TUNE']:
            genre_clean = 'CHIP MUSIC'
        elif genre_nodash == 'ELECTROPOP':
            genre_clean = 'ELECTRO POP'
        elif genre_nodash == 'POP FUNK':
            genre_clean = 'FUNK POP'
        else:
            genre_clean = genre_nodash
        
        genre_clean_list.append(genre_clean)
        
    song_genre_df['Genre'] = genre_clean_list

    genre_song_counter_df = song_genre_df[song_genre_df['Genre'] != 'NO LISTED GENRE'].groupby('Genre')['Song'].count().reset_index()

    return genre_song_counter_df