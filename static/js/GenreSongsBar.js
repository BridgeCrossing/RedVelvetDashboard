// Read json data
var url = '/GenreSongsBar';
Plotly.d3.json(url, function(response) {

    console.log(response)

    response.sort((a, b) => {
        return b.Song - a.Song;
    });

    var genreArray = []
    var songsArray = []

    for (var i = 0; i < 5; i++) {
        genreArray.push(response[i].Genre)
        songsArray.push(response[i].Song)
    };

    var trace = {
        x: genreArray,
        y: songsArray,
        type: 'bar',
        marker: {
            color: ['rgb(220, 28, 19)', 'rgb(234, 76, 70)', 'rgb(240, 116, 112)',
                    'rgb(241, 149, 155)', 'rgb(246, 189, 192)']
        }
    };

    var data = [trace]

    var layout = {
        title: 'Top 5: Number of Songs by Genre',
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

    Plotly.newPlot('genreBars', data, layout);

}); 