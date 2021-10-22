/*
 * Lucy
 * Jan 3, 2018
 * Description: This class outlines the parent methods related for arithmetic practice.
 */
import java.util.InputMismatchException; 
import java.util.Scanner;

// Since Arithmetic is an abstract class, an Arithmetic object cannot be instantiated.
abstract public class Arithmetic {
    
    // setting up private variables
    private int leftOperand;
    private int rightOperand;
    
    // this default constructor will pass two random integers to be assigned in setLeft/RightOperand()
    public Arithmetic() {
        setLeftOperand( (int)(Math.random() * 9 + 1)  );
        setRightOperand( (int)(Math.random() * 9 + 1) );
    }
   
     // accepts an integer parameter and if appropriate assigns it to the variable rightOperand or leftOperand 
    public void setLeftOperand( int operand) {
        leftOperand = operand;
        if (leftOperand < 0) {
            System.err.println("Setting the operand to 1");
            leftOperand = 1;
        }
    }
    public void setRightOperand( int operand) {
        rightOperand = operand;
        if (rightOperand < 0) {
            System.err.println("Setting the operand to 1");
            rightOperand = 1;
        }
    }
    
    // returns an integer value
    public int getLeftOperand() {
        return leftOperand;
    }
    public int getRightOperand() {
        return rightOperand;
    }
    
    // each child class will inherit these two methods from Arithmetic but will eventually override them
    public abstract String getQuestion();
    public abstract boolean checkAnswer(int answer);
}
        