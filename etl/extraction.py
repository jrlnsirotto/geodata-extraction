import requests
from time import sleep
from tqdm import tqdm 

class Extraction_instance():
    def __init__(self):
        self.client = requests.Session()

    def extract_data_from_aester30m(self,grid):

        with self.client as Client:
            
            elements = len(grid.get('x_latlon'))

            grid['elevation'] = []
            
            for position in tqdm(range(0,elements), colour="BLUE"):

                x_latlon = grid.get('x_latlon')[position]
                
                y_latlon = grid.get('y_latlon')[position]
                
                req = f'https://api.opentopodata.org/v1/aster30m?locations={x_latlon},{y_latlon}'

                api_response = Client.get(url=req,timeout=60)
                
                elevation = api_response.json().get('results')[0].get("elevation")
                
                grid.get('elevation').append(elevation)
                
                sleep(1)
            return grid

