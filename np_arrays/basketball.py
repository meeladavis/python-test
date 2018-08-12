# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)
#print type
print(type(np_baseball))

#import weight data
filename_w = 'Basketball_weight.txt'
np_weight = np.loadtxt(filename_w)

#convert heights to metres
np_weight_kg = 0.453592 * np_weight
print("weight")
print(np_weight_kg)
print(len(np_weight_kg))

#import height data
filename_h = 'Basketball_height.txt'
np_height = np.loadtxt(filename_h)

#convert heights to metres
np_height_m = 0.0254 * np_height
print("height")
print(np_height_m)
print(len(np_height_m))

#Calculate BMI
np_bmi = np_weight_kg / ((np_height_m)**2)
print("bmi")
print(np_bmi)

bmi_low = np_bmi < 21

light = np.array(np_bmi < 21)
print(light)

print(np_bmi[50])
print(np_bmi[100:110])


################################
#2d arrays
# Create baseball, a list of lists
#baseball_2d = [[180, 78.4],
#            [215, 102.7],
#            [210, 98.5],
#            [188, 75.2]]

filename_all = 'Basketball_numeric.txt'
np_baseball_2d = np.loadtxt(filename_all,skiprows=1)


# Create a 2D numpy array from baseball: np_baseball
#np_baseball_2d = np.array(baseball_2d)


# Print out the type of np_baseball
print(np_baseball_2d)
print(np_baseball_2d.shape)
print(np_baseball_2d[:,1])
print(np_baseball_2d[124,0])




# create height from np_baseball_2d
np_heightx = np_baseball_2d[:,1]
print(np_heightx)

np_weightx = np_baseball_2d[:,2]
print(np_weightx)

avg_h = np.mean(np_heightx)
avg_w = np.mean(np_weightx)

med_h = np.median(np_heightx)
med_w = np.median(np_weightx)

std_h = np.std(np_heightx)
std_w = np.std(np_weightx)

print("HEIGHT - Average: " + str(avg_h) + " Median: " + str(med_h) + " Standard Deviation: " + str(std_h) )
print("WEIGHT - Average: " + str(avg_w) + " Median: " + str(med_w) + " Standard Deviation: " + str(std_w) )


cor = np.corrcoef(np_heightx, np_weightx)
print(cor)
