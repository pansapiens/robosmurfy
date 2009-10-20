# A Google Wave Robot, inspired the WebSmurfer (http://websmurfer.devnull.net/).
#
import re, random

from waveapi import events
from waveapi import model
from waveapi import robot

from patterns import replacements, doubles

__author__ = 'ajperry@pansapiens.com (Andrew Perry)'

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

  try: # we try, so just in case this fails somehow cleanup will still be called
    # initial substitutions
    for subst in replacements:
      prob = subst[0]
      match = subst[1]
      replace_with = subst[2]
      if prob > random.random():
        contents = contents.replace(match, replace_with)
  except:
    pass

  try:
    # cleanup and double-smurfy's
    for doub in doubles:
      match = doub[0]
      replace_with = doub[1]
      contents = contents.replace(match, replace_with)
  except:
    pass
  
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
