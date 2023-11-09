/*
 * javac DemoJava.java
 * 注意创建自己的MF文件
 * jar cvmf MANIFEST.MF DemoJava.jar DemoJava.class
 */

public class DemoJava {
    public static int add(int a, int b) {
        return a + b;
    }

    public int add(int a, int b, int c) {
        return a + b + c;
    }
}
