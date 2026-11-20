# A2 — Cleaning and Normalisation Design (5 marks)

## Cleaning rules
- Missing sensor readings: preserve as missing; for trend summaries, fill a short gap with previous value only if the time sequence supports it, otherwise use station median and flag imputed data.
- Negative pollutant values: reject and record in a rejected-row log.
- Impossible readings: reject or flag values outside the documented sensor range; avoid arbitrary thresholds.
- Duplicate station/date/hour rows: retain one valid row or resolve by timestamp/quality flag.
- Fahrenheit: convert to Celsius using `(F - 32) * 5 / 9`.
- Station names: trim whitespace and standardise casing. Dates use ISO `YYYY-MM-DD`; readings use numeric values with consistent precision.

## Normalisation
Min-max: `x_scaled=(x-min)/(max-min)`; bounded to [0,1], useful when a fixed range is required but sensitive to outliers.
Z-score: `z=(x-mean)/standard_deviation`; useful for comparing deviations from the mean and has no fixed bounds.

## Alternative: dropping missing values
Dropping rows is O(n) and uses O(1) extra space in a streaming implementation, but loses valid measurements from rows with any missing field. Median calculation generally requires sorting O(n log n) and O(n) memory (or a selection algorithm).
