# Auction Game Bidding Strategy

A strategy to win the 'Auction Game'

# Synopsis

You are in an auction bidding against other people in real time. The items you are bidding are paintings from four different artists (Rembrandt, Da Vinci, Picasso, and Van Gogh). All players start with $100 and bid some amount of money for each painting that comes up. The order in which the paintings come up is randomized in the beginning of the game, but is known to the player. The objective is to get 3 paintings from the same artist before anyone else. 

# Controls

The algorithm defined in 'determinebid' function of NewBot file determines the bids automatically based on the predetermined strategy.
The only thing that the player must do is to connect to the server and chose a nickname.

# Set-up Instructions

The host and client must connect to the same network. The host modifies lines 12 and 13 in the server.py file to select number of players and the host's IP address respectively. Meanwhile, the client must modify line 10 in NewBot.py to match the host's IP address. After server.py has been executed by the host, the client must execute NewBot.py and enter his/her name. The game begins when *all* clients have connected to the server.

# Compatibility

The game requires python modules that come with Continuum's [Anaconda](https://www.continuum.io/why-anaconda).

Python 2.7 must be installed. 

The game is compatible with both OS X and Windows given the above prerequisites.

# Technology Used

[Python 2.7](https://www.python.org/download/releases/2.7/)

Continuum's [Anaconda](https://www.continuum.io/why-anaconda)

# Credits

The backbone of the game is programmed by Prof. Dennis Shasha. A UI version of the Auction game is available at his website ['Dr.Ecco'](http://cims.nyu.edu/drecco/)

# [Website]( http://brainstorm6334.github.io/Auction-Game-Bidding-Strategy)



