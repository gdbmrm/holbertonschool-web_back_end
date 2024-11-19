export default function cleanSet(set, startString) {
  let myString = '';
  let first = true;
  if (startString.length === 0) {
    return myString;
  }

  for (const element of set) {
    if (element.includes(startString)) {
      if (!first) {
        myString += '-';
      }
      first = false;
      myString += String(element.replace(startString, ''));
    }
  }
  return myString;
}
