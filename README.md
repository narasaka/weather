weather
=======
A quick lil weather thingy made with python
- - - -


## Installation ##
    
    git clone https://github.com/narasaka/weather.git
    cd weather
    sudo dpkg -i weather_v0.0.2.deb
    sudo nano /usr/local/bin/apikeys.py 
    (get the api keys by visiting darksky.net/dev and https://ipstack.com/product)
    
    once you finished filling those up, go ahead and run:
    
    weather --version
    
### Usage ###
    
    weather
    
    2020-03-11 22:07:20
    America/Vancouver
       _.._
     .' .-'`
    /  /
    |  |
    \  \
     '._'-._
         ```

    Clear for the hour.
    4.49 °C
    Feels like 2.08 °C
    Chance of rain is 0%
- - - -
    
    weather -f marburg
    
    2020-03-16 04:11:22
    Europe/Berlin
          _
        (  )
     ( `  ) . )
    (_, _(  ,_)_)


    Mostly Cloudy
    11.85 °C
    Feels like 11.92 °C
    Chance of rain is 0%
- - - -
    
    weather -h
    
    Formatting command:
    weather [option] [location]

    The [option] is optional.
    You may leave it blank and go with the forecast based on your ip address.
    The [location] can be just a city, or your full address.

    -----

    example 1(no option): weather
    example 2(with -h option): weather -h (displays guide/help page)
    example 3(with find feature): weather -f seattle(displays forecast for Seattle)

    -----

    option list:
    -a or --advice: display an advice #still in development, sorry lol
    -f or --find: set mode to "find" and lets you input [location]
    -h or --help: display guide/help page.
    -q or --quick: display a one-sentence weather summary
    -v or --version: display current version program.

