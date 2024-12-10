// Задача: "Изменение регистра символов"
// Реализовать функцию, которая принимает строку и меняет регистр каждой буквы
// на противоположный. Функция должна возвращать изменённую строку.
//
//
// Подсказки:
// - Используйте свойство length для определения длины строки:
//   'example'.length; // 7
// - Метод toUpperCase() переводит символ в верхний регистр:
//   'a'.toUpperCase(); // 'A'
// - Метод toLowerCase() переводит символ в нижний регистр:
//   'B'.toLowerCase(); // 'b'

// Task: "Change Character Case"
// Implement a function that takes a string and toggles the case of each letter
// to the opposite. The function should return the modified string.
//
// Examples:
// invertCase('Hello, World!'); // hELLO, wORLD!
// invertCase('I loVe JS');     // i LOvE js
//
// Hints:
// - Use the `length` property to get the length of a string:
//   'example'.length; // 7
// - The `toUpperCase()` method converts a character to uppercase:
//   'a'.toUpperCase(); // 'A'
// - The `toLowerCase()` method converts a character to lowercase:
//   'B'.toLowerCase(); // 'b'


// @ts-check

const invertCase = (str) => {
    let result = ''

    for (let i = 0; i < str.length; i++) {

        switch (str[i]){
            case str[i].toLowerCase():
                result += str[i].toUpperCase();
                break;
            case str[i].toUpperCase():
                result += str[i].toLowerCase();
                break;
        }
    }
    return result;
};

export default invertCase;


// Teacher's decision

// const invertCase = (str) => {
//     let result = '';
//     for (let i = 0; i < str.length; i += 1) {
//         const isUpper = str[i] === str[i].toUpperCase();
//         result += isUpper ? str[i].toLowerCase() : str[i].toUpperCase();
//     }
//
//     return result;
// };
//
// export default invertCase;