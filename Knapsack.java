import java.util.ArrayDeque;
import java.util.Deque;

public class Test
{
    public static int knapSack(int[] members, int[] profits, char[] names, int n, int capacity, Deque<Integer> groups, Deque<Character> groupNames)
    {
        /**
         * This method solves a 0-1 knapsack problem where groups of people need to be loaded into five buses in the most profitable way possible.
         * @param members integer array for storing members
         * @param profits integer array for storing weights
         * @param names char array for storing group names
         * @param n integer for storing number of groups to choose from
         * @param capacity integer for storing bus capacity
         * @param groups queue for storing group profits
         * @param groupNames queue for storing group names
         * @return the profit made on a bus
        */

        // Base case for a negative capacity
        if (capacity < 0) {
            return Integer.MIN_VALUE;
        }

        // Base case for no remaining groups or if capacity = 0
        if (n < 0 || capacity == 0) {
            return 0;
        }

        // Backup current groups to queue
        Deque<Integer> originalGroups = new ArrayDeque<>(groups);
        Deque<Character> originalNames = new ArrayDeque<>(groupNames);

        // Either
        // Add current group to queue and recur for remaining groups with decreased capacity
        groups.addLast(members[n]);
        groupNames.addLast(names[n]);
        int add = members[n] + knapSack(members, profits, names, n - 1, capacity - profits[n], groups, groupNames);

        // Or
        // Leave current group and recur for remaining groups
        int leave = knapSack(members, profits, names, n - 1, capacity, originalGroups, originalNames);

        // Return maximum value by adding or leaving current group
        if (add > leave) {
            return add;
        }

        else {
            groups.clear();
            groupNames.clear();
            groups.addAll(originalGroups);
            groupNames.addAll(originalNames);
            return leave;
        }
    }

    public static void main(String[] args)
    {
        // Input data
        char[] names = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O'};
        int[] members = {48,30,32,36,36,48,42,42,36,24,30,30,42,36,36};
        int n = members.length;
        int[] weights = {100,300,250,500,350,300,150,400,300,350,450,100,200,300,250};
        
        // Data for profit to be made from each group
        int[] profits = new int[n];
        for (int i=0; i<n;i++)
        {
            profits[i] = (weights[i]-100)*5;
        }

        // If found, deque to store the groups in queue
        Deque<Integer> groups = new ArrayDeque<>();
        Deque<Character> groupNames = new ArrayDeque<>();

        // Bus capacity
        int capacity = 100;

        System.out.println("Profit on bus is R" + knapSack(profits, members, names, n - 1, capacity, groups, groupNames));

        System.out.println("Bus groups are " + groupNames);
    }
}
