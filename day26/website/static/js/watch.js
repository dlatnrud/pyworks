// 디지털 시계

setInterval(myWatch, 100)

function myWatch(){
   var date = new Date();
   var now = date.toLocaleTimeString();
   document.getElementById('demo').innerHTML = now;
}