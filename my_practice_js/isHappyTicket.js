// Задача: "Проверка счастливого билета"
// Реализовать функцию isHappyTicket(), которая принимает номер билета (строку)
// и возвращает true, если билет счастливый, или false — в противном случае.
//
// "Счастливым" называют билет, в котором сумма первой половины цифр равна
// сумме второй половины. Номер билета всегда строка чётной длины.
//
//
// Task: "Happy Ticket Check"
// Implement the isHappyTicket() function that takes a ticket number (string)
// and returns true if the ticket is happy, or false otherwise.
//
// A "happy ticket" is a ticket where the sum of the first half of the digits
// equals the sum of the second half. Ticket numbers are always strings of even length.
//
//
// Examples:
// isHappyTicket('385916'); // true (3 + 8 + 5 === 9 + 1 + 6)
// isHappyTicket('231002'); // false (2 + 3 + 1 !== 0 + 0 + 2)
// isHappyTicket('1222');   // false
// isHappyTicket('054702'); // true
// isHappyTicket('00');     // true
//


const isHappyTicket = (string) => {
    let firstSum = 0
    let secondSum = 0
    for (let i = 0; i < string.length; i+= 1) {
        if (i < (string.length / 2)) {
            firstSum += Number(string[i])
        } else {
            secondSum += Number(string[i])
        }
    }
    return firstSum === secondSum
};

export default isHappyTicket;


// Teacher's decision

// export default (num) => {
//     let balance = 0;
//
//     for (let i = 0, j = num.length - 1; i < j; i += 1, j -= 1) {
//         balance += parseInt(num[i]) - parseInt(num[j]);
//     }
//     return balance === 0;
// };