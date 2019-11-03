// Remember, the possible candidates are: Tim, Sally, and Beth (in that order)
const castVote = (name, votes) => {
  // Code here!

  // Remember to return a value!
  switch (name) {
    case 'Tim':
      votes[0]++;
      break;
    case 'Sally':
      votes[1]++;
      break;
    case 'Beth':
      votes[2]++;
      break;
  }
  return votes;
}

