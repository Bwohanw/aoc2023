f = open("two.txt", "r")

games = f.readlines()

numred = 12
numgreen = 13
numblue = 14

idxsum = 0


for game in games:
    possible = True
    idsplit = game.split(':')
    id = int(idsplit[0][5:])
    turns = idsplit[1].split(";")
    for turn in turns:
        colorsplit = turn.split(',')
        for color in colorsplit:
            if "blue" in color:
                blue = int(color.split("blue")[0].strip())
                if (blue > numblue):
                    possible = False
            if "green" in color:
                green = int(color.split("green")[0].strip())
                if (green > numgreen):
                    possible = False
            if "red" in color:
                red = int(color.split("red")[0].strip())
                if (red > numred):
                    possible = False
    if (possible):
            idxsum += id

print(idxsum)