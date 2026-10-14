import re
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Paste your Java output between the triple quotes below
java_output = """
Added data point: price=517.84998, timestamp=2026-10-13T03:31:03.899452253Z
Current queue size: 1
Added data point: price=517.84998, timestamp=2026-10-13T03:31:18.213997295Z
Current queue size: 2
Added data point: price=517.84998, timestamp=2026-10-13T03:31:33.210453514Z
Current queue size: 3
Added data point: price=517.84998, timestamp=2026-10-13T03:31:48.241710362Z
Current queue size: 4
Added data point: price=517.84998, timestamp=2026-10-13T03:32:03.214810591Z
Current queue size: 5
Added data point: price=517.84998, timestamp=2026-10-13T03:32:18.210973610Z
Current queue size: 6
Added data point: price=517.84998, timestamp=2026-10-13T03:32:33.234883125Z
Current queue size: 7
"""

# Extract price and timestamp from every "Added data point" line
matches = re.findall(
    r"price=([0-9.]+), timestamp=(\S+)",
    java_output
)

if not matches:
    raise ValueError("No data points found. Check that you pasted the 'Added data point' lines.")

# Convert to DataFrame
df = pd.DataFrame(matches, columns=["price", "timestamp"])

# Convert data types
df["price"] = df["price"].astype(float)
df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)

print(df)

# Plot the data
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df["timestamp"], df["price"], marker="o", linewidth=2)

ax.set_title("DIA Price Over Time")
ax.set_xlabel("Timestamp (UTC)")
ax.set_ylabel("Price (USD)")

# Readable time labels and plain (non-offset) price labels
ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))
ax.ticklabel_format(axis="y", useOffset=False, style="plain")
ax.grid(True, alpha=0.3)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
