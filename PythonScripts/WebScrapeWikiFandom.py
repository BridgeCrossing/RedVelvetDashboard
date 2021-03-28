def WebScrapeWikiFandom(url):

    # import dependencies
    import pandas as pd
    from bs4 import BeautifulSoup
    import requests

    ################# Web Scrape Red Velvet Wiki Fandom Song List Page #################

    # scrape raw data
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('td')

    # extract text from raw data
    text_list = []
    for result in results:
        text = result.text
        text_list.append(text)

    # clean text 
    text_clean_list = []
    for text in text_list:
        clean_text = text.rstrip('\n').lstrip('\n')
        text_clean_list.append(clean_text)

    # extract song data from text
    songs = text_clean_list[::4]
    albumns = text_clean_list[1:len(text_clean_list)][::4]
    artists = text_clean_list[2:len(text_clean_list)][::4]
    year = text_clean_list[3:len(text_clean_list)][::4]

    # create dataframe of song information
    df = pd.DataFrame({'Song': songs, 'Album': albumns, 'Artist': artists, 'Year': year})

    # clean album data
    df['Album'] = df['Album'].fillna('No Album')

    album_clean_list = []
    for i, row in df.iterrows():
        album = row[1]
        
        if album in ('', '-'):
            album_clean = 'No Album'
        else:
            album_clean = album
        album_clean_list.append(album_clean)
        
    df['Album'] = album_clean_list 

    # clean artist data
    RV_list = ['Red Velvet', 'Irene', 'Wendy', 'Joy', 'Seulgi', 'Yeri']

    song_list = []
    counter_list = []
    for i, song_row in df.iterrows():
        for name in RV_list:
            
            song = song_row[0]
            artist = song_row[2]
            
            count = 0
            if name in artist:
                count += 1
                
            song_list.append(song)
            counter_list.append(count) 
    
    dummy_df = pd.DataFrame({'Song': song_list, 'Counter': counter_list})
    ArtistCounter_df= dummy_df.groupby('Song')['Counter'].sum().reset_index()
    df2 = pd.merge(df, ArtistCounter_df, on = 'Song', how = 'inner')

    artist_clean_list = []
    for i, row in df2.iterrows():
        artist = row[2]
        counter = row[4]
        
        if artist == '':
            artist_clean = 'Red Velvet'
        elif counter == 0 and artist not in RV_list:
            artist_clean = 'Red Velvet with ' + artist
        else:
            artist_clean = artist
        artist_clean_list.append(artist_clean)

    df2['Artist'] = artist_clean_list

    df3 = df2.drop(columns = 'Counter')


    ############### Web Scrape Individual Red Velvet Song Pages #################

    # scrape raw data for urls
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('td')
    song_link_unclean_list = results[::4]

    # extract song urls from raw data
    song_url_list = []
    for song_link in song_link_unclean_list:
        a_href = song_link.find('a').get('href')

        try:
            song_url = 'https://redvelvet.fandom.com' + a_href
        except TypeError:
            song_url = 'No URL'
        song_url_list.append(song_url)

    df3['Song_URL'] = song_url_list

    # create genre column
    genre_list = []

    for i, row in df3.iterrows():
        song_url = row[4]
        
        if song_url != 'No URL':
            
            response = requests.get(song_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            descriptions = soup.find_all("h3", {"class": "pi-data-label pi-secondary-font"})

            description_list = []
            for description in descriptions:
                description_text = description.text
                description_list.append(description_text)

            if 'Genre' not in description_list:
                genre = 'No Listed Genre'
            else:
                genre_index = description_list.index('Genre')
                song_description_list = []
                song_descriptions = soup.find_all("div", {"class": "pi-data-value pi-font"})
                for song_description in song_descriptions:
                    song_description_text = song_description.text
                    song_description_list.append(song_description_text)

                genre = song_description_list[genre_index]
            
            
        else:
            genre = 'No Listed Genre'

        genre_list.append(genre)
    
    df3['Genre'] = genre_list

    # clean columns
    df3['Year'].loc[df3['Song'] == '미래 (Future)'] = '2020'
    df3['Genre'].loc[df3['Song'] == 'Two Words'] = 'Ballad'
    df3['Genre'].loc[df3['Song'] == 'Dumb Dumb (Japanese Ver.)'] = 'R&B, Funk, Hip-hop, dance pop'
    df3['Artist'].loc[df3['Album'] == 'Monster'] = 'Irene & Seulgi'
    
    return df3