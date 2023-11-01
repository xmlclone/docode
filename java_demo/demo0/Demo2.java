/*
E - Element (在集合中使用，因为集合中存放的是元素)
T - Type（Java 类）
K - Key（键）
V - Value（值）
N - Number（数值类型）
？ - 表示不确定的 java 类型
*/


class Box<T> {
    private T t;

    public Box() {}
    public Box(T t) {this.t = t;}

    public T getT() {return this.t;}
}


public class Demo2 {

    public static <E> void printArray(E[] array) {
        for (E e : array) {
            System.out.print(e);
            System.out.print(", ");
        }
        System.out.println("");
    }

    public static <T extends Comparable<T>> T max(T x, T y, T z) {
        T max = x;
        if (y.compareTo(max) > 0) {
            max = y;
        }
        if (z.compareTo(max) > 0) {
            max = z;
        }
        return max;
    }

    public static void main(String[] args) {
        // 注意不能使用int类型
        Integer[] arr1 = {1, 2, 3, 4};
        printArray(arr1);

        Double[] arr2= {1.2d, 2.5, 3.5};
        printArray(arr2);

        System.out.println(max(1, 2, 3));

        Box<Integer> box1 = new Box<Integer>(1);
        System.out.println(box1.getT());

    }
}
