// Read json data
var url = '/LineChart';
Plotly.d3.json(url, function(response) {

    var yearArray = []
    var songsArray = []

    for (var i = 0; i < response.length; i++) {
        yearArray.push(response[i].Year)
        songsArray.push(response[i].Song)
    };

    var trace = {
        x: yearArray,
        y: songsArray,
        mode: 'lines+markers',
        marker: {
            color: 'rgb(0,0,0)',
            size: 8
          },
          line: {
            color: 'rgb(255,0,0)',
            width: 3
          }
    };

    var data = [trace]

    var layout = {
        title: 'Number of Songs Released Over the Years',
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

    Plotly.newPlot('lineChart', data, layout);



});
    
    