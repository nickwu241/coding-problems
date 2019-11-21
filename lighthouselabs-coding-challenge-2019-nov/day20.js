// Use the value below whenever you need the value of Pi

const PI = 3.14159 

const sphereVolume = function (radius) {
  return PI * 4 / 3 * radius * radius * radius;
}

const coneVolume = function (radius, height) {
  return PI / 3 * height * radius * radius;
}

const prismVolume = function (height, width, depth) {
  return height * width * depth;
}

const totalVolume = function (solids) {
  let totalVolume = 0;
  solids.forEach(solid => {
    switch(solid['type']) {
      case 'sphere':
        totalVolume += sphereVolume(solid['radius']);
        break;
      case 'cone':
        totalVolume += coneVolume(solid['radius'], solid['height']);
        break;
      case 'prism':
        totalVolume += prismVolume(solid['height'], solid['width'], solid['depth']);
        break;
    }
  });
  return totalVolume;
}

