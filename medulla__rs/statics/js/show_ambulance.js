let userLocation;

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function (position) {
                userLocation = [
                    position.coords.latitude,
                    position.coords.longitude,
                ];
                console.log("Location coordinates:", userLocation);
                calculateDistance();
                // hideLocationPopup();
            },
            function (error) {
                console.error("Error getting location:", error.message);
                // hideLocationPopup();
            }
        );
    } else {
        console.error("Geolocation is not supported by this browser.");
        // hideLocationPopup();
    }
}

function calculateDistance() {
    if (userLocation) {
        // Example usage
        const distance = calculateDistanceBetween(
            userLocation[0],
            userLocation[1],
            28.4745076,
            77.4800492
        );
        console.log("Distance:", distance.toFixed(2), "km");

        document.getElementById("input2").value = distance.toFixed(2) + " km";
    }
}

function calculateDistanceBetween(lat1, lon1, lat2, lon2) {
    // Radius of the Earth in kilometers
    const R = 6371;

    // Convert latitude and longitude from degrees to radians
    const dLat = (lat2 - lat1) * (Math.PI / 180);
    const dLon = (lon2 - lon1) * (Math.PI / 180);

    // Haversine formula
    const a =
        Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        Math.cos(lat1 * (Math.PI / 180)) *
            Math.cos(lat2 * (Math.PI / 180)) *
            Math.sin(dLon / 2) *
            Math.sin(dLon / 2);

    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    const distance = R * c; // Distance in kilometers

    return distance;
}
