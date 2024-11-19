export default function getStudentIdsSum(myArray) {
  return myArray.reduce((accumulator, currentValue) => accumulator + currentValue.id,
    0);
}
