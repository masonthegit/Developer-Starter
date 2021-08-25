package array_shape;

public class Circle

extends GeometricObject implements Comparable<Circle> {
		private double radius;
		public Circle() {
		}
	public Circle(double radius) {
		this.radius = radius;
	}
	public Circle(double radius, 
			String color, boolean filled) {
			this.radius = radius;
			setColor(color);
			setFilled(filled);
		}
	public double getRadius() {
		return radius;
	}
	public void setRadius(double radius) {
		this.radius = radius;
	}
	@Override
	public double getArea() {
		return radius * radius * Math.PI;
	}
	public double getDiameter() {
		return 2 * radius;
	}
	@Override
	public double getPerimeter() {
		return 2 * radius * Math.PI;
	}
	@Override
	public boolean equals(Object o) {
		return this.compareTo((Circle)o) == 0;
	}

	@Override
	public int compareTo(Circle o) {
		if (this.radius > o.radius)
			return 1;
		else if (this.radius < o.radius)
			return -1;
		else
			return 0;
	}

	@Override
	public String toString() {
		return super.toString() + "\nDate created: " + getDateCreated() +
			"\nRadius: " + radius;
	}
}