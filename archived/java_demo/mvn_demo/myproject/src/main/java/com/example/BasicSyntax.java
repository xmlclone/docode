package com.example;

// 本文举例一些基础语法，大部分语言通用的语法未在此全部列举，比如break continue等使用基本一致

public class BasicSyntax {
    public void demo1() {
        int a = 10;
        while (a > 0) {
            System.out.println(a);
            a--;
        }
    }

    public void demo2() {
        for (int i = 0; i < 10; ++i) {
            System.out.println(i);
        }

        int[] a = {10, 20, 30, 40, 50};
        // 类似python的for in
        for (int i : a) {
            System.out.println(i);
        }
    }

    public void demo3(int val) {
        if (val == 0) {
            System.out.println("val == 0");
        } else if (val > 0) { // 注意python是 elif
            System.out.println("val > 0");
        } else {
            System.out.println("val < 0");
        }
    }

    public void demo4() {
        // 数组
        int[] a = new int[5];
        int[] b = {1, 2, 3, 4, 5};
        System.out.printf("a length: %d, b length: %d\n", a.length, b.length);
        System.out.println("a length: " + a.length + ", b length: " + b.length);
    }

    public void demo5() {
        try {
            // throws 用于方法声明此方法可能抛出异常
            throw new Exception("Test exception");
        } catch (Exception e) { // python里面是 except
            e.printStackTrace();
        } finally {
            System.out.println("END");
        }
    }
}
