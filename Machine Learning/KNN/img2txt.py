from scipy import misc
import sys

img = misc.imread(sys.argv[1])
with open(sys.argv[2], 'w') as file:
    x, y = img.shape
    for i in range(x):
        temp = ''
        for j in range(y):
            if img[i][j] >= 128:
                temp += '0'
            else:
                temp += '1'
        file.write(temp + "\n")