export default function getFullResponseFromAPI(success) {
  if (success === true) {
    /* return Promise.resolve('Success'), 200; */
    return Promise.resolve({ status: 200, body: 'Success' });
  }
  return Promise.reject(Error('The fake API is not working currently'));
}
