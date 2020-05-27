import numpy as np

print("Hello World !")

days_left = np.datetime64('2021-07-23') - np.datetime64('today')
print("We are", days_left, "away from Tokyo olympic games...")
