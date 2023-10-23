import java.util.LinkedList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int number = in.nextInt();

        LinkedList<LinkedList<Integer>> sequences = new LinkedList<>();

        LinkedList<Integer> initSequence = new LinkedList<>();
        initSequence.add(1);

        Solve(sequences, initSequence, 1, number);

        while (!sequences.isEmpty()) {
            LinkedList<Integer> curSequence = sequences.pollFirst();
            while (!curSequence.isEmpty()) {
                System.out.print(curSequence.pollFirst());
                System.out.print(" ");
            }
            System.out.println();
        }
    }

    public static void Solve(LinkedList<LinkedList<Integer>> sequences, LinkedList<Integer> prefix, int prefix_sum, int number) {
        if (prefix_sum == number) {
            sequences.addLast((LinkedList<Integer>) prefix.clone());
            return;
        }
        for (int i = prefix.getLast() + 1; i < number; i++) {
            if (() && (prefix.getLast() % 2 != i)) {
                prefix.addLast(i);
                Solve(sequences, prefix, prefix_sum + i, number);
                prefix.removeLast();
            }
        }
    }
}