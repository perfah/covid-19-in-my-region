function request_data() {
  var sel = document.getElementById('county-select').value;
  var acc = document.getElementById('acc').checked;


  fetch('/fetch_data?region=' + sel + '&acc='+ acc, {
  method: 'GET',
  headers:{
    'Content-Type': 'application/json'
  }
  }).then(function(response){
    response.json().then(function(data){
      if(data.region == sel && (data.x.length == data.y.length)) {
        graph = document.getElementById('graph');
        Plotly.newPlot( graph, [{
          x: data.x,
          y: data.y ,
          type: 'scatter'
        }]);
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
