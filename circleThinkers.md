# Thought proccess for movement

1. define the center of the circle
2. pick the starting point for the moving item
3. find the theta of the triangle made from the x axis and the height to get to
the point on the circle y is currently at.
4. Increase the theta by the speed you want to travel per tick
5. calculate new coordinates based on the sin and cos of that theta
6. move orbiting dot to the new coordinates
7. repeat proccess
