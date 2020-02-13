import java.util.Scanner;

public class Test {

   public static void main(String[] args){
      Set set = new Set();
      Scanner sc = new Scanner(System.in);
      System.out.println("70-210");
      System.out.println("NAME: JOE");
      System.out.println("PROGRAMMING ASSIGNMENT 4 -SET");
      while(true) {
    	  	System.out.print("Enter command: ");
    	  	String command = sc.next();
    	  	int x = sc.nextInt();
    	  	if(command.equals("add")) {
    	  		set.add(x);
    	  		System.out.println(set);
    	  	}
    	  	else if(command.equals("del")) {
    	  		set.delete(x);
    	  		System.out.println(set);
    	  	}
    	  	else if(command.equals("exists")) {
    	  		System.out.println(set.exists(x));
    	  	}
    	  	else {
    	  		System.out.println("Unsupported command!");
    	  	}
      }
    }
}
