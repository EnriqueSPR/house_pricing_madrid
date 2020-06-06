
function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for (var i in uiBathrooms) {
        if (uiBathrooms[i].checked) {
            return parseInt(i) + 1;
        }
    }
    return -1; // Invalid Value
}

function getRoomsValue() {
    var uiRooms = document.getElementsByName("uiRooms");
    for (var i in uiRooms) {
        if (uiRooms[i].checked) {
            return parseInt(i) + 1;
        }
    }
    return -1; // Invalid Value
}


function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var mt_built = document.getElementById("uisq_mt_built");
    var rooms = getRoomsValue();
    var bathrooms = getBathroomsValue();
    var loc = document.getElementById("uiLocations");
    var estPrice = document.getElementById("uiEstimatedPrice");

    var url = "http://127.0.0.1:5000/predict_home_price"; // Use this if you are NOT using nginx which is first 7 tutorials
    //var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

    $.post(url, {
        sq_mt_built: mt_built.value,
        location: loc.value,
        n_rooms: rooms,
        n_bathrooms: bathrooms
    }, function (data, status) {
        console.log(data.EstimatedPrice);
        estPrice.innerHTML = "<h2>" + data.EstimatedPrice.toString() + " Euros</h2>";
        console.log(status);
    });
}

function onPageLoad() {
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url, function (data, status) {
        console.log("got response for get_location_names request");
        if (data) {
            var locations = data.locations;
            // var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for (var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
}

window.onload = onPageLoad;