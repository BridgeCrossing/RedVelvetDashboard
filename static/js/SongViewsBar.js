// Read json data
var url = '/SongViewsBar';
Plotly.d3.json(url, function(response) {

    response.sort((a, b) => {
        return a.Views - b.Views;
    });

    console.log(response)

    var songArray = []
    var viewsArray = []

    for (var i = 0; i < response.length; i++) {
        songArray.push(response[i].Song)
        viewsArray.push(response[i].Views)
    };

    var trace = {
        x: viewsArray,
        y: songArray,
        type: 'bar',
        orientation: 'h',
        marker: {
            color: ['rgb(255, 230, 230)', 'rgb(255, 204, 204)', 'rgb(255, 179, 179)', 'rgb(255, 153, 153)', 'rgb(255, 128, 128)',
                    'rgb(255, 102, 102)', 'rgb(255, 77, 77)', 'rgb(255, 51, 51)', 'rgb(255, 25, 25)', 'rgb(255, 0, 0)']
        }
    };

    var data = [trace]

    var layout = {
        title: 'Top 10 Songs Viewed on YouTube',
        xaxis: {
            zeroline: false,
            showline: true,
            showgrid: false
          },
          yaxis: {
            zeroline: false,
            showline: true,
            showgrid: false,
            automargin: true
          },
          plot_bgcolor: "rgba(231,154,142, .000005)",
          paper_bgcolor: "rgba(231,154,142, .000005)"
    };

    Plotly.newPlot('viewBars', data, layout);

}); 