const festivalColours = color1 => {
  // code here!
  // formula: H1 = |(H0 + 150 degrees) - 360 degrees|
  // formula: H2 = |(H0 + 210 degrees) - 360 degrees|
  let h1 = color1 + 150;
  let h2 = color1 + 210;
  if (h1 >= 360) {
    h1 -= 360;
  }
  if (h2 >= 360) {
    h2 -= 360;
  }
  let splitColours = [h1, h2];
  splitColours.sort();
  return splitColours;
}

