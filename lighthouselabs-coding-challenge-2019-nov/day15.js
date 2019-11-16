const finalPosition = (moves) => {
  // Code here!
  let x = 0;
  let y = 0;
  moves.forEach(move => {
    switch(move) {
      case 'north':
        y += 1;
        break;
      case 'south':
        y -= 1;
        break;
      case 'west':
        x -= 1;
        break;
      case 'east':
        x += 1;
        break;
    }
  });
  return [x, y];
}

