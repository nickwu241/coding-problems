const carPassing = (cars, speed) => {
  // Code here!
  cars.push({
    time: Date.now(),
    speed: speed
  });
  return cars;
}

