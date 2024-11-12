export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = name;
    if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = length;

    if (!Array.isArray(students) || !students.every((students) => typeof students === 'string')) {
      throw new TypeError('Student must be an array of string');
    }
    this._students = students;
  }
}
