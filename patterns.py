
# probability, match, replace

replacements = [
(1.0, " new ", " smurfy new "),
(1.0, "woman ", "smurfette "),
(1.0, "women ","smurfettes "),
(1.0, "Woman ", "Smurfette "),
(1.0, "Women ","Smurfettes "),
(1.0, "men ","smurfs "),
(1.0, "man ","smurf "),
(1.0, "Men ","Smurfs "),
(1.0, "Man ","Smurf "),
(1.0, " was ", " was smurfily "),
(0.5, " a ", " a smurfy "),
(1.0, " is "," is smurfily "),
(1.0, "link","smurf"),
(1.0, " are "," are smurfily "),
(0.5, " be "," be smurfily "),
(1.0, " my "," my smurfy "),
(1.0, "Government ","Gargamel "),
(1.0, "government","gargamel"),
(1.0, "Microsoft","Gargamel"),
(1.0, "microsoft","gargamel"),
(1.0, "Police","Azrael"),
(1.0, "police","Azrael"),
(1.0, "house","mushroom"),
(1.0, "House","Mushroom"),
(1.0, "home","mushroom"),
(1.0, "Home","Mushroom"),
(1.0, "Condo","Mushroom"),
(1.0, "condo","Mushroom"),
(1.0, "condominium", "mushroom"),
(1.0, "Condominium", "Mushroom"),
(1.0, "apartment", "mushroom"),
(1.0, "Apartment", "Mushroom"),
(1.0, "building", "mushroom"),
(1.0, "Building", "Mushroom"),
(1.0, "mansion", "mushroom"),
(1.0, "Mansion", "Mushroom"),
(1.0, "palace", "mushroom"),
(1.0, "Palace", "Mushroom"),
(1.0, "terrorism","Smurfism"),
(1.0, "Terrorism","Smurfism"),
(1.0, "terrorist","Smurf"),
(1.0, "Terrorist","Smurf"),
(1.0, "small ","smurfy "),
(1.0, " child"," Baby Smurf"),
(1.0, " Child"," Baby Smurf"),
(1.0, " baby"," Baby Smurf"),
(1.0, " Baby"," Baby Smurf"),
(1.0, " babies"," Baby Smurfs"),
(1.0, " Babies"," Baby Smurfs"),
(1.0, "Christ", "Smurf"),
(1.0, "christ", "smurf"),
(1.0, "Messiah", "Smurf"),
(1.0, "messiah", "smurf"),
(1.0, "Pope", "Grandpa Smurf"),
(1.0, "pope", "Grandpa Smurf"),
(1.0, "President", "Papa Smurf"),
(1.0, "president", "Papa Smurf"),
(1.0, "link", "smurf"),
(1.0, "mix", "smurf"),
(1.0, "cocaine", "smurfcaine"),
(1.0, "democracy", "Smurfocracy"),
(1.0, "Democracy", "Smurfocracy"),
(1.0, "enforcement", "ensmurfment"),
(1.0, "Enforcement", "Ensmurfment"),
(1.0, "entertainment", "smurftainment"),
(1.0, "Entertainment", "Smurftainment"),
(1.0, "lawyer", "Gargamel"),
(1.0, "Lawyer", "Gargamel"),
(1.0, "magistrate", "Gargamel"),
(1.0, "Magistrate", "Gargamel"),
(1.0, "networking", "Smurf Collectivizing"),
(1.0, "Networking", "Smurf Collectivizing"),
(1.0, "network", "Smurf Collective"),
(1.0, "Network", "Smurf Collective"),
(1.0, "outrage", "smurfrage"),
(1.0, "Outrage", "Smurfrage"),
(1.0, "surf", "smurf"),
(1.0, "Surf", "Smurf"),
(1.0, "software", "softsmurf"),
(1.0, "Software", "Softsmurf"),
(1.0, "threat", "smurf"),
(1.0, "Threat", "Smurf"),

(1.0, "king","king smurf"),
(1.0, "King","King smurf"),
]

# HACK, till we do this properly
# will remove duplicate smurfy and smurfily's
doubles = [
("smurfy smurfy","smurfy"),
("smurfily smurfily","smurfily"),
("smurfy new smurfy new", "smurfy new"),
("the smurf the smurf", "the smurf"),
("Smurf Smurf", "Smurf"),
("smurf smurf", "smurf"),
("Smurf Smurf Smurf", "Smurf"),
("smurf smurf smurf", "smurf"),
]

