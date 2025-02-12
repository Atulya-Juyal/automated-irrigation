function updateDashboardRow() {
    // Update Temperature, Humidity, and Soil Moisture
    document.getElementById('temperature').textContent = (Math.random() * (38.99 - 18.00) + 18.00).toFixed(2);
    document.getElementById('humidity').textContent = (Math.random() * (81.27 - 38.00) + 38.00).toFixed(2);
    document.getElementById('soil-moisture').textContent = (Math.random() * (984.83 - 314.51) + 314.51).toFixed(2);
    let a = Math.random()
    if (a < 0.5){
        document.getElementById('automatic-irrigation-status').textContent = "Active";
    } else {
        document.getElementById('automatic-irrigation-status').textContent = "Disabled";
    }
}

// Run the function every 3 seconds
setInterval(updateDashboardRow, 3000);