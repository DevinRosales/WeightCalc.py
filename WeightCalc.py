#!/usr/bin/python


# get user input for max weight, case as int and assign to the variable: weight
weight = int(input('Please enter your max weight for this lift: '))

while True:
    if weight < 60:
        print ("Get Stronger!")
        weight = int(input('For real, enter your max weight:'))

    else:
        break

def calculate_percentages( weight , percent ):
    # This takes the weight, and determines the 90, 80, 70, 60 % values
    result = weight * (percent / 100)

    print ( "%s percent of the weight %s lbs is %s" % (percent , weight, result) )

    return result

def plate_subtract ( weight , plateWeight , plates):
    double_plateWeight = plateWeight * 2
    if weight >= double_plateWeight:
        plates.append(plateWeight)
        weight = weight - double_plateWeight
    return plates , weight


def plate_count ( weight ):
    plates = []
    # subtract the bar
    weight = weight - 45
    while weight >= 90:
        (plates , weight) = plate_subtract (weight, 45, plates)

    while weight >= 70:
        (plates , weight) = plate_subtract (weight, 35, plates)

    while weight >= 50:
        (plates , weight) = plate_subtract (weight, 25, plates)

    while weight >= 20:
        (plates , weight) = plate_subtract (weight, 10, plates)

    while weight >= 10:
        (plates , weight) = plate_subtract (weight, 5, plates)

    while weight >= 5:
        (plates , weight) = plate_subtract (weight, 2.5, plates)

    plates.sort()
    plates.reverse()
    return plates

w90 = calculate_percentages ( weight , 90)
print (plate_count (w90))
w80 = calculate_percentages ( weight , 80)
print (plate_count (w80))
w70 = calculate_percentages ( weight , 70)
print (plate_count (w70))
w60 = calculate_percentages ( weight , 60)
print (plate_count (w60))
