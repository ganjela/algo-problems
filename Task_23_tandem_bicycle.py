def find_total_speed_tandem_bicycle(red_shirt_heights, blue_shirt_heights, fastest):
    total_speed = 0
    if fastest:
        red_shirt_heights.sort()
        blue_shirt_heights.sort()
        j = 0
        for i in range(len(blue_shirt_heights)-1, -1, -1):
            total_speed += max(red_shirt_heights[i], blue_shirt_heights[j])
            j += 1
    else:
        red_shirt_heights.sort()
        blue_shirt_heights.sort()
        for i in range(len(red_shirt_heights)):
            total_speed += max(red_shirt_heights[i], blue_shirt_heights[i])

    return total_speed