const pumpkinSpice = money => {
  const nPumpkinPies = Math.floor(money / 5);
  const nPumpkinSpiceLattes = Math.floor((money % 5) / 3);
  const nPumpkinSpiceMacarons =(money % 5) % 3;
  
  const nGramsPumpkinSpice = 
    nPumpkinPies * 30 +
    nPumpkinSpiceLattes * 15 +
    nPumpkinSpiceMacarons * 3;

  return [
    nPumpkinPies,
    nPumpkinSpiceLattes,
    nPumpkinSpiceMacarons,
    nGramsPumpkinSpice
  ];
}

