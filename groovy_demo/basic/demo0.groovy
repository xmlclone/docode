
// 通过 groovy demo0.groovy运行即可

/*
 这是多行注释
 多行注释
*/


// 在同级目录下，导入java编写的代码，需要有class文件，不需要java和jar包
import DemoJava;
import DemoJava2;

class HelloWord {

    static def f1(a, b=0) {
        return a + b
    }

    def f2(a, b=0) {
        return a + b
    }

    // 类方法默认是public的
    static void main(String[] args) {
        println("Hello, world!")

        // 每行末尾的分号，也不是必须的
        byte a = 1;
        int b = 2;
        float c = 3.01f;
        long d = 12l;
        double e = 122.111;

        def f = "abc";
        // 可以使用+连接字符串与数字
        println("a: " + a + ", f: "+ f);


        def g = 1 + 2
        println("g: " + g)

        // 范围运算符(包含5和10)
        def h = 5..10
        println(h.get(0))


        // for
        for (int i = 0; i < 5; i++) {
            println("loop for: " + i)
        }

        for (i in 5..10) {
            println("loop for in: " + i)
        }

        // condition的()必须要
        if (a > 0) {
            println("a > 0")
        } else if (a < 0) {
            println("a < 0")
        } else {
            println("a = 0")
        }


        println("static function f1: " + f1(1));
        def obj = new HelloWord();
        println("class function f2: " + obj.f2(1, 2));


        println("java jar static fun: " + DemoJava.add(1, 2));
        println("java jar instance fun: " + new DemoJava().add(1, 2, 3));

        println("java source instance fun: " + new DemoJava2().add(1, 2, 3));
        // println(instance f);
    }
}