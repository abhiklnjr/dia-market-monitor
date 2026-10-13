# DIA Market Data Monitor

A small prototype built for the **Citi ICG Technology Software Development Job Simulation** on Forage.
It collects near real-time prices for `DIA` (an ETF that closely tracks the Dow Jones Industrial Average)
and charts how the price changes over a single run.

> This is a learning project built around hypothetical tasks. It is not affiliated with or endorsed by Citi.

## What it does

1. **`App.java`** polls the [Twelve Data](https://twelvedata.com/) `/price` endpoint for `DIA` every 15 seconds,
   captures the current timestamp, and stores each result in a queue.
2. **`plot_prices.py`** takes the Java program's console output, parses the price and timestamp values with
   pandas, and draws a price-over-time line chart with matplotlib.

## Example output

```
Added data point: price=506.049988, timestamp=2026-05-26T10:28:36.547871559Z
Current queue size: 1
```

![DIA price over time](images/dia_price_chart.png)

## Tech

- Java 11 (`java.net.http.HttpClient`, `ScheduledExecutorService`, `ConcurrentLinkedQueue`)
- Python 3 (pandas, matplotlib)
- Developed and run in Google Colab

## Run it

You need a free Twelve Data API key. **Never commit your key.** Provide it as an environment variable.

```bash
export TWELVE_DATA_API_KEY="your_key_here"
javac App.java
java App
```

In Google Colab, set the key with `getpass` so it never appears in the notebook:

```python
from getpass import getpass
import os
os.environ["TWELVE_DATA_API_KEY"] = getpass("Enter your Twelve Data API key: ")
```

Then copy the `Added data point: ...` lines from the Java output into `java_output` in `plot_prices.py` and run it.

## Design notes and limitations

- The app stops after a fixed number of polls so it finishes on its own (needed for the Colab runner).
- Failed requests are logged and skipped, so one bad poll does not stop the run.
- The `/price` endpoint returns the last available price, so the line can be flat when the market is closed.
- This is a single-run chart, not a live dashboard.

## Possible next steps

- Update the chart continuously instead of from a single run
- Persist data points to a database or file instead of an in-memory queue
- Support multiple symbols and longer time ranges (hourly, daily, monthly)
- Retry with backoff and respect API rate limits
