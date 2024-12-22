// Задача: "Переворачивание числа"
// Реализуйте и экспортируйте по умолчанию функцию, которая переворачивает цифры
// в переданном числе и возвращает новое число.
//
//
// Примечания:
// - Убедитесь, что функция работает корректно для отрицательных чисел и чисел с нулями в конце.
//
// Task: "Reversing a Number"
// Implement and export by default a function that reverses the digits
// in the given number and returns the new number.
//
// Examples:
// reverseInt(13);    // 31
// reverseInt(-123);  // -321
// reverseInt(8900);  // 98
//
//
// Notes:
// - Ensure the function handles negative numbers and numbers with trailing zeros correctly.


const reverseInt = (number) => {
    const numToReverseString = number.toString().split('').reverse().join('');
    return number > 0? parseInt(numToReverseString) : - parseInt(numToReverseString);
}

export default reverseInt;

// Teacher's decision
//
// const reverseInt = (num) => {
//     const numAsStr = String(Math.abs(num));
//     let reversedStr = '';
//
//     for (let i = numAsStr.length - 1; i >= 0; i -= 1) {
//         reversedStr += numAsStr[i];
//     }
//     const reversedModule = Number(reversedStr);
//
//     return num < 0 ? -reversedModule : reversedModule;
// };
