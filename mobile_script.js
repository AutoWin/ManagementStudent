function myFunction() {
    var x = document.getElementById("myLinks");
    if (x.style.display === "block") {
        x.style.display = "none";
    } else {
        x.style.display = "block";
    }
}

if (document.documentElement.clientWidth < 900) {
    window.location = "student_mobile.html";
}

if (screen.width < 900) {
    window.location = "student.html";
}