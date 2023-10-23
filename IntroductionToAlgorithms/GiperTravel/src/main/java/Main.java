import java.util.Scanner;

import static java.lang.Math.max;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int gravitationalPotentialsNumber = in.nextInt();
        int currentSum = 0;
        int maxSum = 0;
        for (int i = 0; i < gravitationalPotentialsNumber; i++) {
            int currentPotential = in.nextInt();
            currentSum += currentPotential;
            if (currentSum < 0) {
                currentSum = 0;
            }
            maxSum = max(currentSum, maxSum);
        }
        System.out.println(maxSum);
    }
}