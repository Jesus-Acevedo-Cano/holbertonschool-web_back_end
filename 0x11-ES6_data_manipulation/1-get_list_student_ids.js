export default function getListStudentIds(array) {
  if (Array.isArray(array)) return array.map((i) => i.id);
  return [];
}
