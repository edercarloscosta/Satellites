    let current_latitude = 0.0;
    let current_longitude = 0.0;

    (() => {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition((e) => {
                current_latitude = e.coords.latitude;
                current_longitude = e.coords.longitude;
            });
          } else {
            console.log("Geolocation is not supported by this browser.");
          }
        })();

    let mymap = L.map('mapid').setView([current_latitude,current_longitude], 2);

    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 10,
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1,
        accessToken: 'you_mapbox_access_token_here'
    }).addTo(mymap);

    items_on_map = (items) => {
        for (var i = 0; i < items.length; i++)
              mymap.removeLayer(items[i]);
    }

    event_message = (e) => {

        let data = JSON.parse(e.data);
        // Enable the code below to see consumer logs
        // console.log(data)

        let iss_satellite = L.divIcon({
          html: '<i class="fas fa-satellite fa-3x"></i>',
          iconSize: [10, 10],
          className: 'satelliteIssIcon'
        });

        let iss_tracing = L.divIcon({
          html: "<strong>.</strong>",
          iconSize: [5, 5],
          className: 'tracingIssIcon'
        });

        let sentinel_satellite = L.divIcon({
          html: '<i class="fas fa-satellite fa-3x"></i>',
          iconSize: [10, 10],
          className: 'satelliteSentinelIcon'
        });

        let sentinel_tracing = L.divIcon({
          html: "<strong>.</strong>",
          iconSize: [5, 5],
          className: 'tracingSentinelIcon'
        });

        if(data.id === 25544) {

            items_on_map(iss_positions)

             // Building the custom marker
            let iss_current_position = L.marker([data.latitude, data.longitude], {
               icon: iss_satellite
            })
            //  Building a tracer dots
            let iss_tracing_position = L.marker([data.latitude, data.longitude], {
                icon: iss_tracing
            })

            iss_positions.push(iss_current_position);

             // Adding on map layer
            iss_tracing_position.addTo(mymap)
            iss_current_position.addTo(mymap);
        }


        if(data.id === 40697) {
            items_on_map(sentinel_positions)

             // Building the custom marker
            let sentinel_current_position = L.marker([data.latitude, data.longitude], {
               icon: sentinel_satellite
            })
            //  Building a tracer dots
            let sentinel_tracing_position = L.marker([data.latitude, data.longitude], {
                icon: sentinel_tracing
            })

            sentinel_positions.push(sentinel_current_position);

            // Adding on map layer
            sentinel_tracing_position.addTo(mymap)
            sentinel_current_position.addTo(mymap);
          }

    }

    iss_positions = [];
    sentinel_positions = [];
    let iss_event_source = new EventSource('/consumer_iss');
    iss_event_source.addEventListener('message', event_message, false);

    let sentinel_event_source  = new EventSource('/consumer_sentinel');
    sentinel_event_source.addEventListener('message', event_message, false);