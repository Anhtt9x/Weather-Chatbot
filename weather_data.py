import pyowm
import os
from dotenv import load_dotenv
load_dotenv()

own_key=os.getenv('OWN_KEY')

class WeatherData:
    def __init__(self) -> None:
        self.own_key = own_key
        self.own = pyowm.OWM(self.own_key)

    def processRequest(self,req):
        
