# DB-YoutubeDL
A Docker image that download video from a DB

## Running the Container
you need a database with a table named 'youtube' and you need 3 columns in this order:
- id 
- name
- url

After that, you need to launch the container via this docker-compose file : 
"""
version: "3"
services: 
    portainer: 
        image: ghcr.io/randoye/db-youtubedl:1.0
        container_name: DB-Youtube-dl
        hostname: YTDownloader
        volumes: 
            - /video/destination:/output
        environment:
            dbhost: something
            dbname: something
            dbuser: something
            dbpass: something
        restart: no
"""