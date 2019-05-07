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

loadModule(findModuleIndex('life-support'));
loadModule(findModuleIndex('propulsion'));
loadModule(findModuleIndex('navigation'));
resetLARRY();
