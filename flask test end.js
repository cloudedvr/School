function countZeroes(arr) {
  // If the array is empty, return 0.
  if (arr.length === 0) return 0;
  
  let left = 0;
  let right = arr.length - 1;
  let firstZeroIndex = -1;
  
  // Binary search to find the first occurrence of 0.
  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    
    if (arr[mid] === 0) {
      // Record the index and keep searching to the left.
      firstZeroIndex = mid;
      right = mid - 1;
    } else {
      // If the mid element is 1, move to the right.
      left = mid + 1;
    }
  }
  
  // If no 0 was found, return 0.
  if (firstZeroIndex === -1) return 0;
  
  // The count of zeros is the total length minus the first index of 0.
  return arr.length - firstZeroIndex;
}

module.exports = countZeroes;
