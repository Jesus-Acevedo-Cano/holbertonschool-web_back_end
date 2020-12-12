export default function appendToEachArrayValue(array, appendString) {
  const aux = array;
  for (const idx of array) {
    const value = array.indexOf(idx);
    aux[value] = `${appendString}${idx}`;
  }

  return aux;
}
