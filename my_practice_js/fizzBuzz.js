// Задача: "FizzBuzz"
// Реализовать функцию, которая выводит в терминал числа из диапазона от begin до end.
// При этом:
// - Если число делится на 3, вместо него выводится слово Fizz.
// - Если число делится на 5, вместо него выводится слово Buzz.
// - Если число делится и на 3, и на 5, вместо него выводится FizzBuzz.
// - В остальных случаях выводится само число.
// Если диапазон пуст (begin > end), функция ничего не выводит.
//
//


// Task: "FizzBuzz"
// Implement a function that prints numbers from the range begin to end to the terminal.
// Rules:
// - If a number is divisible by 3, print Fizz instead of the number.
// - If a number is divisible by 5, print Buzz instead of the number.
// - If a number is divisible by both 3 and 5, print FizzBuzz instead of the number.
// - Otherwise, print the number itself.
// If the range is empty (begin > end), the function should not print anything.
//
// Example:
// fizzBuzz(11, 20);
// Output:
// 11
// Fizz
// 13
// 14
// FizzBuzz
// 16
// 17
// Fizz
// 19
// Buzz
//


const fizzBuzz = (begin, end) => {
    for (let i = begin; i <= end; i += 1) {
        if (((i % 3) === 0) && ((i % 5) === 0)) {
            console.log('FizzBuzz');
        } else if ((i % 3) === 0) {
            console.log('Fizz');
        } else if ((i % 5) === 0) {
            console.log('Buzz');
        } else {
            console.log(i);
        }
    }
}


export default fizzBuzz;


// Teacher's decision

// const fizzBuzz = (begin, end) => {
//     for (let i = begin; i <= end; i += 1) {
//         const hasFizz = i % 3 === 0 ? 'Fizz' : '';
//         const hasBuzz = i % 5 === 0 ? 'Buzz' : '';
//         console.log(`${hasFizz}${hasBuzz}` || i);
//     }
// };