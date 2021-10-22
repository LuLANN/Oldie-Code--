/*
 * Lucy
 * Nov. 28 2018
 * Description: This class outlines the methods related for addition practice.
 */

import java.util.Scanner;
import java.io.IOException;
import java.util.InputMismatchException;

public class AdditionTest {
    public static void main(String[] args) {
        
        int numQuestions = 0;;
        boolean questionStatus = false;
        int counter = 1;
        int answer;
        int attempts = 0;
        
        Scanner input = new Scanner(System.in);
        
        while (questionStatus == false) {
           
            try {
                System.out.print("How many questions would you like (1-10) ?");
                numQuestions = input.nextInt();
                if (numQuestions >= 1 || numQuestions <= 10) {
                    questionStatus = true;
                }
                
            }
            
            catch ( InputMismatchException inputMismatchException ) {
                System.err.println("You must enter an integer between 1 and 10.");

            }
        }
        
        while (counter <= numQuestions) {
            
            // a new question object is created after every answer
            Addition a = new Addition();
            
            
            System.out.print( "Q" + counter + ": " + a.getQuestion() );
            answer = input.nextInt();
            
            
            if ( a.checkAnswer(answer)) {
               System.out.print(compliment() + "\n"); 
               
            }
            else {
               
               System.out.print( critiscism() + "\n");
               
            }
            attempts += 1;
            counter += 1;
        }
        
        System.out.print("You answered " + numQuestions + " using " + attempts + " responses, your score is " + (attempts/numQuestions * 1.0) + "%.");
    }   
    
public static String compliment() {
    int randomNum = (int)(Math.random() * 4 + 1);
    String s;  
    
    switch(randomNum) {
        case 1: 
            return s = "Correct!";
            
        case 2: 
            return s = "Good work!";
            
        case 3: 
            return s = "Nice job!";
            
        case 4: 
            return s = "Keep up the good work!";
           
        default: 
            return s = "Brilliant!";
       }
    }
    
    public static String critiscism() {
       int randomNum = (int)(Math.random() * 4 + 1);
       String s;    
       
       switch(randomNum) {
           case 1: 
               return s = "Incorrect!";
               
           case 2: 
               return s = "You can do better!";
               
           case 3: 
               return s = "Sorry, try again.";
               
           case 4: 
               return s = "Um.. no.";
               
           default: 
               return s = "Better Luck Next Time";
       }
   }
 
}
    
    