function request_data() {
  var sel = document.getElementById('county-select').value;
  console.log(sel);

  fetch('/fetch_data?region=' + sel, {
  method: 'GET',
  headers:{
    'Content-Type': 'application/json'
  }
  }).then(function(response){
    response.json().then(function(data){
      TESTER = document.getElementById('tester');
      Plotly.newPlot( TESTER, [{
        x: [1, 2, 3, 4, 5],
        y: [1, 2, 4, 8, 16] }], {
          margin: { t: 0 }
        }
      );
    })
  })

}
