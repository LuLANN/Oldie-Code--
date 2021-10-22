/*
 * Lucy
 * Nov. 28 2018
 * Description: This class outlines the code needed to set up, display, and evaluate questions.
 */

import java.util.Scanner;
import java.util.InputMismatchException;

public class ArithmeticTest {

    public static void main(String[] args) {
        // setting up the variables that will be used in the loops below
        boolean answerCheck = false;
        String unknownQuestion = "";
        int questionCounter = 1;
        int answer;
        int attempts = 0;
        int userInput = 0;
        int numQuestion = 0;
        int mathOption = 0;
        int mixCounter = 0;
        
        Scanner input = new Scanner(System.in);
        // The range of questions alongside the display message is passed into inputCheck() 
        // inputCheck will then return the number of requested questions which will be referenced by the variable numQuestions
        String prompt = "How many questions would you like (1-10) ?";
        numQuestion = inputCheck(1,10, prompt);

        String prompt2 ="What would you like to practice?\n1. Addition only\n2. Subtraction only\n3. Multiplication only\n4. Random mix (all three types)\n\nChoice: ";
        mathOption = inputCheck(1,4, prompt2);
        
        // This while loop will reiterate and instantiate a child object for every question requested. 
        while (questionCounter <= numQuestion) {
            // Using polymorphism to instantiate a parent object and assigning it to a child object
            Arithmetic parent = new Addition(); 
            if (mathOption == 1) {
                parent = new Addition();
            }
            else if (mathOption == 2) {
                parent = new Subtraction();
            }
            else if (mathOption == 3) {
                parent = new Multiplication();
            }
            else {
                // these if statements will instantiate any one of the child class based on an random integer from 1 to 3 
                int randomQ = (int)(Math.random() * 3 + 1);
                if (randomQ == 1) {
                    parent = new Addition();
                }
                else if (randomQ == 2)  {
                    parent = new Subtraction();
                }
                else  {
                    parent = new Multiplication();
                }
            }
            boolean redo = true;
            // this loop evaluate the user's answer and will reiterate if incorrect
            while (redo) {
                
                try { 
                    System.out.print( "Q" + questionCounter + ": " + parent.getQuestion() );
                    answer = input.nextInt();
                    attempts += 1;
                    
                    // calling an inherited method to evaluate the user's answer
                    if (parent.checkAnswer(answer)) {
                        System.out.print(compliment() + "\n");
                        questionCounter += 1;
                        // if the answer is correct, the loop ends
                        redo = false;
                    }
                    else {
                        // but if the answer is incorrect, feedback is given and the loop reiterates
                        System.out.print( critiscism() + "\n");
                    }
                }
                catch ( InputMismatchException inputMismatchException ) {
                    System.err.println("You must enter an integer.");
                    attempts += 1;
                    input.nextLine();
                }
            }
        }
        // displaying the user's result
        System.out.printf("You answered " + numQuestion + " question(s) using " + attempts + " responses, your score is %5.2f%%.\n", (numQuestion * 1.0/attempts *100 ));
    }

//inputCheck will run a while loop that will collect and evaluate user input and catch exceptions if necessary. 
private static int inputCheck(int min, int max, String message) {
    Scanner input = new Scanner(System.in);
    boolean loopStatus = false;
    int userInput = 0;
    
    while (loopStatus == false) {
        try {
            // display prompt 
            System.out.print(message);
            //collect input
            userInput = input.nextInt();
            // evaluate if input is within range
            if ((userInput >= min) && (userInput <= max)) {
                // if it is, the loop ends, if not it reiterates
                loopStatus = true;
            }
        }
        catch ( InputMismatchException inputMismatchException ) {
            System.err.println("You must enter an integer between " + min + " and " + max + "." );
            input.nextLine();
        }
    }
    // If appropriate, the number of questions is returned 
    return userInput;
}   

// This helper method will return a positive message when an correct answer is given. 
private static String compliment() {
    int randomNum = (int)(Math.random() * 4 + 1);
    String s;  
    
    switch(randomNum) {
        case 1: return s = "Correct!";
            
        case 2: return s = "Good work!";
            
        case 3: return s = "Nice job!";
            
        case 4: return s = "Keep up the good work!";
            
        default: return s = "You're a star!";
            
       }
    }

// This helper method will return feedback when an incorrect answer is given. 
private static String critiscism() {
    int randomNum = (int)(Math.random() * 4 + 1);
    String s;    
       
    switch(randomNum) {
        case 1: return s = "Incorrect!";
            
        case 2: return s = "You can do better!";
            
        case 3: return s = "Sorry, try again.";
           
        case 4: return s = "Um.. no.";
            
        default: return s = "Don't give up!";
            
        }
    }
}