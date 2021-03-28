############################################### Red Velvet Dashboard #########################################

# import dependencies
import pandas as pd
from flask import Flask, jsonify, render_template

#################### Set up dashboard app #######################
app = Flask(__name__)

# Create dictionary of year and number of songs released
Year_Songs_DF = pd.read_csv('https://raw.githubusercontent.com/dFeelz/RedVelvetDashboard/master/Datasets/RedVelvet_YearSongs.csv')
Year_Songs_Dict = Year_Songs_DF.to_dict('records')

# Create dictionary of song and all its genres (repeat song row if have multiple genres)
Song_Genre_DF = pd.read_csv('https://raw.githubusercontent.com/dFeelz/RedVelvetDashboard/master/Datasets/RedVelvet_SongGenreCount.csv')
Song_Genre_Dict = Song_Genre_DF.to_dict('records')

# Create dictionary of artist and number of songs she has
Artist_SongCounter_DF= pd.read_csv('https://raw.githubusercontent.com/dFeelz/RedVelvetDashboard/master/Datasets/RedVelvet_SongCount.csv')
Artist_SongCounter_Dict = Artist_SongCounter_DF.to_dict('records')

# Create dictionary of song and YouTube views
SongViews_DF = pd.read_csv('https://raw.githubusercontent.com/dFeelz/RedVelvetDashboard/master/Datasets/RedVelvet_YouTubeSongViews.csv')
SongViews_DF = SongViews_DF.sort_values(by = ['Views'])
SongViews_Top10 = SongViews_DF.tail(10)
SongViews_Top10['Song'] = SongViews_Top10['Song'].str.replace("Red Velvet 레드벨벳 '", "")
SongViews_Top10['Song'] = SongViews_Top10['Song'].str.replace("' MV", "")
print(SongViews_Top10)
SongViews_Dict = SongViews_Top10.to_dict('records')

#################### Set up routes #########################
@app.route("/")
def index():
    """Return the home page."""
    return render_template("index.html")

@app.route("/LineChart")
def YearSongLineChart():
    """Return year and number of songs released for line chart."""
    return(jsonify(Year_Songs_Dict))

@app.route("/ArtistSongsBar")
def ArtistSongsBarGraph():
    """Return artist name and number of songs she has outside of group for bar graph."""
    return(jsonify(Artist_SongCounter_Dict))

@app.route("/GenreSongsBar")
def GenreSongsBarGraph():
    """Return genre and number of songs for bar graph."""
    return(jsonify(Song_Genre_Dict))

@app.route("/SongViewsBar")
def SongViewsBarGraph():
    """Return songs and YouTube views for bar graph."""
    return(jsonify(SongViews_Dict))

if __name__ == "__main__":
    app.debug = True
    app.run()