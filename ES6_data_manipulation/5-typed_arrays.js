export default function createInt8TypedArray(length, position, value) {
  if (position >= length || position < 0) {
    throw new Error('Position outside range');
  }

  if (typeof position !== 'number') {
    throw new Error('Position must be a number');
  }

  if (typeof value !== 'number') {
    throw new Error('Value must be a number');
  }

  if (typeof length !== 'number') {
    throw new Error('Length must be a number');
  }

  const buffer = new ArrayBuffer(length);
  const int8Array = new Int8Array(buffer);

  int8Array[position] = value;

  return buffer;
}
