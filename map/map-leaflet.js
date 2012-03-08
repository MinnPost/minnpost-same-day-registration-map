var map;
var interaction;
var geocoder = new google.maps.Geocoder();
var marker;

$(document).ready(function() {
    wax.tilejson('../same_day_registration_interaction.json',
    function(tilejson) {
        map = new L.Map('map-div')
            .addLayer(new wax.leaf.connector(tilejson))
            .setView(new L.LatLng(46.3, -94.2), 7);
            //.setMaxBounds(new L.LatLngBounds(new L.LatLng(-97.7124, 43.125), new L.LatLng(-89.165, 49.5466)));
        interaction = wax.leaf.interaction(map, tilejson);
    });
    $("#redist_search").submit(function(){geocode($("#redist_query").val());return false;});
});


function geocode(query) {
    if (typeof(query) == 'string') {
        pattr = /\smn\s|\sminnesota\s/gi;
        match = query.match(pattr);
        if (!match) {
            query = query + ' MN';
        }
        gr = { 'address': query };
    } else {
        gr = { 'location': query };
    }
    geocoder.geocode(gr, handle_geocode);
}
 
function handle_geocode(results, status) {
    lat = results[0].geometry.location.lat();
    lng = results[0].geometry.location.lng();
    
    normalized_address = results[0].formatted_address;
    $('#redist_query').val(normalized_address)

	var point = new L.LatLng(lat, lng);
	arker = new L.Marker(point);
	map.addLayer(marker);
	map.setView(point, 12);
}
