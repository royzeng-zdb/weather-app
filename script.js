function getWeather() {
    var city = document.getElementById('cityInput').value;
    var url = 'http://127.0.0.1:5000/weather?city=' + city;
    
    fetch(url)
      .then(response => response.json())
      .then(data => {
        var weatherInfo = document.getElementById('weatherInfo');
        weatherInfo.innerHTML = `
          <h2>${data.city}</h2>
          <p>Temperature: ${data.temperature}°C</p>
          <p>Description: ${data.description}</p>
        `;
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }
  