# A3 — Analysis and Visualisation Design (5 marks)

- PM2.5 trend across a month: **line chart**; time ordering and trend are clear.
- Station comparison: **bar chart** of station means; categories are directly comparable.
- Temperature vs PM2.5: **scatter plot**; reveals association, clusters and outliers.
- Hours with worst air: **bar chart** of hourly average or **box plot** by hour; compare hour categories or distributions.

## Summary table
Group by station and date. Produce minimum, maximum, mean and valid-reading count using SQL `MIN`, `MAX`, `AVG`, `COUNT`. Exclude invalid/missing readings from aggregates; show count so low-coverage days are apparent.

## Alternative: Python loops
A single scan over n readings is O(n) time and can use O(s*d) memory for grouped accumulators (stations × days). SQL `GROUP BY` also processes the records, but the database engine can optimise, aggregate, and avoid transferring all rows into Python.
