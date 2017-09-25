package zipzap;

public class ZipZap {

    /**
     * This method returns a Triple that contains the number of zips, zaps and
     * zipzaps that would be encountered between m and n in the Zip Zap Game.
     * (See problem statement.)
     * 
     * @param m
     *            the starting integer of the Zip Zap Game.
     * @param n
     *            the ending integer of the Zip Zap Game, n >= m.
     * @return a triple (a, b, c) where a represents the number of zips, b
     *         represents the number of zaps and c represents the number of
     *         zipzaps between m and n (both limits inclusive).
     */
    public static Triple countZZZs(Integer m, Integer n) {
        int a = 0, b = 0, c = 0;
        for (int num = m; num <= n; num++) {
            if (num % 5 == 0 && num % 3 == 0) {
                c++;
            } else if (num % 5 == 0) {
                b++;
            } else if (num % 3 == 0) {
                a++;
            }
        }
        return new Triple(a, b, c);
    }

}
