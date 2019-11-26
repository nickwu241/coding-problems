const chooseRecipe = function(bakeryA, bakeryB, recipes) {
  // Code here!
  return recipes.find(r => {
    return bakeryA.some(ingredient => r['ingredients'].includes(ingredient)) &&
      bakeryB.some(ingredient => r['ingredients'].includes(ingredient))
  })['name'];
}

