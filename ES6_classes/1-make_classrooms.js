import ClassRoom from "./0-classroom";

export default function initializeRooms() {
    let firstClass = new ClassRoom(19);
    let secondClass = new ClassRoom(20);
    let thirdClass = new ClassRoom(34);

    return [firstClass, secondClass, thirdClass];
}