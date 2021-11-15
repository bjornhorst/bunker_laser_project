 // load video object
        var video = videojs('example_video_1');
        //load markers
        video.markers({
            markers: [
                {
                    time: 0,
                    text: "begin",
                    class: 'hide-marker'
                },
            ]
        });

        function addMarkerLaserOn() {
            console.log("current time = " + video.currentTime);
            video.markers.add([{
                time: video.currentTime(),
                text: "ON",
            }]);
            updateMarkerList();
        }

        function addMarkerLaserOff() {
            console.log("current time = " + video.currentTime);
            video.markers.add([{
                time: video.currentTime(),
                text: "OFF",
                class: 'custom-marker1'
            }]);
            updateMarkerList();
        }

        function updateMarkerList() {
            var vidList = video.markers.getMarkers();
            markerId = 1
            $("#videdPuntenTable").html("");
            var button = "<button onclick='removeMarker(" + markerId + ")'>verwijderen</button>";
            var markerTable = $("<table>").addClass("tbl_sm");
            var tr = $("<tr>")  // maak header row met td's aan
                .append($("<th>").html("Tijd"))
                .append($("<th>").html("aan of uit"))
                .append($("<th>").html("Verwijder"));
            markerTable.append(tr);
            $(vidList).each(function (key, marker) {
                //console.log( beer );
                if (key != 0) {
                    var tr = $("<tr>")  // maak header row met td's aan
                        .append($("<td>").html(marker.time))
                        .append($("<td>").html(marker.text))
                        .append($("<td><button onclick='removeMarker(" + markerId + ")'>verwijderen</button>"))
                        .append($("<td>").html(markerId));
                    markerTable.append(tr);
                    markerId = markerId + 1;
                }
            });
            $("#videdPuntenTable").append(markerTable);
        }

        function removeMarker(id) {
            if (id != 0) {
                video.markers.remove([id]);
            }
            updateMarkerList();
        }

        function saveMarkers() {
            var proceed = confirm("Weet je zeker dat je alle punten hebt toegevoegd?");
            if (proceed) {
                //proceed
                jsonObj = [];
                var markerarray = video.markers.getMarkers();
                $(markerarray).each(function (key, marker) {
                    timeMarks = {};
                    timeMarks["time"] = marker["time"];
                    timeMarks["laserOnOff"] = marker["text"];
                    console.log(marker["time"]);
                    console.log(marker['text']);
                    jsonObj.push(timeMarks);
                });
                console.log(jsonObj);
                $.ajax({
                    type: 'get',
                    url: '/admin/video/{{ id }}/punten/edit/',
                    dataType: 'json',
                    data:jsonObj,
                    success: function (dataAJAX) {
                        location.reload();
                        // or click related .related-products-control
                    }
                });
            } else {
                //don't proceed
            }

        }