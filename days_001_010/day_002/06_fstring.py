# f-String

score = 0
height = 1.78
isWinning = True

print("score = " + str(score))
print("height = " + str(height))
print("isWinning = " + str(isWinning))

print(f"score = {score}")
print(f"height = {height}")
print(f"isWinning = {isWinning}")

heigth_format = "{:.4f}".format(height)

print(f"Height formatted = {heigth_format}")