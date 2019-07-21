import numpy as np
# Record flags
# Flag = 0 means that this is the first time input
# Flag = 1 means that this is the normal condition and will be continue to find centroid
# Flag = 2 means that the centroid is correct and no need to change
# Flag = 3 means that the centroid maybe not correct and need to be fixed
# The initial value is 0
flag = 0
# Input value
centroid_x = 0
centroid_y = 0
# The original centroid
centroid_origin_x = 0
centroid_origin_y = 0
# The new centroid input
centroid_nowaday_x = 0
centroid_nowaday_y = 0
# Record the extreme centorid data continuly
centroid_abnormal_x = []
centroid_abnormal_y = []
# Record the normal data intermittently
centroid_normal_x = []
centroid_normal_y = []
# Record the final result of centroid
centroid_final_x = []
centroid_final_y = []
# Distance threshold value
Maxdistance = 0
# length of normal/abnormal array
length_normal = len(centroid_normal_x)
length_abnormal = len(centroid_abnormal_x)
# Distance formula
def distance( a_x , a_y , b_x , b_y ):
    distance = ((b_x - a_x)**2 + (b_y - a_y)**2)**0.5
return distance
# Judgement
if flag == 0:
    flag = 1
    centroid_origin_x = centroid_x
    centroid_origin_y = centroid_y
elif flag == 1:
    centroid_nowaday_x = centroid_x
    centroid_nowaday_y = centroid_y
    if distance(centroid_origin_x, centroid_origin_y, centroid_nowaday_x, centroid_nowaday_y) < Maxdistance:
        centroid_normal_x.append(centroid_nowaday_x)
        centroid_normal_y.append(centroid_nowaday_y)
    else :
        centroid_abnormal_x.append(centroid_nowaday_x)
        centroid_abnormal_y.append(centroid_nowaday_y)
    if length_abnormal <= 2 and length_normal == 10:
        flag = 2
        centroid_final_x = np.sum(centroid_normal_x)/10
        centroid_final_y = np.sum(centroid_normal_y)/10
    elif length_abnormal >= 10 and length_normal <= 2:
        flag = 0
    elif length_abnormal >=10 and length_normal >= 10:
        flag = 3
    else:
        flag = 1
# Job done, return value
elif flag == 2:
    continue
# I think the most excetutable method is move the plane
elif flag == 3:
    continue































