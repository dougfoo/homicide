/*
  initialize Map function -- stored as blob
        <script type="text/javascript" src="https://homicidestorage.z13.web.core.windows.net/homicide.js"></script>
 */

function initializeMap(addresses, zoom) {
    geocoder = new google.maps.Geocoder();
    var latlng = new google.maps.LatLng(35.2251855,-80.8415298);
    var myOptions = {
        zoom: zoom,
        center: latlng,
        mapTypeControl: true,
        mapTypeControlOptions: {
            style: google.maps.MapTypeControlStyle.DROPDOWN_MENU
        },
        navigationControl: true,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
            
    map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
    var i=0;
    addresses.forEach(function(add,i) { 
        console.log('addrs:', add.street);
        setTimeout(function(){
        geocoder.geocode({
            'address': add.street
            }, function(results, status) {
                if (status == google.maps.GeocoderStatus.OK) {
                    if (status != google.maps.GeocoderStatus.ZERO_RESULTS) {
                        console.log('results: ', results[0].geometry.location);
                        var marker = new google.maps.Marker({
                            position: results[0].geometry.location,
                            map: map,
                            icon: 'https://homicidestorage.z13.web.core.windows.net/icons8-skull-crossbones-48.png',
                            title: results[0].formatted_address + ', ' +add.date,
                        });
                        var infowindow = new google.maps.InfoWindow({
                            content: '<div id="info">'+results[0].formatted_address + '<br>Homicide on: '+add.date+'</div>',
                            size: new google.maps.Size(150, 50)
                        });
                        marker.addListener('click', function() {
                            map.setZoom(14);
                            map.setCenter(marker.getPosition());
                            infowindow.open(map, marker);
                        });
                    } else {
                        console.log("No results found for: " + addresses[i]);
                    }
                } else {
                    console.log("Geocode was not successful for the following reason: " + status);
                }
            });
        }, Math.floor(500*i++));
    });
}
