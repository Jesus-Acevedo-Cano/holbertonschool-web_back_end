export default function cleanSet(_set, startString) {
  if (startString === '') return '';

  const stringSet = [];
  [..._set].forEach((x) => {
    if (x.indexOf(startString) === 0) stringSet.push(x.replace(startString, ''));
  });
  return stringSet.join('-');
}
