let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 32.4844, lng: 75.4541 },
    zoom: 8,
  });
}