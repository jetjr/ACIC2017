#!/usr/bin/env python3

import sys
import itertools

args = sys.argv

if len(args) < 3:
    print('Usage:', args[0], 'Seconds', 'FPS')
    sys.exit(1)

#CREATE MAKEFLOW FILE FOR RUBIKS MOVIE

seconds = int(args[1])
pov = str(args[2])
out = str(args[3])

frames = seconds * 10
frames_l = reversed(range(1,frames + 1))
file_names = []
for j in frames_l:
    file_names.append("frame{:03d}.png".format(j))

#CREATE cube.mov DEPEND UPON LAST FRAME

sys.stdout = open('makeflow_cube', 'wt')

print("cube.mov:", " ".join(file_names))
print("\tffmpeg -r 10 -i frame%03d.png -r ntsc cube.mov", "\n")

clock = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
iterator = itertools.cycle(clock)

#CREATE ALL FRAMES
for i in file_names:
    print("{}:".format(i), "rubiks.pov")
    print("\tpovray +Irubiks.pov +O{}".format(i), "+K.{}".format(next(iterator)), "\n")
