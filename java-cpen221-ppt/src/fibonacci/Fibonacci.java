package fibonacci;

import java.util.ArrayList;
import java.util.List;
import java.util.SortedSet;
import java.util.TreeSet;

public class Fibonacci {

    private static boolean isFib(int num) {
        if (num == 1 || num == 2 || num == 3) {
            return true;
        } else {
            double check1, check2;
            check1 = Math.sqrt((5 * (int) Math.pow(num, 2) + 4)) % 1;
            check2 = Math.sqrt((5 * (int) Math.pow(num, 2) - 4)) % 1;
            if ((check1 == 0 || check2 == 0) && !(check1 == 0 && check2 == 0)) {
                return true;
            } else {
                return false;
            }
        }
    }

    /**
     * Given an array of ints, this method returns a sorted List that contains
     * the Fibonacci numbers in the input list. The list returned contains the
     * Fibonacci numbers in ascending order and has no duplicates.
     * 
     * @param inputArray
     * @return a list of all the Fibonacci numbers in inputArray, in ascending
     *         order, with no duplicates. If the input array is null or does not
     *         contain any Fibonacci numbers then an empty list is returned.
     */
    public static List<Integer> getFibonacciNumbers_sorted(Integer[] inputArray) {
        //checks if inputArray is null first, then checks if it's empty
        if (inputArray == null || inputArray.length == 0){
            return new ArrayList<>();
        }
        SortedSet<Integer> fibNumbers = new TreeSet<>();
        for (Integer integer : inputArray) {
            if (isFib(integer)) {
                fibNumbers.add(integer);
            }
        }
        List<Integer> sortedFibArray = new ArrayList<>(fibNumbers.size());
        sortedFibArray.addAll(fibNumbers);
        return new ArrayList<>(sortedFibArray); // change this
    }

}
