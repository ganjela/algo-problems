"""
To get the maximum total speed we need to pair faste team members with the slow ones .
and if we want minimum we do otherwise we pair fast red team members with also fast blue team members.
for example if we have red team members [1,2,5] and blue team members [3,4,6]

we don't pair 5 with 6 if we want maximum total speed. the reason is that we could pair 5 with 3,
In which case we take advantage of the faster team member.
"""
def find_total_speed_tandem_bicycle(red_shirt_heights, blue_shirt_heights, fastest):
    total_speed = 0
    red_shirt_heights.sort()
    blue_shirt_heights.sort()
    if fastest:
        j = 0
        for i in range(len(blue_shirt_heights)-1, -1, -1):
            total_speed += max(red_shirt_heights[i], blue_shirt_heights[j])
            j += 1
    else:
        for i in range(len(red_shirt_heights)):
            total_speed += max(red_shirt_heights[i], blue_shirt_heights[i])

    return total_speed