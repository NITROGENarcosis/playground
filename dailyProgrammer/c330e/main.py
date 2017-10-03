data = [[1,1,2],
        [2,2,0.5],
        [-1,-3,2],
        [5,2,1]]

north=east=south=west = float(data[0][0])

for cir in data:
    n = float(cir[1] + cir[2])
    e = float(cir[0] + cir[2])
    s = float(cir[1] - cir[2])
    w = float(cir[0] - cir[2])
    if n > north :
        north = n
    if e > east :
        east = e
    if s < south :
        south = s
    if w < west :
        west = w

print( '(%f,%f) (%f,%f) (%f,%f) (%f,%f)' % (west, south, west, north, east, north, east, south) )