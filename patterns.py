
# probability, match, replace

replacements = [
(1.0, " new ", "smurfy new "),
(1.0, "woman ", "smurfette "),
(1.0, "women ","smurfettes "),
(1.0, "men ","smurfs "),
(1.0, "man ","smurf "),
(1.0, " was ", "was smurfily "),
(0.5, " a ", " a smurfy "),
(1.0, " is "," is smurfily "),
(1.0, "link","smurf"),
(1.0, " are ","are smurfily "),
(0.5, " be ","be smurfily "),
(1.0, " my ","my smurfy "),
(1.0, "Government ","Gargamel "),
(1.0, "government","gargamel"),
(1.0, "trafficking ","trafficking smurf "),
(1.0, " who ","who the smurf "),
(1.0, "Police ","Azrael "),
(1.0, "police ","Azrael "),
(1.0, "house ","mushroom "),
(1.0, "House ","Mushroom "),
(1.0, "home ","mushroom "),
(1.0, "Home ","Mushroom "),
(1.0, "terror","Smurf"),
(1.0, "Terror","Smurf"),
(1.0, "small ","smurfy "),
(1.0, " child"," Baby Smurf"),
(1.0, " Child"," Baby Smurf"),
(1.0, " baby"," Baby Smurf"),
(1.0, " Baby"," Baby Smurf"),
]

# HACK, till we do this properly
# will remove duplicate smurfy and smurfily's
doubles = [
(1.0, "smurfy smurfy","smurfy"),
(1.0, "smurfily smurfily","smurfily"),
(1.0, "smurfy new smurfy new", "smurfy new"),
(1.0, "the smurf the smurf", "the smurf"),
(1.0, "Smurf Smurf", "Smurf"),
(1.0, "smurf smurf", "smurf"),
(1.0, "Smurf Smurf Smurf", "Smurf"),
(1.0, "smurf smurf smurf", "smurf"),
]

