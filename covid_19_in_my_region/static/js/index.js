function request_data() {
  var sel = document.getElementById('county-select').value;
  var acc = document.getElementById('acc').checked;

  var config = {responsive: true};


  var layout = {
    autosize: true
  };


  fetch('/fetch_data?region=' + sel, {
  method: 'GET',
  headers:{
    'Content-Type': 'application/json'
  }
  }).then(function(response){
    response.json().then(function(data){
      if(data.region == sel && (data.x.length == data.y.length)) {
        var graph = document.getElementById('graph');
        if(acc) {
          var trace1 = {
            x: data.x,
            y: data.y,
            name: "New Cases",
            type: 'scatter'
          };
          var trace2 = {
            x: data.x,
            y: data.y_acc,
            name: "Accumulated Cases",
            type: 'scatter'
          };
          var data = [trace1, trace2];

          Plotly.newPlot(graph, data, layout, config);
        }
        else {
          Plotly.newPlot( graph, [{
            x: data.x,
            y: data.y ,
            type: 'scatter'
          }], layout, config);
        }
      } else {
        if(data.region != sel) {
          alert("Internal Server Error, Region mismatch")
        }
        else if((data.x.length != data.y.length)) {
          alert("Internal Server Error, Data mismatch")
        }
        else {
          alert("Internal Server Error, Unknown cause")
        }
      }
    })
  })

}
