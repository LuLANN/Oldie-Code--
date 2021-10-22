/*
 * Lucy
 * Dec 12, 2018
 * Description: This class outlines the methods required for substraction practice.
 */

public class Subtraction extends Arithmetic{
    
    @Override
    // overriding the inherited parent methods
    // getQuestion will return the question as a string
    public String getQuestion() {
        return getLeftOperand() + " - " + getRightOperand() + " = ";
    } 
    
    public int getAnswer() {
        int answer = getLeftOperand() - getRightOperand();
        return answer;
    }
    @Override
    public boolean checkAnswer(int answer) {
        //reusing the getAnswer() method  to evaluate the user's input
        return getAnswer() == answer;
        
    }
}
