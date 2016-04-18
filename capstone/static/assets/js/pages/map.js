/**
 * Created by Yiming on 3/27/2016.
 */

var mapStyle = [{
    "featureType": "landscape",
    "stylers": [{"hue": "#FFBB00"}, {"saturation": 43.400000000000006}, {"lightness": 37.599999999999994}, {"gamma": 1}]
}, {
    "featureType": "road.highway",
    "stylers": [{"hue": "#FFC200"}, {"saturation": -61.8}, {"lightness": 45.599999999999994}, {"gamma": 1}]
}, {
    "featureType": "road.arterial",
    "stylers": [{"hue": "#FF0300"}, {"saturation": -100}, {"lightness": 51.19999999999999}, {"gamma": 1}]
}, {
    "featureType": "road.local",
    "stylers": [{"hue": "#FF0300"}, {"saturation": -100}, {"lightness": 52}, {"gamma": 1}]
}, {
    "featureType": "water",
    "stylers": [{"hue": "#0078FF"}, {"saturation": -13.200000000000003}, {"lightness": 2.4000000000000057}, {"gamma": 1}]
}, {
    "featureType": "poi",
    "stylers": [{"hue": "#00FF6A"}, {"saturation": -1.0989010989011234}, {"lightness": 11.200000000000017}, {"gamma": 1}]
}];
/********** MAP WITH INFOBOXES **********/

var usLat=39.952584
var usLng=-75.165222
function offersMapInit(id, locations) {
    var mapOptions = {
        zoom: 12,
        disableDefaultUI: false,
        mapTypeControl: true,
        mapTypeControlOptions: {
            position: google.maps.ControlPosition.LEFT_TOP
        },
        zoomControl: true,
        zoomControlOptions: {
            position: google.maps.ControlPosition.RIGHT_CENTER
        },
        scaleControl: true,
        streetViewControl: true,
        streetViewControlOptions: {
            position: google.maps.ControlPosition.RIGHT_CENTER
        },
        scrollwheel: true,
        center: new google.maps.LatLng(usLat,usLng),
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        styles: mapStyle
    };
    var mapElement = document.getElementById(id);

    var map = new google.maps.Map(mapElement, mapOptions);
    var LatLngList = [];
    var i = 0;
    var mapMarkers = [];
    for (i = 0; i < locations.length; i++) {
        var pos = new google.maps.LatLng(locations[i].lat, locations[i].lng);
        var marker = new google.maps.Marker({
            position: pos,
            map: map,
            title: '',
            icon: '/static/assets/images/map-pin.png'
        });

        mapMarkers[i] = marker;

        mapMarkers[i].infobox = new google.maps.InfoWindow({
			content: locations[i].crn
		});
        google.maps.event.addListener(marker, 'click', (function (marker, i) {
            return function () {
                var j = 0;
                for (j = 0; j < mapMarkers.length; j++) {
                    mapMarkers[j].infobox.close();
                }
                mapMarkers[i].infobox.open(map, this);
            }
        })(marker, i));
        LatLngList[i] = pos;
    }


    var markerClusterStyle = [
        {
        textColor: 'black',
        url: '/static/assets/images/m1.png',
        height: 50,
        width: 50
        },
        {
        textColor: 'black',
        url: '/static/assets/images/m2.png',
        height: 60,
        width: 60
        },
        {
        textColor: 'black',
        url: '/static/assets/images/m3.png',
        height: 70,
        width: 70
        }];
    var markerCluster = new MarkerClusterer(map, mapMarkers, {styles: markerClusterStyle});
    var minClusterZoom = 12;
    markerCluster.setMaxZoom(minClusterZoom);

    var oms = new OverlappingMarkerSpiderfier(map, {
        markersWontMove: true,
        markersWontHide: true,
        keepSpiderfied: true,
        legWeight: 2
    });

    for (var i = 0; i < mapMarkers.length; i++) {
        oms.addMarker(mapMarkers[i]);  // <-- here
    }
}
