import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ArrayList<Long> numbers = new ArrayList<>();

        for (int i = 0; i < 60; i++) {
            for (int j = 0; j < 50; j++) {
                for (int k = 0; k < 50; k++) {
                    BigInteger x = BigInteger.valueOf(1);
                    x = x.multiply(BigInteger.valueOf(2).pow(i));
                    x = x.multiply(BigInteger.valueOf(3).pow(j));
                    x = x.multiply(BigInteger.valueOf(5).pow(k));
                    if (x.compareTo(BigInteger.valueOf(10).pow(18)) < 0) {
                        numbers.add(x.longValue());
                    }
                }
            }
        }

        Collections.sort(numbers);
        Scanner in = new Scanner(System.in);
        int numbersToPrint = in.nextInt();
        for (int i = 1; i < numbersToPrint + 1; i++) {
            System.out.println(numbers.get(i));
        }
    }
}