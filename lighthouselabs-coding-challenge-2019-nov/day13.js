const lightsOn = function(lights) {
  // Code here!
  for (let i = 0; i < lights.length; i++) {
    lights[i]['on'] = true;
  }
  return lights;
}

const lightsOff = function(lights) {
  // Code here!
  for (let i = 0; i < lights.length; i++) {
    lights[i]['on'] = false;
  }
  return lights;
}

const toggleLights = function(lights, lightsAreOn) {
  // Code here!
  return lightsAreOn ? lightsOff(lights) : lightsOn(lights);
}

