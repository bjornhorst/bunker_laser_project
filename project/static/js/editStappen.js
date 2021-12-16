//set default value to 0
var stappenX = 0;
var stappenY = 0;

var stappenXObject = {
    "stappenX": []
};
var stappenYArray = [];

function getX_Links() {
    $.get('/motor/call/m1/links', function (data) {
        console.log(data)
        stappenX -= 1;
        document.getElementById("stappenX").innerHTML = stappenX;
    });
}

function getX_Rechts() {
    $.get('/motor/call/m1/rechts', function (data) {
        console.log(data)
        stappenX += 1;
        document.getElementById("stappenX").innerHTML = stappenX;
    });
}

function getY_Links() {
    $.get('/motor/call/m2/links', function (data) {
        console.log(data)
        stappenY -= 1;
        document.getElementById("stappenY").innerHTML = stappenY;
    });
}

function getY_Rechts() {
    $.get('/motor/call/m2/rechts', function (data) {
        console.log(data)
        stappenY += 1;
        document.getElementById("stappenY").innerHTML = stappenY;
    });
}

document.onkeydown = checkKey;

function checkKey(e) {

    e = e || window.event;

    if (e.keyCode == '38') {
        // up arrow
        getY_Links();
    } else if (e.keyCode == '40') {
        // down arrow
        getY_Rechts();
    } else if (e.keyCode == '37') {
        // left arrow
        getX_Links();
    } else if (e.keyCode == '39') {
        // right arrow
        getX_Rechts()
    }

}

function updateStappenListX(stappen) {
    if (stappenX <= 0) {
        var markup = "<tr><td>MoterX Links</td><td>" + stappenX + "</td></tr>";
        stappenXObject.stappenX.push(stappenX);
        console.log(stappenXObject);
    } else {
        var markup = "<tr><td>MoterX rechts</td><td>" + stappenX + "</td></tr>";
    }

    $("#videoStappenTableX>tbody").append(markup);
    // console.log(stappen)
}

function updateStappenListY(stappen) {
    if (stappenY <= 0) {
        var markup = "<tr><td>MoterY Links</td><td>" + stappenY + "</td></tr>";
    } else {
        var markup = "<tr><td>MoterY rechts</td><td>" + stappenY + "</td></tr>";
    }

    $("#videoStappenTableY>tbody").append(markup);
    // console.log(stappen)
}