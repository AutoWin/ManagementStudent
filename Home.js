$(document).ready(function () {
    $.ajax({
        url: "http://api.openweathermap.org/data/2.5/weather?q=Vietnam&APPID=5a3ce50c1b636d1ef7db2529bf088d21",
        dataType: 'json',
        success: function (data) {
            var element = document.getElementById("weather");
            var para = document.createElement("p");
            var node = para.createTextNode("Temperature is: " + (data.main.temp - 273).toString().substr(0, 4) + " C");
            element.appendChild(para);
        },
        error: function () {
            alert("error");
        }
    });
});