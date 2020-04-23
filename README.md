# covid-19-in-my-region [![Build Status](https://travis-ci.com/perfah/covid-19-in-my-region.svg?branch=master)](https://travis-ci.com/perfah/covid-19-in-my-region)
A webserver able to plot the development of covid-19 in Swedish regions on a website. The server is written in Python and uses the web framework 'Flask'.

<p align="center">
<img src="https://i.imgur.com/l6nC3wc.png" alt="drawing" width="500"/>
</p>

## Usage

To start the webserver simply the following commands in a terminal:

    $ git clone https://github.com/perfah/covid-19-in-my-region
    $ cd covid-19-in-my-region
    $ python3 run.py
    
To test the webserver you can additionally run (in the same directory):

    $ pytest
    
## Regional support

The webserver supports the following Swedish regions:

    Blekinge, Dalarna, Gotland, Gävleborg, Halland, Jämtland, Jönköping, Kalmar, Kronoberg,
    Norrbotten, Skåne, Stockholm, Södermanland, Uppsala, Värmland, Västerbotten, Västernorrland,
    Västmanland, Västra götaland, Örebro, Östergötland
    
## Data source

The data we use is automatically retrieved from [DIGG - Antal fall av covid-19 i Sverige per dag och region](https://www.dataportal.se/sv/datasets/525_1424/antal-fall-av-covid-19-i-sverige-per-dag-och-region)

    
