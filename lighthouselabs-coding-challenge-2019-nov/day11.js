const busTimes = buses => {
  // Code here!
  let result = {};
  for (let [busName, busInfo] of Object.entries(buses)) {
    result[busName] = busInfo['distance'] / busInfo['speed'];
  }
  return result;
}

