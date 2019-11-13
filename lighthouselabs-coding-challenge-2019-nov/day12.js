const checkAir = function (samples, threshold) {
  // Code here!
  const dirtySamples = samples.filter(sample => sample === 'dirty');
  const dirtyRatio = dirtySamples.length / samples.length;
  return dirtyRatio < threshold ? 'Clean' : 'Polluted';
}

