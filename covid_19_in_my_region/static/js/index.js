window.addEventListener('load', fetchCounties);

function fetchCounties() {

}

function request_data() {
  TESTER = document.getElementById('tester');
  Plotly.newPlot( TESTER, [{
    x: [1, 2, 3, 4, 5],
    y: [1, 2, 4, 8, 16] }], {
      margin: { t: 0 }
    }
  );
}
