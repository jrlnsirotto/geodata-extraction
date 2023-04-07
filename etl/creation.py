import utm

import numpy as np

def position_vector_in_each_direction(position_left_bottom:list, 
                                      position_right_up:list,
                                      grid_number_of_points:int) -> np.array:
    
    vector_x =  np.linspace(position_left_bottom[0], 
                            position_right_up[0],                              
                            grid_number_of_points)

    vector_y =  np.linspace(position_left_bottom[1], 
                            position_right_up[1],                              
                            grid_number_of_points)
    


    return vector_x, vector_y


def positions_to_extract_data(vector_x:np.array, 
                              vector_y:np.array) -> np.array:
    x_list = []
    y_list = []
    
    for x in vector_x:
        for y in vector_y:
            x_list.append(x)
            y_list.append(y)
 
    return {'x':x_list, 'y':y_list}

def grid_to_latlon(grid,zone,letter):


    grid['x_utm'] = []
    grid['y_utm'] = []
    grid['x_latlon'] = []
    grid['y_latlon'] = []

    for i in range(0,len(grid.get('x',[]))):

        latlon = utm.to_latlon(grid.get('x')[i],
                               grid.get('y')[i],
                               zone_number=zone,
                               zone_letter=letter)
        
        grid['x_utm'].append(grid.get('x')[i]+zone*(10**6))
        grid['y_utm'].append(grid.get('y')[i])
        grid['x_latlon'].append(latlon[0])
        grid['y_latlon'].append(latlon[1])
    
    grid.pop('x')
    grid.pop('y')

    return grid