# Project: Data Modeling with Postgres

## Summary
This project creates a relational database in PosgreSQL reading json files from ```/data``` folder and insert the data into the following tables:

* ```songplays```
* ```users```
* ```songs```
* ```artists```
* ```time```

## Input Data

In this section the input data structure is described.

### Song data files

### Log data files

```json
{
    "artist":"Sydney Youngblood",
    "auth":"Logged In",
    "firstName":"Jacob",
    "gender":"M",
    "itemInSession":53,
    "lastName":"Klein",
    "length":238.07955,
    "level":"paid",
    "location":"Tampa-St. Petersburg-Clearwater, FL",
    "method":"PUT",
    "page":"NextSong",
    "registration":1540558108796.0,
    "sessionId":954,
    "song":"Ain't No Sunshine",
    "status":200,
    "ts":1543449657796,
    "userAgent":"\"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit\/537.78.2 (KHTML, like Gecko) Version\/7.0.6 Safari\/537.78.2\"",
    "userId":"73"
}
```

## Run the project

First, tables have to be created executing the next command:
```
python create_tables.py
```

Then, ETL must be executed to read the files and insert the date into the tables:
```
python etl.py
```

## Output

### Artists table

![Artists table example](docs/images/artists.png)

### Songs table

![Songs table example](docs/images/songs.png)

### Users table

![Users table example](docs/images/users.png)

### Time table

![Time table example](docs/images/time.png)

### Songplays table

![Songplays table example](docs/images/songplays.png)