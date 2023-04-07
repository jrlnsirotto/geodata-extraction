import matplotlib.pyplot as plt

def range_to_extract_data(position_left_bottom:list, 
                          position_right_up:list,
                          zone:int,
                          sizes:list=[15,15],
                          colors:list=[80,80],
                          prop:float=0.00005) -> plt:

    
    x = [position_left_bottom[0] + zone*(10**6), position_right_up[0] + zone*(10**6)]
    y = [position_left_bottom[1], position_right_up[1]]
        
    rectangle = plt.Rectangle((x[0],y[0]), 
                              x[1] - x[0], 
                              y[1] - y[0], 
                              fill=False, 
                              ec="red",
                              linestyle='--')
                              
    plt.style.use('_mpl-gallery')
    plt.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)
    plt.gca().add_patch(rectangle)
    plt.title('Posicionamento')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.show()


def grid_to_extract_data(position_left_bottom:list, 
                          position_right_up:list,
                          zone:int,
                          grid:dict,
                          sizes:list=[15,15],
                          colors:list=[80,80],
                          prop:float=0.00005) -> plt:

    
    x = [position_left_bottom[0] + zone*(10**6), position_right_up[0] + zone*(10**6)]
    y = [position_left_bottom[1], position_right_up[1]]
        
    rectangle = plt.Rectangle((x[0],y[0]), 
                              x[1] - x[0], 
                              y[1] - y[0], 
                              fill=False, 
                              ec="red",
                              linestyle='--')
    
    plt.style.use('_mpl-gallery')
    plt.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)
    plt.scatter(grid.get('x_utm',[]), grid.get('y_utm',[]))
    plt.gca().add_patch(rectangle)
    plt.title('Posicionamento')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.show()