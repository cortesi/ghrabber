Grab all files matching a search specification from Github. 

Downloaded files are written to files named user.repository. Existing files
with the same name are skipped, which means that you can reasonably efficiently
stop and resume a ghrab. 

Note that this is a Quick Hack that may break whenever Github changes even
minor features on the site.


### Usage

Grab all .bash_history files:

    ./ghrabber.py "path:.bash_history"

Grab all files with extension of .key:

    ./ghrabber.py "extension:key"


### Installation

Check out this code and install the dependencies: 

    git clone git@github.com:cortesi/ghrabber.git
    cd ghrabber
    pip install beautifulsoup requests
    
If pip is not installed, try to install it with `easy_install pip` first

