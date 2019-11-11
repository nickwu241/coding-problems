const whereCanIPark = (spots, vehicle) => {
  // Code here!
  const parkingMap = {
    'regular': ['R'],
    'small': ['R', 'S'],
    'motorcycle': ['R', 'S', 'M']
  };
  for (let row = 0; row < spots.length; row++) {
    for (let col = 0; col < spots[row].length; col++) {
      if (parkingMap[vehicle].includes(spots[row][col])) {
        return [col, row];
      }
    }
  }
  return false;
}
