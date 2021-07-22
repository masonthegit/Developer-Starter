package application;

// Mason Becker
// 5/4/2021

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.stage.Stage;

import javafx.scene.control.TextField;
import javafx.scene.control.TextArea;
import javafx.scene.control.Button;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.Label;

import javafx.scene.layout.HBox;
import javafx.scene.layout.BorderPane;
import javafx.geometry.Pos;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;


public class Loan extends Application {
	protected TextField tfLoanAmount=new TextField(); // Accepts Loan Amount
	   protected TextField tfNumberOfYear=new TextField(); // Accepts Loan Period
	   protected TextArea txtArea=new TextArea();       // Show interest rate and payment

	public void start(Stage primaryStage) throws Exception {
	     
	   // Maximum width of control
	   tfNumberOfYear.setPrefColumnCount(2);
	   tfLoanAmount.setPrefColumnCount(7);
	   txtArea.setPrefColumnCount(30);

	   // Button to show result
	Button btnshow=new Button("Show Table");
	  
	// HBox layout add controls Text Field,Button and Label for message
	HBox panelforControl=new HBox(10);
	panelforControl.setAlignment(Pos.CENTER);
	panelforControl.getChildren().addAll(new Label("Loan amount "),tfLoanAmount,new Label("No Of Years "),
	       tfNumberOfYear,btnshow);

	//allow text area to scrollable
	ScrollPane spane =new ScrollPane(txtArea);

	// border layout add panelforControl and txtArea
	BorderPane pan=new BorderPane();
	pan.setTop(panelforControl);
	pan.setCenter(txtArea);

	// Main scene setup
	Scene scene = new Scene(pan);
	primaryStage.setTitle("Excersice"); // please set your title
	primaryStage.setScene(scene);   
	primaryStage.show();

	// event handler for button
	btnshow.setOnAction(new EventHandler<ActionEvent>() // BUTTON CLICK EVENT REGISTERED
	       {
	               @Override
	           public void handle(ActionEvent event)
	           {

	               print(); // Show Button onclick call print method.
	           }

	       }); // END EVENT ACTION
	} // end start

	private void print()
	{
	   String output=""; // output string to be diaplay on text area
	   Double monthlyInterestRate;
	   Double monthlyPayment;

	   output+= "Interest Rate   Monthly Payment       Total Payment\n";

	   //Interest rate and payment is calculated , displayed in tabular format
	   for(double i=5.0;i <=8.0 ;i+=0.125)
	   {
	       monthlyInterestRate=i/1200;
	       monthlyPayment=Double.parseDouble(tfLoanAmount.getText())*monthlyInterestRate /
	               ( 1- 1/Math.pow(1+monthlyInterestRate,Double.parseDouble(tfNumberOfYear.getText())*12 ) );

	       output   +=String.format("%-24.3f%-34.2f%-8.2f\n",i,monthlyPayment,
	               monthlyPayment*12*Double.parseDouble(tfNumberOfYear.getText()) );
	   }

	   txtArea.setText(output); // displayed on text area
	}

	public static void main(String args[]){
	launch(args);
	}   
}
