const termTopics = (interviews) => {
  // Code here!

  // Remember to return an array!
  let termsCounter = [0, 0 ,0];
  let terms = ['smart city', 'arts funding', 'transportation'];
  
  interviews.forEach(interview => {
    for (const [i, term] of terms.entries()) {
      if (interview.includes(term)) {
        termsCounter[i]++;
      }
    }
  });
  return termsCounter;
}

