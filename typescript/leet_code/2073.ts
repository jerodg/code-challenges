function timeRequiredToBuy(tickets: number[], k: number): number {
    let seconds: number = 0;
    let ticketNeedToBuy = tickets[k];
    let gap = tickets.filter((item, index) => index < k && item < tickets[k]).length;

    while (ticketNeedToBuy > 1) {
        seconds += tickets.length;

        tickets = tickets.reduce((newArr: number[], currentValue, currentIndex) => {
            if (--currentValue !== 0) {
                newArr.push(currentValue);
            }
            return newArr;
        }, []);

        ticketNeedToBuy--;
    }
    return seconds + k - gap + 1;
}
