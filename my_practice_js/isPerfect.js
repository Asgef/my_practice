// Задача: "Проверка совершенного числа"
// Реализовать функцию isPerfect(), которая принимает число и возвращает true,
// если оно является совершенным, и false — в противном случае.
//
// Совершенное число — это положительное целое число, равное сумме всех его
// положительных делителей (кроме самого числа).
//
//
//
// Task: "Perfect Number Check"
// Implement the isPerfect() function that takes a number and returns true
// if it is a perfect number, and false otherwise.
//
// A perfect number is a positive integer that is equal to the sum of all its
// positive divisors (excluding the number itself).
//
// Examples:
// isPerfect(6);  // true (6 = 1 + 2 + 3)
// isPerfect(7);  // false
//


const isPerfect = (num) => {
    if (num <= 0) return false
    let sumDivisors = 0
    for (let i = 1; i <= Math.floor(num/2); i+= 1) {
        if (num % i === 0) {
            sumDivisors += i;
        }
    }
    return sumDivisors === num;
}

export default isPerfect;
