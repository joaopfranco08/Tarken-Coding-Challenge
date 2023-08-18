from PIL import Image
img = Image.open('meteor_challenge_01.png')
pixels = list(img.getdata())

red = (255,0,0,255)
blue = (0,0,255,255)
white = (255,255,255,255)
black = (0,0,0,255)


# --------------------------------------
#            1st and 2nd Task:
# --------------------------------------
"""To get the amount of stars and meteors, I simply used the .count() function on the list I obtained
from the image pixel data. To identify the stars, I filtered the pixels with a pure whitecolor, while 
for the meteors, I filtered by the pure red color"""

stars = pixels.count(white)
meteors = pixels.count(red)


# --------------------------------------
#               3rd Task:
# --------------------------------------
"""Firstly I obtained the height and width of the image in pixels using img.size."""
x = 0
y = 704

"""In order to determine the y-coordinate at which the first water pixel appears (water level), I 
iterated through the pixels, checked if the color was pure blue, and then saved the y-value as 192.""" 
# for pixel in pixels:
#     if x == 704:
#         x = 0
#         y -= 1
#     if pixel == blue:
#         break
#     x += 1
# print(y)


"""Then, I iterated through all the pixels once again to obtain the x-values where the pixels were 
pure blue and the y-value was 192."""
blueXindex = []
for pixel in pixels: 
    if x == 704:
        x = 0
        y -= 1
    if pixel == blue and y == 192:
        blueXindex.append(x)
    x += 1

"""Finally, I went through all the pixels and incremented the 'meteors_above_water' counter for each 
meteor with an x-value matching an x-value in 'blueXindex'."""
meteors_above_water = 0
for pixel in pixels: 
    if x == 704:
        x = 0
        y -= 1

    if x in blueXindex and pixel == red:
        meteors_above_water += 1
    
    if pixel == blue:
        break
    x += 1


# --------------------------------------
#                4th Task:
# --------------------------------------

"""To make the dots more readable and discernible from the rest of the image, I created a new image 
in which all the dots were made white, while the remaining areas were black."""
# colors = [white, red]

# newImageData = []
# for pixel in pixels:
#     if pixel not in colors:
#         newImageData.append(black)
#     else:
#         newImageData.append(white)

# newImage = Image.new(img.mode,img.size)
# newImage.putdata(newImageData)
# newImage.save('imagem.png')

"""While examining the dots, I considered the possibility that a hidden phrase might be encoded in 
Morse code, given the presence of white dots and spaces between them. I attempted to interpret the 
lines as Morse code characters, but I was unable to get to an actual phrase."""
# newImage = Image.open('imagem.png')
# newPixels = list(newImage.getdata())

# morsecode = []
# x = 0
# y = 704

# linha = ""
# for pixel in newPixels: 
#     if x == 704:
#         x = 0
#         y -= 1

#         if linha:
#             morsecode.append(linha)
#         else:
#             morsecode.append('_')

#         linha = ""
    
#     if pixel == white:
#         linha += '.'

#     x += 1
# morsecode = ' '.join(morsecode)


# --------------------------------------
#                Results:
# --------------------------------------
print(f"""1) Number of Stars: {stars}
2) Number of Meteors: {meteors}
3) Meteors that will fall on the Water: {meteors_above_water}
4) Hidden Phrase: 404 Page not found :(""")