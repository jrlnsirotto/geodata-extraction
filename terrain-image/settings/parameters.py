from pydantic import BaseSettings

class Extraction_parameters(BaseSettings):

    EXTRACTION_NAME: str

    ZONE: int

    ZONE_FACTOR : float 

    LETTER: str

    POSITION_LEFT_BOTTOM : list

    POSTION_RIGHT_UP : list

    GRID_NUMBER_OF_POINTS : int

    SAVE: bool


    class Config:
        env_file = ".env"

parameters = Extraction_parameters()
