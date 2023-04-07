#%%
import pandas as pd
from settings.parameters import parameters
from etl import visuals, creation, extraction

visuals.range_to_extract_data(parameters.POSITION_LEFT_BOTTOM, 
                              parameters.POSTION_RIGHT_UP,
                              parameters.ZONE)

vector_x, vector_y = creation.position_vector_in_each_direction(parameters.POSITION_LEFT_BOTTOM, 
                                                                parameters.POSTION_RIGHT_UP,
                                                                parameters.GRID_NUMBER_OF_POINTS)
                            
grid_utm_without_zone = creation.positions_to_extract_data(vector_x,vector_y)

grid = creation.grid_to_latlon(grid_utm_without_zone,parameters.ZONE,parameters.LETTER)

visuals.grid_to_extract_data(parameters.POSITION_LEFT_BOTTOM, 
                             parameters.POSTION_RIGHT_UP,
                             parameters.ZONE,
                             grid)

ext = extraction.Extraction_instance()

grid_elevation = ext.extract_data_from_aester30m(grid)

pd.DataFrame(grid_elevation).to_csv('terreno.csv')

print(f"min elevation {pd.DataFrame(grid_elevation).elevation.min()} and max elevation {pd.DataFrame(grid_elevation).elevation.max()}")
