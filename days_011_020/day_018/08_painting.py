import colorgram

color_list = []

colors = colorgram.extract('./days_011_020/day_018/hirst.webp', 10)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    color_list.append((r, g, b))

print(color_list)