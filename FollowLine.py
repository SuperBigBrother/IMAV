# This is used for follow the line...

# This value shows the which square we come from
pre_index = 0

def follow_line(img_thre, rope_areas, pre_index):
    # flag = 1 shows we are still following lines
    # flag = 2 shows we have already finished our trip
    # flag = 3 shows we met a pole and this interrupt with our route
    flag = 0
    # This is used for save the area of each square
    areas = []
    # This value records the max & min area
    min_area = 0
    max_area = 0
    # This value record which square has the max area
    node = 1
    # This value record how amny blocks have zero area
    zero = 0
    # Check if there are poles block us
    avoid_poles()
    # flag = 1 code starts here...
    if flag == 1:
        for rope_area in rope_areas:
            if rope_area[5] != pre_index:
                rope_img = img_thre[rope_area[1]:(rope_area[1]+rope_area[3]),0:640]
                image, contours, hierarchy = cv2.findContours(rope_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
                for contour in contours:
                    if cv2.contourArea(contour) >= min_area:
                        if cv2.contourArea(contour) <= max_area:
                            area = area + cv2.contourArea(contour)
                areas.append(area)
        for area in areas:
            if area >= max_area:
                max_area = area
        for area in areas:
            if max_area != area:
                node = node + 1
        if node >= pre_index:
            node = node + 1
        pre_index = 8 - node
        # Check if we arrive the end of rope
        for i in range(0,6):
            if area[i] == 0:
                zero = zero + 1
        if zero == 7:
            flag = 2
        # Find the pre_index
        if node == 1: pre_index = 5
        elif node == 2: pre_index = 6
        elif node == 3: pre_index = 7
        elif node == 4: pre_index = 8
        elif node == 5: pre_index = 1
        elif node == 6: pre_index = 2
        elif node == 7: pre_index = 3
        elif node == 8: pre_index = 4
        if flag == 1: return 2,pre_index
    # Control code should starts here...

    # flag = 2 code starts here...
    if flag == 2:
        return 3,pre_index
    # flag = 3 code starts here...
    if flag == 3:
        return
































