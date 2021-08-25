package array_shape;

public class Shape_array {
	public static void main(String[] args) {
		// Create an array of four objects
		GeometricObject[] array = {new Circle(5), new Circle(8),
			new Rectangle(3, 4), new Rectangle(4, 2)};

		System.out.println("The Sum Of The Area In This Array Is: " + sumArea(array));
	}

	public static double sumArea(GeometricObject[] a) {
		double sum = 0;
		for (int i = 0; i < a.length; i++) {
			sum += a[i].getArea();
		}
		return sum;
	}
}
