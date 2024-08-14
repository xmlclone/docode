package com.example;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );

        BasicSyntax basicSyntax = new BasicSyntax();
        basicSyntax.demo1();
        basicSyntax.demo2();
        basicSyntax.demo3(0);
        basicSyntax.demo3(1);
        basicSyntax.demo3(-1);
        basicSyntax.demo4();
        basicSyntax.demo5();
    }
}
