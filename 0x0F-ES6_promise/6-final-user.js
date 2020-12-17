import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((values) => {
      for (const i of values) {
        if (i.status === 'rejected') {
          i.value = `Error: ${i.reason.message}`;
          delete i.reason;
        }
      }
      return values;
    });
}
