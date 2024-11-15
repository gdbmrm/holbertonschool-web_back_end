/* eslint-disable no-underscore-dangle */

export default class Car {
  constructor(brand, moto, color) {
    this._brand = brand;
    this._moto = moto;
    this._color = color;
  }

  cloneCar() {
    return new Car(this._brand, this._moto, this._color);
  }
}
