const dynamicPricing = (numberOfPeople, distanceTraveled) => {
  // Code here!
  let total = 1.00 + distanceTraveled * 0.25;
  if (numberOfPeople >= 30) {
    total += 0.25;
  }
  return '$' + total.toFixed(2);
}

