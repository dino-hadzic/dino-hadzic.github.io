import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int u = input.nextInt();
        int d = input.nextInt();
        int n = input.nextInt();
        int time = 0, dist = 0;
        while (true) {  // Beskonačna petlja za nabrajanje koraka
            dist += u;
            time++;
            if (dist >= n) {
                break;  // Kad je uvjet ispunjen, izađi iz petlje
            }
            dist -= d;
        }
        System.out.println(time);   // Ispiši rezultat
        input.close();
    }
}
