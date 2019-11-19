const countTickets = (tickets) => {
  // Code here!
  let counter = {'red': 0, 'green': 0, 'blue': 0};
  tickets.forEach(ticket => counter[ticket]++);
  return counter;
}

const bestOdds = (tickets, raffleEntries) => {
  // Code here!
  let bestOdds = 0.0;
  let bestColour = null;
  const counter = countTickets(tickets);
  
  for (let [ticketColour, nTotalTickets] of Object.entries(raffleEntries)) {
    const odds = counter[ticketColour] / nTotalTickets;
    if (odds > bestOdds) {
      bestOdds = odds;
      bestColour = ticketColour;
    }
  }
  return `You have the best odds of winning the ${bestColour} raffle.`
}

