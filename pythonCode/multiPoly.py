class Point:
	def __init__(self, x_in, y_in):
		self.x = x_in
		self.y = y_in
		
	def __add__(self, pt):
		return Point(self.x + pt.x, self.y + pt.y)
		
	def __sub__(self, pt):
		return Point(self.x - pt.x, self.y - pt.y)
		
	def __mul__(self, n):
		return Point(self.x * n, self.y * n)
		
	def __div__(self, n):
		return Point(self.x / float(n), self.y / float(n))
		
		
p1 = Point(383866.047191507765092, 6356213.465902045369148)
p2 = Point(383877.274589003412984, 6356204.879094554111362)
p3 = Point(383876.218353001051582, 6356203.431660033762455)
p4 = Point(383864.932275729137473, 6356212.018467526882887)

poly = [p1, p2, p3, p4]

print "Poly: "
for i in range(0, 4):
	#print "P", i , "=", poly[i].x, poly[i].y
	print "P%d=%f %f" % (i, poly[i].x, poly[i].y)
	
numPV = 14

vec12 = p2 - p1
vec12 = vec12 / numPV
print (vec12.x, vec12.y)

#vec43 = Point(p3.x - p4.x, p3.y - p4.y)
vec43 = p3 - p4
vec43 = vec43 / numPV
print (vec43.x, vec43.y)


for i in range(0, 14):
	p1_s = p1 + (vec12 * i)
	p2_s = p1 + (vec12 * (i + 1))
	p3_s = p4 + (vec43 * (i + 1))
	p4_s = p4 + (vec43 * i)
	print "Poly", i
	print "[ %f, %f ]," % (p1_s.x, p1_s.y)
	print "[ %f, %f ]," % (p2_s.x, p2_s.y)
	print "[ %f, %f ]," % (p3_s.x, p3_s.y)
	print "[ %f, %f ]," % (p4_s.x, p4_s.y)
	print "[ %f, %f ]" % (p1_s.x, p1_s.y)
	print " "
	
	