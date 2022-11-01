#indexesview
indexesview

Web service that:
- receives cryptocurrency rates from coinchecko
- saves their address, name, price in the database
- api-point returns this data, with filtering options by name, by market, by name and market
- connected swagger
This solution is packaged in docker compose
Preferred stack:
-django-rest-framework
- postgres



# documentation


# Get Started:

To start, you need to create docker containers and run them.
If Docker is not installed on the server, then it's time to install it:

https://docs.docker.com/engine/install/ubuntu/
https://docs.docker.com/compose/install/compose-plugin/#installing-compose-on-linux-systems

Clone the repository to a convenient location:

    git@github.com:MikhailKravchenko/indexesview.git

 Collecting images:

    docker-compose -f docker-compose.yml up -d --build

#Information
To parse/update data, pull the handle: api/v1/refresh/
