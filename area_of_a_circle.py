def compute_area_of_circle(diameter):
	pi = 3.14
	area = (pi * (diameter ** 2))/4
	return area

diameter1 = 30
area1 = compute_area_of_circle(diameter1)
print(f"The area of circle with diameter {diameter1} is: {area1}")

diameter2 = 40
area2 = compute_area_of_circle(diameter2)
print(f"The area of circle with diameter {diameter2} is: {area2}")
