
# Debit Scheduler Take-home

Welcome! If you're reading this, odds are that you're interviewing for a backend engineering role at EarnUp. We are excited to continue the conversation! Your mission, should you choose to accept, is to build a debit scheduling endpoint for loans.

There is a lot of flexibility to this exercise... and it’s intentional. We always appreciate clean, well-documented code, but we’re also looking to see how you approach problems and make tradeoffs. We’re just as interested to discuss your design as we are to see a working app. The boilerplate code in this project should serve as a foundation; feel free to make modifications, write helper functions, extend tests, etc.

This project is designed to take **45 minutes**, no more than 1 hour, but we respect your right to work on it as needed on your own time. Clone this repo to get started. Please send the recruiter a link to your solution within a week.


## Deliverable

Build an endpoint called `/get_next_debit` that accepts information about a loan and returns the *next* debit amount and debit date for that loan.

There are 3 primitives to understand:
- **Loan** - this could be a mortgage, auto loan or some other financial product that requires a regularly scheduled payment.
- **Payment** - a date and amount that gets paid towards a loan on the `payment_due_day` of the month.
- **Debit** - a date and amount to retrieve funds from a customer. Multiple debits add up to a monthly payment.

For example, a loan with a $750 monthly payment that debits a customer bi-weekly (every other Friday) starting on May 7th, 2021 would have the following debit schedule for the month of May:
- Debit $375 on May 7th, 2021
- Debit $375 on May 21st, 2021

Keep in mind, some months have more debit dates than other months. The sum of debit amounts for a given month should equal the `monthly_payment_amount`. A debit cannot be used for a payment on the same day, it would need to be used for the next payment. Debits and payments can only occur on business days (Monday - Friday).

Explore `/tests` for more examples.

### Example Request
```json
{
    "loan": {
        "monthly_payment_amount": 750,
        "payment_due_day": 28,
        "schedule_type": "biweekly",
        "debit_start_date": "2021-05-07",
        "debit_day_of_week": "friday"
    }
}
```

### Example Response
```json
{
    "debit": {
        "amount": 375,
        "date": "2021-05-21"
    }
}
```

### Getting Started

Run the API app
```bash
docker-compose build
docker-compose run app
```

The API will be exposed on `0.0.0.0:5000`

Run tests
```bash
docker-compose run app python -m pytest
```

#### bonus
Ensure that the debit schedule respects Federal Reserve [bank holidays](https://www.federalreserve.gov/aboutthefed/k8.htm).
