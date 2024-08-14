/*
 * 1. 接口支持多继承，类不支持，但类支持实现多个接口
 * 2. 多态形成的3要素： 继承、重写、父类引用执行之类实例
 */

interface Animal {
    public void eat();  
}

// 接口是支持多继承的
interface IPerson extends Animal {
    public void stand();
}

class Person {
    private int age;
    private String name;

    public Person() {}

    public Person(int age, String name) {
        this.name = name;
        this.age = age;
    }

    public int getAge() {
        return this.age;
    }

    public String getName() {
        return this.name;
    }
}

// java不支持多继承，但可以实现多个接口
class Student extends Person implements IPerson {
    private int grade;

    public Student(int age, String name, int grade) {
        super(age, name);
        this.grade = grade;
    }

    public int getGrade() {
        return this.grade;
    }

    public String getName() {
        return super.getName().toUpperCase();
    }

    public void eat() {
        System.out.println("eat");
    }

    public void stand() {
        System.out.println("stand");
    }
}


public class Demo1 {
    public static void main(String[] args) {
        Student student1 = new Student(10, "xiaoming", 2);
        System.out.printf("age: %d, grade: %d, name: %s\n", student1.getAge(), student1.getGrade(), student1.getName());
        student1.eat();
        student1.stand();

        // 多态
        // 继承+重写+父引用指向子类
        Person stuPerson1 = new Student(10, "xiaohua", 3);
        System.out.println(stuPerson1.getName());
    }
}
