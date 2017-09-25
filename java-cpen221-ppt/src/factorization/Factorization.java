package factorization;

import java.util.ArrayList;
import java.util.List;

public class Factorization {

    /**
     * Given an integer n, this method returns a string that represents the
     * prime factorization of n.
     * 
     * The prime numbers that are factors of n must appear in ascending order in
     * the returned string.
     * 
     * <p>
     * Examples:
     * </p>
     * <ul>
     * <li>N = 8. The returned string should be "2^3" where "^" refers to
     * exponentiation.</li>
     * 
     * <li>N = 12. The returned string should be "2^2 * 3" where "*" represents
     * multiplication.</li>
     * 
     * <li>N = 7. The returned string should be "7".</li>
     * 
     * <li>N = 1764. The returned string should be "2^2 * 3^2 * 7^2".</li>
     * 
     * <li>N = 210. The returned string should be "2 * 3 * 5 * 7".</li>
     * 
     * <li>N = 1. The returned string should be "1". Note that 1 is a special
     * case because 1 is not considered a prime number.</li>
     * </ul>
     * 
     * @param n
     *            should be greater than or equal to 1.
     * @return a String that represents the proper prime factorization of N with
     *         the prime factors in ascending order and with the correct
     *         exponents. Exponentiation is indicated using ^ and multiplication
     *         using *. White space between symbols is maintained as per the
     *         examples.
     */
    public static String getPrimeFactorization(Integer n) {
        if (n.equals(1)) {
            return "1";
        }
        StringBuffer equation = new StringBuffer();
        List<Integer> sortedFactors = new ArrayList<>();
        for (int i = 2; i <= n; i++) {
            while (n % i == 0) {
                sortedFactors.add(i);
                n /= i;
            }
        }
        if (n > 1) {
            sortedFactors.add(n);
        }
        System.out.println(sortedFactors);
        int exponent = 1;
        for (int index = 0; index < sortedFactors.size(); index++) {
            if (index + 1 != sortedFactors.size()) {
                if (sortedFactors.get(index) == sortedFactors.get(index + 1)) {
                    exponent++;
                } else {
                    equation.append(sortedFactors.get(index));
                    if (exponent > 1) {
                        equation.append("^");
                        equation.append(exponent);
                        exponent = 1;
                        equation.append(" * ");
                    } else {
                        equation.append(" * ");
                    }
                }
            }
            else {
                equation.append(sortedFactors.get(index));
            }
        }
        if (exponent > 1){
            equation.append("^");
            equation.append(exponent);
        }
        return equation.toString();
    }

}