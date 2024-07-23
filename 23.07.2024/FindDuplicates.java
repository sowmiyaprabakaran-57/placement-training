import java.util.HashSet;
import java.util.Set;

public class FindDuplicates {
    public static Set<Integer> findDuplicates(int[] arr) {
        Set<Integer> seen = new HashSet<>();
        Set<Integer> duplicates = new HashSet<>();
        for (int num : arr) {
            if (!seen.add(num)) {
                duplicates.add(num);
            }
        }
        return duplicates;
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 2, 3, 6};
        System.out.println(findDuplicates(arr)); 
    }
}
