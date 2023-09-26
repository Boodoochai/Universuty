import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] stars_x = new int[n];
        int[] stars_y = new int[n];

        for (int i = 0; i < n; i++) {
            stars_x[i] = in.nextInt();
            stars_y[i] = in.nextInt();
        }

        int[][] stars_in_rect_in_cord = new int[1000][1000];
        int[] stars_in_rect = new int[1000];

        int[] levels = new int[n];

        for (int i = 0; i < n; i++) {
            int cur_x = stars_x[i];
            int cur_rect = cur_x / 1000;
            int cur_x_in_rect = cur_x - cur_rect * 1000;
            int level = 0;
            for (int j = 0; j < cur_rect; j++) {
                level += stars_in_rect[j];
            }
            for (int j = 0; j <= cur_x_in_rect; j++) {
                level += stars_in_rect_in_cord[cur_rect][j];
            }
            stars_in_rect_in_cord[cur_rect][cur_x_in_rect] += 1;
            stars_in_rect[cur_rect] += 1;
            levels[level] += 1;
        }

        for (int i = 0; i < n; i++) {
            System.out.println(levels[i]);
        }
    }
}