export default function signUpUser(firstName, lastName) {
  return new Promise(((myResolve) => {
    myResolve({
      firstName,
      lastName,
    });
}));
}
