// Задача: "Числа Фибоначчи"
// Реализуйте и экспортируйте по умолчанию функцию fib(), которая вычисляет положительные
// числа Фибоначчи. Порядковый номер числа передается в качестве аргумента.
// Нумерация чисел начинается с нуля.
//
// Формула последовательности Фибоначчи:
// f(0) = 0
// f(1) = 1
// f(n) = f(n-1) + f(n-2)
//
//
// Task: "Fibonacci Numbers"
// Implement and export by default the function fib() that computes positive
// Fibonacci numbers. The argument is the index of the number in the sequence.
// The numbering in the sequence starts from zero.
//
// Formula for the Fibonacci sequence:
// f(0) = 0
// f(1) = 1
// f(n) = f(n-1) + f(n-2)
//
// Examples:
// fib(3);  // 2
// fib(5);  // 5
// fib(10); // 55
//


const fib = (n) => {
    if (n === 0) {return n}
    else if (n < 3) {return 1}
    else {
        return  fib(n - 2) + fib(n - 1)
    }
};

export default fib;
