# imports
import time
from blinkt import set_pixel, clear, show, set_clear_on_exit
from weatherDicts import conditionsDict, colourDict, conditionsShowcase
from weatherFunctions import weather_get
from pixelFunctions import pix

# city and key
apikey = 'abcde12345' # your personal key for the OpenWeatherMap api (see https://home.openweathermap.org/users/sign_up)
city_id = '1850147' # your city's id on the OpenWeatherMap api (see http://bulk.openweathermap.org/sample/)


# parameters and settings
fixedBrightness = 0.05 # non-flashing pixel brightness
minBrightness = 0.04 # flashing pixel minimum brightness
maxBrightness = 0.2 # flashing pixel maximum brightness

increment = maxBrightness # upward brightness change per pixelRefresh per interval for flashing pixels 
decrement = -1 * maxBrightness/10 # downward brightness change per pixelRefresh per interval for flashing pixels

weatherRefresh = 600 # update weather every n seconds
pixelRefresh = 0.1 # update brightnesses every n seconds
maxCounter = int(weatherRefresh/pixelRefresh) # number of cycles before updating weather
showcaseDelay = 10 # number of seconds to display showcase before getting first weather data

counter = maxCounter - int(1/pixelRefresh)*showcaseDelay # starting counter setting
conditions = conditionsShowcase # set conditions to showcase at first

set_clear_on_exit() # clear pixels on exit


# initalise pix object and set pixel colours and brightnesses
pix = pix()
pix.start(conditions,
          colourDict,
          fixedBrightness, minBrightness, maxBrightness,
          conditionsDict) 


# main loop
while True:
    ## if no pixels need brightness updates
    if pix.nFlash == 0:
        for p in range(8):        
            set_pixel(p,
                pix.colours[p]['r'],
                pix.colours[p]['g'],
                pix.colours[p]['b'],
                pix.brightnesses[p])
        show()
        time.sleep(weatherRefresh) # sleep until next weather update

    ## if any pixels need brightness updates enter loop to update and render changes
    else:
        while counter < maxCounter:
            pix.update() # update brightnesses

            #### set then show pixel colours and brightnesses
            for p in range(8):        
                set_pixel(p,
                          pix.colours[p]['r'],
                          pix.colours[p]['g'],
                          pix.colours[p]['b'],
                          pix.brightnesses[p])
            show()

            #### sleep until next pixel refresh and add 1 to counter
            time.sleep(pixelRefresh)
            counter += 1

    ## clear display to indicate update
    clear()
    show()

    ## get new weather data
    conditions = weather_get(city_id, apikey)

    ## set pixel colours and brightnesses
    pix.start(conditions, colourDict,
              fixedBrightness, minBrightness, maxBrightness,
              conditionsDict)

    ## reset counter
    counter = 0
    
