# Satellites
A environment for testing technologies composition 
- Leaflet
- Flask
- Kafka (This guy was my real motivator for this lab)

### Goals
Offer a simple and dynamic (Laboratory) web application where we may run Kafka reading maps coordinates on real-time. 
Each 15 sec the application sends message (Producer) to Kafka topic with coordinates, those coordinates will be read (Consumer) by an endpoint on Leaflet and diplay on satellites icons.

**Red satellite icon:** Display coordinates on real time from [where the ISS at?](https://wheretheiss.at/w/developer)

**Blue satellite icon:** 
 - Display fake coordinates from local file OR 
 - In case you want to real data this application is ready for running the coordinates from Sentinel 2A satellite. Please to read the section below "Real coordinates from Sentinel 2A"


## Pre-requirements
 - [Docker](https://docs.docker.com/get-docker/)
 - [Docker Compose](https://docs.docker.com/compose/install/)
 - Mapbox: You need to create an account, generate an accessToken and reference this on `leaflet.js`
   - This is a Mapbox requirement to rendering map on Leaflet, but it's pretty simple [Access Token](https://docs.mapbox.com/help/getting-started/access-tokens/)
 - Add Mapbox accessToken on code:
   - Go to `flaskProject/app/static/js/` and open the `leaflet.js` file
   - Replace `you_mapbox_access_token_here` by your access token
 
## Real coordinates from Sentinel 2A

> Note: Keep in mind the current limit is 1000 transactions/hour

- First of all, should access [n2yo](https://www.n2yo.com/api/) to create a register and generates API Key
- After generates you API Key, copy that and paste into `const.py` file:
  - Go to `flaskProject/app/service/` open the file `const.py`
  - Replace `personal_key_here` by the API Key
- Adapting the application
  - Go to flaskProject/app/ open the file `app.py`
  - Follow the two simple steps on top comments
    - Import: Sentinel2A
    - Replace Worker() parameter from "" to `Sentinel2A.SENTINEL2A_URI.value`
  - Now just read next section "How to run step-by-step"

## How to run step-by-step
1. Clone this repo
2. Navigate to root path flaskProject when you w'll see `docker-compose.yaml` and `Dockerfile`
3. Compile the docker-compose with:
>docker-compose build
4. Run docker compose:
>docker-compose up -d
5. In case you want to see logs run:
>docker-compose up
6. Go to browser and type 0.0.0.0:5001 

## References
### Leaflet
<img src="https://user-images.githubusercontent.com/76518699/111771022-10edd180-88a3-11eb-8cb8-460864516a34.png" width="200px" height="80px"/> 
An open-source JavaScript library for mobile-friendly interactive maps

See more on [Leaflet](https://leafletjs.com/)

### Flask
<img src="https://user-images.githubusercontent.com/76518699/111771355-7b9f0d00-88a3-11eb-998a-c801d41c5421.png" width="200px" height="80px"/>
A really fun web development framework / microframework (Python)

See more on [Flask](https://flask.palletsprojects.com/en/1.1.x/)

### Kafka
<img src="https://user-images.githubusercontent.com/76518699/111771200-4e525f00-88a3-11eb-8f32-f817e216b07c.png" width="200px" height="80px"/>
Apache Kafka is an open-source distributed event streaming platform used by thousands of companies for high-performance data pipelines, streaming analytics, data integration, and mission-critical applications.

See more in [Apache Kafka](https://kafka.apache.org/)

##### Bitnami containers
<img src="https://user-images.githubusercontent.com/76518699/111771572-c751b680-88a3-11eb-8831-79bec20675f7.png" width="200px" height="80px"/>

This guys offer all we need to use Kafka esily as possible

See more on [Bitnami](https://bitnami.com/stack/kafka/containers)
