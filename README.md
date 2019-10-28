# fightfor-alembic

## Deployment

> CAUTION: This repository needs to be double-deployed in order to function correctly when migrations that create new tables or sequences are executed. Following a deployment of this repository on a host, and the application of given Alembic migrations, this deploy needs to be deployed again so that privileges to the newly created tables/sequences are given to the defined users.