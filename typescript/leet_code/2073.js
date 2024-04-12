function timeRequiredToBuy(tickets, k) {
    var seconds = 0;
    var ticketNeedToBuy = tickets[k];
    var gap = tickets.filter(function (item, index) { return index < k && item < tickets[k]; }).length;
    while (ticketNeedToBuy > 1) {
        seconds += tickets.length;
        tickets = tickets.reduce(function (newArr, currentValue, currentIndex) {
            if (--currentValue !== 0) {
                newArr.push(currentValue);
            }
            return newArr;
        }, []);
        ticketNeedToBuy--;
    }
    return seconds + k - gap + 1;
}
