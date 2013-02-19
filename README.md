Grab all files matching a search specification from Github. 

Downloaded files are written to files named user.repository. Existing files
with the same name are skipped, which means that you can reasonably efficiently
stop and resume a ghrab. 

Note that this is a Quick Hack that may break whenever Github changes even
minor features on the site.


### Examples

Grab all .bash_history files:
`ghrabber.py "path:.bash_history"`

Grab all files with extension of .key:
`ghrabber.py "extension:key"`
