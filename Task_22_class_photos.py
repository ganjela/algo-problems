"""
After sorting both classes by height, we can check which class is taller by comparing heights of the first persons.
Next, if anyone in the taller class is shorter than the person standing in front of them, we can't take photos.
"""
def can_photo_be_taken(red_shirt_heights, blue_shirt_heights):
    red_shirt_heights.sort()
    blue_shirt_heights.sort()
    taller_class = red_shirt_heights if red_shirt_heights[0] > blue_shirt_heights[0] else blue_shirt_heights
    shorter_class = blue_shirt_heights if taller_class == red_shirt_heights else red_shirt_heights

    for i in range(len(red_shirt_heights)):
        if taller_class[i] <= shorter_class[i]:
            return False

    return True