import java.util.Scanner;

public class test {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // Read input size
        int n = sc.nextInt();
        
        // Read the array
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        
        // Read number of allowed swaps
        int B = sc.nextInt();
        
        // Function call to get the largest lexicographical array
        int[] result = getLargestLexicographicalArray(arr, B);
        
        // Print the result array
        for (int num : result) {
            System.out.print(num + " ");
        }
    }
    
    public static int[] getLargestLexicographicalArray(int[] arr, int B) {
        int n = arr.length;
        
        for (int i = 0; i < n && B > 0; i++) {
            // Find the maximum element in the remaining unsorted part
            int maxIndex = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] > arr[maxIndex]) {
                    maxIndex = j;
                }
            }
            
            // If maxIndex is different from i, we perform a swap
            if (maxIndex != i) {
                // Perform the swap
                int temp = arr[i];
                arr[i] = arr[maxIndex];
                arr[maxIndex] = temp;
                
                // Decrement the number of allowed swaps
                B--;
            }
        }
        
        return arr;
    }
}