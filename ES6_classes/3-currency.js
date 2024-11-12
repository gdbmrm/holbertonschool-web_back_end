/* eslint-disable no-underscore-dangle */
export default class HolbertonCourse {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  get getCode() {
    return this._code;
  }

  get getName() {
    return this._name;
  }
  
  set changeCode(newCode) {
    if (typeof newCode !== 'string') {
      throw new TypeError('Code must be a string');
    }
    this._code = newCode;
  }

  set changeName(newName) {
    if (typeof newName !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = newName;
  }
}    
  function displayFullCurrency() {
}
