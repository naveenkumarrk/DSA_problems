public class recursion {
    public static void main(String[] args) {
        // System.out.println(fibo(4));
        // display(7);
        // even(1);
        int[] arr = {1,2,3,5,25,32,47,87,98};
        int target = 47;
        System.out.println(search(arr, target, 0, arr.length-1));
        

    }

    static int fibo(int n) {
        // base condition
        if (n < 2) {
            return n;
        }
        return fibo(n - 1) + fibo(n - 2);
    }

    static void display(int n) {
        if (n == 10) {
            return;
        }
        System.out.println(n);
        display(n + 1);
    }

    static void even(int n) {
        if (n == 10) {
            return;
        }
        System.out.println(n % 2 == 0 ? n : "");
        // System.out.println(n + " is " +( n % 2==0 ?"Even" : "odd"));
        even(n + 1);
    }

    static int search(int[] arr, int target, int s, int e ){
        if (s > e){
            return -1;
        }
        int mid = s + (e-s) /2;
        if (arr[mid] == target){
            return mid;
        }
        if (target > arr[mid]){
            return search(arr, target, mid +1, e);
        }
        
        return search(arr, target, s, mid-1);
        
    }
}