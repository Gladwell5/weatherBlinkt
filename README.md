# weatherBlinkt
Weather display with Pi Zero W and Blinkt

1. Ensure your RPi has internet access so it can get the weather data.
2. Set up an OpenWeatherMap API account to get your key.
3. Look up your city's id on the OpenWeatherMap.
4. Enter your key and city id in the weather.py file.
5. Run the weather.py file or better yet, add it to your crontab to run on reboot.

If there are any flashing pixels (rain/snow), the consumes about 12% of CPU on average.
If no flashing pixels, it's much lower as it just sets the pixels and then sleeps.

The weather colour and flash settings are tailored to where I live, which is rarely very warm or very cold but has plenty of rain.
So the main thing for me to know in the morning is whether it's raining, cloudy or clear skies.
You may want to adjust the settings (in conditionsDict in the weatherDicts.py file) to suit your city's climate.
