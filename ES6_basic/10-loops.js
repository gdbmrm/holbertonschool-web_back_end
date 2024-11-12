export default function appendToEachArrayValue(array, appendString) {
  const myArray = [...array];

  for (const value of array) {
    myArray[array.indexOf(value)] = appendString + value;
  }

  return myArray;
}
