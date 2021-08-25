package homework;

public class Assignment1 {
	public static void main(String[] args) {
		final int SLOW = 1;
		final int MEDIUM = 2;
		final int FAST = 3;
		Fan fan1 = new Fan();
		Fan fan2 = new Fan();
		fan1.setSpeed(FAST);
		fan1.setRadius(10);
		fan1.setColor("yellow");
		fan1.turnOn();
		fan2.setSpeed(MEDIUM);
		fan2.setRadius(5);
		fan2.setColor("blue");
		fan2.turnOff();
		System.out.println(fan1.toString());
		System.out.println(fan2.toString());
	}
}