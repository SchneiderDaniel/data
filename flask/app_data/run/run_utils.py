
import random

def get_randomColors(number_of_colors):
    return ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
                for i in range(number_of_colors)]