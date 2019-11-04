const registerToVote = (name, unregisteredVoters) => {
  // Code here!

  // Remember to return a value!
  return unregisteredVoters.filter(voterName => voterName !== name);
}

