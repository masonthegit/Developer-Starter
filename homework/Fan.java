package homework;

public class Fan {
	final static int SLOW = 1;
	final static int MEDIUM = 2;
	final static int FAST = 3;
	private int speed;
	private boolean on;
	private double radius;
	String color;
Fan() {
	speed = SLOW;
	on = false;
	radius = 5;
	color = "blue";
}
public void setSpeed(int newSpeed) {
	speed = newSpeed;
}
public void turnOn() {
		on = true;
}
public void turnOff() {
		on = false;
}
public void setColor(String newColor) {
	color = newColor;
}
public void setRadius(double newRadius) {
	radius = newRadius;
}
public String getSpeed() {
	String s = "";
	switch (speed) {
		case SLOW: s = "SLOW"; break;
		case MEDIUM: s = "MEDIUM"; break;
		case FAST: s = "FAST";
	}
	return s;
}
public boolean isOn() {
	return on;
}
public double getRadius() {
	return radius;
}
public String getColor() {
	return color;
}
public String toString() {
	if (on == true) {
		return "\nThe Fan Speed Is: " + getSpeed() + ", The Color Is: " + color + ",The Radius Is: " + radius + "\n";
	}
	else{
		return "\nThe Fan Color Is: " + color + ", The Radius Is: " + radius + "\nThe Fan Is Off\n";
	}
}
}
