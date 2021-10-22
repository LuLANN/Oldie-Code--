/*
 * Lucy
 * Nov. 28 2018
 * Description: This class outlines the methods related for addition practice.
 */
import java.util.InputMismatchException; 
import java.util.Scanner;

public class Addition extends Arithmetic{
 
    public int getAnswer() {
        int answer = getLeftOperand() + getRightOperand();
        return answer;
    }
    @Override
    // overriding the inherited parent methods
    // getQuestion will return the question as a string
    public String getQuestion() {
        return getLeftOperand() + " + " + getRightOperand() + " = ";
    } 
    @Override
    public boolean checkAnswer(int answer) {
        //reusing the getAnswer() method  to evaluate the user's input
        return getAnswer() == answer;
    }
}