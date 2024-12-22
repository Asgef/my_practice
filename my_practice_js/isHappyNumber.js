// Задача: "Счастливые числа"
// Реализуйте функцию isHappyNumber(), которая определяет, является ли число "счастливым".
// "Счастливое" число — это число, которое в результате последовательного применения
// операции "сумма квадратов цифр" становится равным единице. Процесс должен быть
// ограничен 10 итерациями.
//
//
// Примечания:
// - Число 1 считается счастливым.
// - Цепочки преобразований для несчастливых чисел могут зацикливаться.
//
// Task: "Happy Numbers"
// Implement the function isHappyNumber() that determines if a number is "happy".
// A "happy" number is a number that, after a series of transformations where
// each step replaces the number with the "sum of the squares of its digits,"
// eventually becomes 1. The process must be limited to 10 iterations.
//
// Examples:
// isHappyNumber(7); // true
// Transformation chain for the number 7:
// 7   => 7^2 = 49,
// 49  => 4^2 + 9^2 = 16 + 81 = 97,
// 97  => 9^2 + 7^2 = 81 + 49 = 130,
// 130 => 1^2 + 3^2 + 0^2 = 10,
// 10  => 1^2 + 0^2 = 1.
// Result: the number 7 is happy.
//
//
// Notes:
// - The number 1 is considered happy.
// - Transformation chains for unhappy numbers may form cycles.


const sumOfSquareDigits = (num) => {
    const numAsStr = String(num);
    let sum = 0;
    for (let i = 0; i < numAsStr.length; i += 1) {
        const digit = Number(numAsStr[i]);
        sum += digit * digit;
    }

    return sum;
};


const isHappyNumber = (number) => {
    let result = number;
    for (let i = 0; i <= 10; i+= 1) {
        result = sumOfSquareDigits(result);
        if (result === 1) return true;
    }
    return false
}

export default isHappyNumber;
