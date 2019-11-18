const judgeVegetable = (vegetables, metric) => {
  // Code here!
  let bestScore = Number.NEGATIVE_INFINITY;
  let bestSubmitter = null;
  
  vegetables.forEach(vegetable => {
    let score = vegetable[metric];
    if (score > bestScore) {
      bestScore = score;
      bestSubmitter = vegetable['submitter'];
    }
  });
  
  return bestSubmitter;
}

