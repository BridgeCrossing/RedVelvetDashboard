############## Update Red Velvet CSV Datasets in Github ######################

# import dependencies
import pandas as pd
from bs4 import BeautifulSoup
import requests

# import python functions
from WebScrapeWikiFandom import WebScrapeWikiFandom
from SongGenre import CreateSongGenreDF
from YearSongs import YearSongsDF
from ArtistSongs import ArtistSongsDF
from YouTubeWebScrape import SongViewsDF

# Web scrape wiki fandom site
WikiFandom_URL = "https://redvelvet.fandom.com/wiki/List_of_songs_by_Red_Velvet"
RV_DF = WebScrapeWikiFandom(WikiFandom_URL)

# Create dataframe of year and number of songs released
Year_Songs_DF = YearSongsDF(RV_DF)
Year_Songs_DF.to_csv('../Datasets/RedVelvet_YearSongs.csv', index = False)

# Create dataframe of song and all its genres (repeat song row if have multiple genres)
Song_Genre_DF = CreateSongGenreDF(RV_DF)
Song_Genre_DF.to_csv('../Datasets/RedVelvet_SongGenreCount.csv', index = False)

# Create dataframe of artist and number of songs she has
Artist_SongCounter_DF= ArtistSongsDF(RV_DF)
Artist_SongCounter_DF.to_csv('../Datasets/RedVelvet_SongCount.csv', index = False)

# Create dataframe of song and YouTube views
Playlist_URL = 'https://www.youtube.com/c/redvelvet/playlists?view=71&shelf_id=4'
SongViews_DF = SongViewsDF(Playlist_URL)
SongViews_DF.to_csv('../Datasets/RedVelvet_YouTubeSongViews.csv', index = False)