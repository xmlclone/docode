// 单行注释

/*
多行注释
多行注释
*/


a = 1
var b = 2
const c = 3
let d = 4
e = true
f = false
g = null
h = undefined
console.log(a, b, c, d, e, f, g, h)
// number boolean false    --> instanceof适用于对象
console.log(typeof(a), typeof(e), a instanceof Number)


// js字符串只有下面两种，python可以使用三引号的方式
s1 = '123'
s2 = "456"
// js可以直接通过+连接字符串和其它类型，python则不行(需要通过字符串格式化的方式处理)
console.log(s1 + s2 + e)


array1 = ['a', 'b', 'c', 'd']
// 数组长度
console.log(array1.length)


for (i=0; i< array1.length; i++) {
    console.log("for array: " + array1[i])
}
for (i in array1) {
    // 这里的i仍然是一个索引
    console.log("for in: " + array1[i])
}
for (i of array1) {
    // for of获取到的就是值
    console.log("for of: " + i)
}


a = true
b = false
c = null
// if (a) &


function f1(){
    console.log("f1")
}
// 匿名函数
var f2 = () => console.log("f2")
var f3 = (a, b=2) => {
    console.log("f3: " + a)
    console.log("f3: " + b)
}
// js参数可以随意传递
f1(123)
f2()
// 但不能通过关键字参数传递一个不存在的，比如c=3会报错，但是可以直接传3
f3(a=1, b=2, 3)


export var ev1 = 1
