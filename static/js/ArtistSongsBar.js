// Read json data
var url = '/ArtistSongsBar';
Plotly.d3.json(url, function(response) {

    response.sort((a, b) => {
        return b.Songs - a.Songs;
    });

    var artistArray = []
    var songsArray = []
    var colorsArray = []

    for (var i = 0; i < response.length; i++) {
        artistArray.push(response[i].Artist)
        songsArray.push(response[i].Songs)
        colorsArray.push(response[i].Color)
    };

    var trace = {
        x: artistArray,
        y: songsArray,
        type: 'bar',
        marker: {
          color: colorsArray
        }
    };

    var data = [trace]

    var layout = {
        title: 'Number of Songs by Each Member Outside the Group',
        xaxis: {
            zeroline: false,
            showline: true,
            showgrid: false
          },
          yaxis: {
            zeroline: false,
            showline: true,
            showgrid: false
          },
          plot_bgcolor: "rgba(231,154,142, .000005)",
          paper_bgcolor: "rgba(231,154,142, .000005)"
    };

    Plotly.newPlot('artistBars', data, layout);

}); 