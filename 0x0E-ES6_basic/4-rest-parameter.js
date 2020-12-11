export default function returnHowManyArguments(...args) {
  let argsCount = 0;
  /* eslint-disable no-unused-vars */
  for (const arg of args) argsCount += 1;
  /* eslint-disable no-unused-vars */
  return argsCount;
}
