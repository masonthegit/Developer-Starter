package application;
	
import javafx.application.Application;
import static javafx.application.Application.launch;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.control.RadioButton;
import javafx.scene.control.ToggleGroup;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;

public class Main extends Application {

    //declaring important UI components

    private Circle red, yellow, green, blue;
    private RadioButton redBtn, yellowBtn, greenBtn, blueBtn;

    @Override

    public void start(Stage primaryStage) {

        //creating a Rectangle to represent the light box

        Rectangle rect = new Rectangle(50, 50, 100, 400);

        //using white color as background

        rect.setFill(Color.WHITE);

        //using black borders

        rect.setStroke(Color.BLACK);

        //creating four circles for the four lights, using no fill color, but

        //using black color for the outline
	
	//Setting Circle To Red

        red = new Circle(100, 100, 40);
        red.setFill(null);
        red.setStroke(Color.BLACK);
	
	//Setting Circle To Yellow

        yellow = new Circle(100, 200, 40);
        yellow.setFill(null);
        yellow.setStroke(Color.BLACK);
	
	//Setting Circle To Green

        green = new Circle(100, 300, 40);
        green.setFill(null);
        green.setStroke(Color.BLACK);
	
	//Setting Circle To Blue

        blue = new Circle(100, 400, 40);
        blue.setFill(null);
        blue.setStroke(Color.BLACK);

        //creating a group and adding the box and lights

        Group lights = new Group(rect, red, yellow, green, blue);

        //creating the four radio buttons

        redBtn = new RadioButton("Red");
        yellowBtn = new RadioButton("Yellow");
        greenBtn = new RadioButton("Green");
        blueBtn = new RadioButton("Blue");
       

        //using a ToggleGroup, so that only one can be selected at a time

        ToggleGroup group = new ToggleGroup();
        redBtn.setToggleGroup(group);
        yellowBtn.setToggleGroup(group);
        greenBtn.setToggleGroup(group);
        blueBtn.setToggleGroup(group);

        //adding action listener to all three radio buttons to call update method

        redBtn.setOnAction(e -> update());
        yellowBtn.setOnAction(e -> update());
        greenBtn.setOnAction(e -> update());
        blueBtn.setOnAction(e -> update());

        //creating an HBox using radio buttons, aligning center

        HBox buttons = new HBox(redBtn, yellowBtn, greenBtn, blueBtn);
	
	//gap between cells
	
        buttons.setSpacing(20);

        //creating a VBox containing lights and radio buttons hbox, aligning center

        buttons.setAlignment(Pos.CENTER);

        VBox root = new VBox(lights, buttons);
	
	//gap between cells

        root.setSpacing(20);

        root.setAlignment(Pos.CENTER);
	
	//padding

        root.setPadding(new Insets(20));

        //setting up and displaying the scene

        Scene scene = new Scene(root);
        primaryStage.setScene(scene);
        primaryStage.setTitle("Traffic Light");
        primaryStage.show();
    }

    //handler method which will be called when a radio button is clicked

    public void update() {

        //finding out which button is clicked and changing colors of circles

        if (redBtn.isSelected()) {

            //setting color of red circle to RED, remaining circles to null

            red.setFill(Color.RED);
            yellow.setFill(null);
            green.setFill(null);
            blue.setFill(null);

        } else if (yellowBtn.isSelected()) {

            red.setFill(null);
            yellow.setFill(Color.YELLOW);
            green.setFill(null);
            blue.setFill(null);

        } else if (greenBtn.isSelected()) {

            red.setFill(null);
            yellow.setFill(null);
            green.setFill(Color.GREEN);
            blue.setFill(null);

        } else {

            red.setFill(null);
            yellow.setFill(null);
            green.setFill(null);
            blue.setFill(Color.BLUE);

        }
    }
    public static void main(String[] args) {
        launch(args);
    }
}
