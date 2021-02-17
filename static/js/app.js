d3.json('/data').then(function (myData) {

    // console.log(myData);

    let myTraces = Object.entries(myData).map(function(item) {

        return({
            x: [item[1].min_temp],
            y: [item[1].max_temp],
            marker: {
                size:[item[1].max_temp * .5 ]
            },
            name: item[1].city,
            mode:'markers'
        });
    })

    var layout = {
        autosize: true,
        paper_bgcolor: '#fcecc0',
        plot_bgcolor: '##fcfcfa'
      };

    var data = myTraces;

    Plotly.newPlot('myDiv', data, layout);

    // make my plots with that data
})