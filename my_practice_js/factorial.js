// Task: "Factorial"
// Write a recursive function to find the factorial of a number.
//
//
// Задача: "Факториал"
// Напишите рекурсивную функцию для нахождения факториала числа.
//
// Example:
// Input: 5
// Output: 120


const factorial = (n) => {
    if (n === 1) {
        return 1;
    }
    else {
        return n * factorial(n - 1);
    }
}

console.log(factorial(5))
