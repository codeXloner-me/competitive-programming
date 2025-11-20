#  7.Area Of Ellipse
#  Given the lengths of semi-major axis A and semi-minor axis B of an ellipse, calculate the Area
#  of the Ellipse.
#  Area of ellipse having semi-major axis length a and semi-minor axis length b is given by π * a *
#  b.
a, b = map(int, input().split())
area = 3.14 * a * b
print(area)
