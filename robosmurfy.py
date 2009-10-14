# A Google Wave Robot, inspired the WebSmurfer (http://websmurfer.devnull.net/).
#
from waveapi import events
from waveapi import model
from waveapi import robot

__author__ = 'ajperry@pansapiens.com (Andrew Perry)'

match_dict = {
"new ": "smurfy new ",
"woman": "smurfette",
"women":"smurfettes",
"men":"smurfs",
"man":"smurf",
"was ": "was smurfily ",
"a ": "a smurfy ",
"is ":"is smurfily ",
"link":"smurf",
"are ":"are smurfily ",
"be ":"be smurfy ",
"Government":"Gargamel",
"trafficking ":"trafficking smurf ",
"who ":"who the smurf ",
" Police ":" Azrael ",
}

def OnParticipantsChanged(properties, context):
  """Invoked when any participants have been added/removed."""
  added = properties['participantsAdded']
  for p in added:
    Notify(context)

def OnRobotAdded(properties, context):
  """Invoked when the robot has been added."""
  root_wavelet = context.GetRootWavelet()
  root_wavelet.CreateBlip().GetDocument().SetText("RoboSmurf reporting for duty. Smurftastic !")

def Notify(context):
  root_wavelet = context.GetRootWavelet()
  root_wavelet.CreateBlip().GetDocument().SetText("Everything's smurfy !")

def OnBlipSubmitted(properties, context):
  blip = context.GetBlipById(properties['blipId'])
  contents = blip.GetDocument().GetText()
  for word in match_dict:
    contents = contents.replace(word, match_dict[word])
    blip.GetDocument().SetText(contents)

if __name__ == '__main__':
  myRobot = robot.Robot('robosmurfy', 
      image_url='http://robosmurfy.appspot.com/static/images/icon.png',
      version='1',
      profile_url='http://robosmurfy.appspot.com/')
  myRobot.RegisterHandler(events.WAVELET_PARTICIPANTS_CHANGED, OnParticipantsChanged)
  myRobot.RegisterHandler(events.WAVELET_SELF_ADDED, OnRobotAdded)
  myRobot.RegisterHandler(events.BLIP_SUBMITTED, OnBlipSubmitted)
  myRobot.Run()
