/*
 * Lucy
 * Nov. 28 2018
 * Description: This class outlines the methods related for addition practice.
 */

import java.util.Scanner; 

public class CopyAdditionTest {
    public static void main(String[] args) {
        
        int numQuestions = 0;
        boolean questionStatus = false;
        int counter = 1;
        int answer;
        int attempts = 0;
        
        Scanner input = new Scanner(System.in);
        Addition a = new Addition();
        
        
        while (questionStatus == false) {
            System.out.print("How many questions would you like (1-10) ?");
            numQuestions = input.nextInt();
            
            if (numQuestions < 0)  {
                System.out.print("You must enter an integer between 1 and 10.");
            }
            else {
                questionStatus = true;
                
            }
        }
        
        while (counter <= numQuestions) {
            System.out.print( "Q" + counter + ": " + a.getQuestion() );
            answer = input.nextInt();
            //String feedback;
            
//            if ( a.checkAnswer(answer) ) {
//                feedback = compliment(); 
//                System.out.print(feedback);
//            }
//            else {
//                feedback = critiscism(); 
//                System.out.print(feedback);
//                
//            }
            attempts += 1;
        }
        
        System.out.print("You answered " + numQuestions + " using " + attempts + " responses, your score is " + (attempts/numQuestions * 1.0) + "%.");
    }   
    
//    public String critiscism() {
//        int randomNum = Math.random(1,5);
//        
//        switch(randomNum) {
//            case 1: 
//                return s = "Correct!";
//                break;
//            case 2: 
//                return s = "Good work!";
//                break;
//            case 3: 
//                return s = "Nice job!";
//                break;
//            case 4: 
//                return s = "Keep up the good work!";
//                break;
//            default: 
//                return s = "";
//        }
//    }
//    
//    public String compliment() {
//        int randomNum = Math.random(1,5);
//        switch(randomNum) {
//            case 1: 
//                return s = "Incorrect!";
//                break;
//            case 2: 
//                return s = "You can do better!";
//                break;
//            case 3: 
//                return s = "Sorry, try again.";
//                break;
//            case 4: 
//                return s = "Um.. no.";
//                break;
//            default: 
//                return s = "";
//        }
//    }
 
}
   