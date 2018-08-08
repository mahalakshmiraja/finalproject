document.addEventListener('DOMContentLoaded', () => {
    console.log("Entered JS!!!!!!!!")

var date = new Date();
var hrs = date.getHours();
var min = date.getMinutes();
let time = hrs+":"+min
// document.querySelector('#myTime').innerHTML = date;
document.querySelector('#myCalendar').innerHTML = date;

});