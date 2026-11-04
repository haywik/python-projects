import os,subprocess,time

cmds=[
  "kscreen-doctor --dpms off",
  "killall -9 firefox",
  "killall -9 Discord",
  "killall -9 sober",
  "killall -9 elisa"
  'elisa "$HOME"/Music/*.mp3'
  "playerctl --player=elisa shuffle On"
  "playerctl --player=elisa play"
  "kscreen-doctor --dpms on",
]

for i in cmds:
  try:
    subprocess.run(i)
  except:
    pass
  
