Robosmurfy - A little blue Google Wave Robot
============================================

Inspired by the <a href="http://websmurfer.devnull.net/">WebSmurfer</a>.

Just add robosmurfy@appspot.com to your Wave. Smurfy !

TODO:
---------------------
* Fix things so that formatting is preserved (currently formatting is lost ... annoying). ( use something like: annotations = blip.GetAnnotations(); for a in annotations:; reapply annotations based on a.name, a.value and a.range. See http://www.alanwestbrook.com/wavebot/synshedbot.py for an example of setting annotations ).

* Convert most (all?) substitutions to regexes, to deal with capitalization (eg House vs. house).

<del>* Prevent double substitution, eg: "This is some excellent prose" => "This smurfily is smurfily some excellent prose" => "This smurfily smurfily is smurfily smurfily some excellent prose".</del>

* Add "Smurftastic!" and "Smurfilicious!" after some sentences (analysis of the original WebSmurfer required to determine exactly where. "Smurftastic!" seems to appear after '' quotes).

<del>* Further analyse output of the WebSmurfer to match subsititutions and behaviour more closely (eg, words.txt dictionary vs. smurf_words.txt, the which is words.txt passed through the original Websmurfer).</del>
