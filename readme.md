# GeoData Extraction

<img align="right" width= 200 src="images/logo.webp">

GeoData extraction intends to help users to download data from a certain area in a easy way. The repository is under construction and has no commercial intention.


## Main goals
- Extract terrain elevation from a certain area

- Easy  to use: only two points coordenates are needed to delimite the area

- Possibility of delimiting the area with more points

- User input/output are UTM coordinates

- Possibility to choose diferent databases, based on public api resources

- Possibility to visualize the 3D terrain

- .csv or .json file with coordinates and elevation, and error associated will be automaticaly generated

## Premisses
- Order of the UTM coordinates list matters

## How to setup the application to run

Use make command to create the virtual environment

```make virtual-env```

and then activate it

```source .venv/bin/activate```

install the dependencies

```make deps```

Be sure you have all the environment variable in a .env file

```
EXTRACTION_NAME = "<name-here>"

ZONE = "<zone-here>"

ZONE_FACTOR = "<zone-factor-here>"

LETTER ="<zone-letter-here>"

POSITION_LEFT_BOTTOM = "[<x-coordinate-here>,<y-coordinate-here>]"

POSTION_RIGHT_UP = "[<x-coordinate-here>,<y-coordinate-here>]"

GRID_NUMBER_OF_POINTS = "<number-of-point-in-one-direction>" 

SAVE = "True"
```

and then, just run

```make run```

## Code architecture


## To do list
- Inclusion of others apis databases

- Make possible the area delimitation using several points