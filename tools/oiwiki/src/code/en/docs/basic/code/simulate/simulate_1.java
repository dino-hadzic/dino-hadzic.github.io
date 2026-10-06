import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int u = input.nextInt();
        int d = input.nextInt();
        int n = input.nextInt();
        int time = 0, dist = 0;
        while (true) {  // Infinite loop to enumerate the steps
            dist += u;
            time++;
            if (dist >= n) {
                break;  // Leave the loop once the condition is met
            }
            dist -= d;
        }
        System.out.println(time);   // Print the result
        input.close();
    }
}
