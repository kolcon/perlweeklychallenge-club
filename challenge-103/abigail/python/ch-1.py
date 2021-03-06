#!/opt/local/bin/python

#
# See ../README.md
#

#
# Run as python ch-1.py < input-file
#

#
# We're reading years from standard input, one year per line, outputting
# years from the sexagenary cycle [1]. This is slightly more than what
# the challenge ask; the challenge asks to output the heavenly stem [2],
# and the earthly branch [3]. But we also output its Yin/Yang.
#
# [1] https://en.wikipedia.org/wiki/Sexagenary_cycle
# [2] https://en.wikipedia.org/wiki/Heavenly_Stems
# [3] https://en.wikipedia.org/wiki/Earthly_Branches
#

#
# Each of the cycles have been rotated so the first entry corresponds to
# the year 0 in the Proleptic Gregorian calendar. (We're using the
# convention of having a year 0, as per ISO 8601).
# That way, we can just mod the year with the number of entries, without
# first having to subtract something from the year.
#
# The heavenly stems last for 2 years, so we just duplicate the entries.
#

yin_yang         = ["Yang", "Yin"]
heavenly_stems   = ["Metal",  "Metal",   "Water",  "Water", "Wood",  "Wood",
                    "Fire",   "Fire",    "Earth",  "Earth"]
earthly_branches = ["Monkey", "Rooster", "Dog",    "Pig",   "Rat",   "Ox",
                    "Tiger",  "Rabbit",  "Dragon", "Snake", "Horse", "Goat"]


import fileinput

for year in fileinput . input ():
    year = int (year)
    print (yin_yang         [year % len (yin_yang)],
           heavenly_stems   [year % len (heavenly_stems)],
           earthly_branches [year % len (earthly_branches)])
