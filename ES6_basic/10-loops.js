export default function appendToEachArrayValue(array, appendString) {
  const myArray = [...array];
  for (const idx of myArray) {
    myArray[array.indexOf(idx)] = appendString + idx;
  }
  return myArray;
}
