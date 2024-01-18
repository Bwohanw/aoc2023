f = open("two.txt", "r")

games = f.readlines()


power = 0


for game in games:
    idsplit = game.split(':')
    id = int(idsplit[0][5:])
    turns = idsplit[1].split(";")
    seenred = 0
    seengreen = 0
    seenblue = 0
    for turn in turns:
        colorsplit = turn.split(',')
        for color in colorsplit:
            if "blue" in color:
                blue = int(color.split("blue")[0].strip())
                if (blue > seenblue):
                    seenblue = blue
            if "green" in color:
                green = int(color.split("green")[0].strip())
                if (green > seengreen):
                    seengreen = green
            if "red" in color:
                red = int(color.split("red")[0].strip())
                if (red > seenred):
                    seenred = red
    power += seenred*seenblue*seengreen


print(power)

