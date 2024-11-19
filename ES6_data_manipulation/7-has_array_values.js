export default function hasValuesFromArray(set, array) {
  let TrueOrFalse = 'false';
  for (const element of array) {
    if (set.has(element)) {
      TrueOrFalse = 'true';
    } else {
      TrueOrFalse = 'false';
    }
  }
  return TrueOrFalse;
}
