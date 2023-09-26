package org.example;

import java.util.Scanner;

public class Main {
    static private long CanTravelTimes(long m, long t) {
        long ans = m / (t * 2);
        if (m % (t * 2) >= t) {
            ans += 1;
        }
        return ans;
    }


    static private boolean isEnough(long m) {
        long s = 0;
        for (int i = 0; i < n; i++) {
            s += CanTravelTimes(m, time_to_travel[i]) * capacity[i];
            if (s >= w) {
                return true;
            }
        }
        return false;
    }

    static long[] capacity;
    static long[] time_to_travel;
    static int n;
    static int w;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        w = in.nextInt();

        capacity = new long[n];
        time_to_travel = new long[n];


        for (int i = 0; i < n; i++) {
            capacity[i] = in.nextInt();
            time_to_travel[i] = in.nextInt();
        }

        long l = -1;
        long r = (w / capacity[0] + 1) * 2 * time_to_travel[0]+1000;

        while (r - l > 1) {
            long m = (l + r) / 2;
            if (isEnough(m)) {
                r = m;
            } else {
                l = m;
            }
        }

        System.out.println(r);
    }
}