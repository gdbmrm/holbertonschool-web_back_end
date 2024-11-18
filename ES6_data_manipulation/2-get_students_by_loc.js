export default function getStudentsByLocation(myArray, city) {
    return myArray.filter(({ city }) === city )
}