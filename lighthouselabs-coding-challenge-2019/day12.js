function powerOn() {
  ship.powerOn = true;
}

function countModules() {
  return availableModules.length;
}

function countEssential() {
  return availableModules.filter((module) => module.essential).length;
}

function loadModule(index) {
  if (index < 0 || index >= availableModules.length) {
    return;
  }
  availableModules[index].enabled = true;
  ship.modules.push(availableModules[index]);
}

function findModuleIndex(moduleName) {
  return availableModules.findIndex(
    (module) => module.essential && module.name === moduleName);
}

function resetLARRY() {
  for (var i = 0; i < 10; i++) {
    LARRY.quack();
  }
}

function setMessage() {
  radio.message = JSON.stringify(navigation);
}

function activateBeacon() {
  radio.beacon = true;
}

function setFrequency() {
  radio.frequency = (radio.range.low + radio.range.high) / 2;
}

function initialize() {
  navigation.x = 0;
  navigation.y = 0;
  navigation.z = 0;  
}

loadModule(findModuleIndex('life-support'));
loadModule(findModuleIndex('propulsion'));
loadModule(findModuleIndex('navigation'));
loadModule(findModuleIndex('communication'));
resetLARRY();
setMessage();
activateBeacon();
