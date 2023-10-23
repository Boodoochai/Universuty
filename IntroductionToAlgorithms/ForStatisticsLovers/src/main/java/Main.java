import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        Map<Integer, List<Integer>> population_in_cities = handleInput(in);

        String answer = processQueries(in, population_in_cities);

        System.out.println(answer);
    }

    private static String processQueries(Scanner in, Map<Integer, List<Integer>> population_in_cities) {
        int query_num = in.nextInt();
        char[] answer = new char[query_num];
        for (int i = 0; i < query_num; i++) {
            Query query = Query.makeQueryFromInput(in);
            boolean query_process_result = processQuery(population_in_cities, query);
            if (query_process_result) {
                answer[i] = '1';
            } else {
                answer[i] = '0';
            }
        }
        return new String(answer);
    }

    private static boolean processQuery(Map<Integer, List<Integer>> population_in_cities, Query query) {
        if (!population_in_cities.containsKey(query.population)) {
            return false;
        }
        int upper_bound = upperBound(population_in_cities.get(query.population), query.left_bound);
        if (upper_bound == -1) {
            return false;
        }
        return upper_bound <= query.right_bound;
    }

    private static Map<Integer, List<Integer>> handleInput(Scanner in) {
        int n = in.nextInt();
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int city_population = in.nextInt();
            if (!map.containsKey(city_population)) {
                map.put(city_population, new ArrayList<Integer>());
            }
            map.get(city_population).add(i);
        }
        return map;
    }

    private static int upperBound(List<Integer> list, int num) {
        int l = -1;
        int r = list.size();
        while (r - l > 1) {
            int m = (r + l) / 2;
            if (list.get(m) < num) {
                l = m;
            } else {
                r = m;
            }
        }
        if (r == list.size()) {
            return -1;
        }
        return list.get(r);
    }

    private static class Query {
        public int left_bound;
        public int right_bound;
        public int population;

        private Query(int left_bound, int right_bound, int population) {
            this.left_bound = left_bound;
            this.right_bound = right_bound;
            this.population = population;
        }

        public static Query makeQueryFromInput(Scanner in) {
            return new Query(in.nextInt() - 1, in.nextInt() - 1, in.nextInt());
        }
    }
}
