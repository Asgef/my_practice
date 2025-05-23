// @ts-check
import reverseInt from '../reverseInt.js';

test('reverseInt', () => {
    expect(reverseInt(12)).toBe(21);
    expect(reverseInt(-122)).toBe(-221);
    expect(reverseInt(8900)).toBe(98);
});
