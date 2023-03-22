# Morgan Gerdin
# Volume Calculater
# 1/28/2022
Volume = 0.0    # make volume a float
for Length in range(1,11):
    for Width in range(1, 6):    # make range 6 so that it goes until 5
        Volume = Length * Width * .25
        print("The Length is:", Length, "The Width is:",  Width, "The Volume is:", Volume)   # print volume
