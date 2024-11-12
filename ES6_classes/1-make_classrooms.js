import ClassRoom from './0-classroom';
/* eslint-disable no-underscore-dangle */
export default function initializeRooms() {
  const firstClass = new ClassRoom(19);
  const secondClass = new ClassRoom(20);
  const thirdClass = new ClassRoom(34);

  return [firstClass, secondClass, thirdClass];
}
