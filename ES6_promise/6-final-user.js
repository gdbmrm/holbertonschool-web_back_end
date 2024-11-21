import { signUpUser } from './4-user-promise'
import { uploadPhoto } from './5-photo-reject'

export default function handleProfileSignup(firstName, lastName, fileName) {
  const photo = uploadPhoto();
  const user = signUpUser();

  return Promise.allSettled([photo, user])
    .then((results) => )
}
