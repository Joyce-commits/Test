import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

print("=" * 58)
print("        GLOBAL CLIMATE DATA STORY")
print("=" * 58)

# ── STEP 1 — GENERATE REALISTIC DATASET ──────────────────────
# 50 years (1974–2023) of annual avg temperature for 5 cities
np.random.seed(42)
years = list(range(1974, 2024))  # 50 years

# Realistic warming trend: base temp + slight upward drift + noise
def gen_temps(base, trend=0.025, noise=0.4):
    return [round(base + trend * i + np.random.normal(0, noise), 2) for i in range(50)]

raw_data = {
    "Year":       years,
    "Delhi":      gen_temps(25.2, trend=0.035),
    "London":     gen_temps(11.3, trend=0.020),
    "New_York":   gen_temps(13.1, trend=0.022),
    "Sydney":     gen_temps(17.8, trend=0.018),
    "Moscow":     gen_temps(5.4,  trend=0.030),
}

df = pd.DataFrame(raw_data)

# ── INJECT MISSING VALUES (realistic dirty data) ──────────────
missing_indices = np.random.choice(df.index, size=8, replace=False)
cities = ["Delhi", "London", "New_York", "Sydney", "Moscow"]
for idx in missing_indices:
    city = np.random.choice(cities)
    df.loc[idx, city] = np.nan

print(f"\n📂 STEP 1: Dataset created — {len(df)} years × {len(cities)} cities")
print(f"   Missing values found: {df[cities].isnull().sum().sum()}")
print(f"\n   Sample (first 5 rows):")
print(df.head().to_string(index=False))

# ── STEP 2 — CLEAN THE DATA ───────────────────────────────────
print("\n🧹 STEP 2: Cleaning missing values...")
before_nulls = df[cities].isnull().sum().sum()

# Fill each city's missing values with its own column mean
for city in cities:
    city_mean = df[city].mean()
    null_count = df[city].isnull().sum()
    df[city].fillna(round(city_mean, 2), inplace=True)
    if null_count > 0:
        print(f"   {city:<12}: filled {null_count} missing value(s) with mean={city_mean:.2f}°C")

after_nulls = df[cities].isnull().sum().sum()
print(f"   Before: {before_nulls} nulls → After: {after_nulls} nulls ✅")

# ── STEP 3 — ANALYSE WITH NUMPY ──────────────────────────────
print("\n📊 STEP 3: City-by-City Analysis")
print("-" * 55)
print(f"  {'City':<12} {'1974':>7} {'2023':>7} {'Δ Temp':>7} {'Min':>6} {'Max':>6} {'Avg':>7}")
print("-" * 55)

for city in cities:
    temps     = df[city].values                    # NumPy array
    temp_1974 = temps[0]
    temp_2023 = temps[-1]
    delta     = temp_2023 - temp_1974
    trend_dir = "↑" if delta > 0 else "↓"
    print(f"  {city:<12} {temp_1974:>7.2f} {temp_2023:>7.2f} {trend_dir}{abs(delta):>6.2f}° "
          f"{np.min(temps):>6.2f} {np.max(temps):>6.2f} {np.mean(temps):>7.2f}")

# Hottest year (global average)
df["Global_Avg"] = df[cities].mean(axis=1)
hottest_year = df.loc[df["Global_Avg"].idxmax(), "Year"]
coldest_year = df.loc[df["Global_Avg"].idxmin(), "Year"]
print(f"\n  🌡️  Hottest year (global avg): {hottest_year} ({df['Global_Avg'].max():.2f}°C)")
print(f"  🌡️  Coldest year (global avg): {coldest_year} ({df['Global_Avg'].min():.2f}°C)")

# Decade averages
print("\n📅 DECADE AVERAGES (Global)")
for decade_start in range(1974, 2024, 10):
    decade_end  = min(decade_start + 9, 2023)
    decade_data = df[(df["Year"] >= decade_start) & (df["Year"] <= decade_end)]["Global_Avg"]
    print(f"   {decade_start}–{decade_end}: {decade_data.mean():.2f}°C")

# ── STEP 4 — VISUALISE ───────────────────────────────────────
print("\n🎨 STEP 4: Building 3-panel dashboard...")
colors = {"Delhi": "#FF6B35", "London": "#4ECDC4", "New_York": "#45B7D1",
          "Sydney": "#96CEB4", "Moscow": "#FFEAA7"}

fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle("50 Years of Global Temperature Change (1974–2023)",
             fontsize=15, fontweight="bold")
fig.patch.set_facecolor("#f0f4f8")

# Panel 1 — Line chart: All city trends
ax1 = axes[0]
for city in cities:
    ax1.plot(df["Year"], df[city], linewidth=1.8,
             color=colors[city], label=city, alpha=0.85)
ax1.plot(df["Year"], df["Global_Avg"], linewidth=2.5,
         color="black", linestyle="--", label="Global Avg")
ax1.set_title("Temperature Trends (All Cities)", fontweight="bold")
ax1.set_xlabel("Year")
ax1.set_ylabel("Avg Temp (°C)")
ax1.legend(fontsize=8)
ax1.grid(alpha=0.3)
ax1.set_facecolor("white")

# Panel 2 — Bar chart: Warming delta per city
ax2 = axes[1]
deltas = [df[c].values[-1] - df[c].values[0] for c in cities]
bar_colors = ["#e74c3c" if d > 0 else "#3498db" for d in deltas]
bars = ax2.bar(cities, deltas, color=bar_colors, edgecolor="white")
ax2.axhline(0, color="black", linewidth=0.8)
ax2.set_title("Warming Since 1974 (°C)", fontweight="bold")
ax2.set_ylabel("Temperature Change (°C)")
for bar, d in zip(bars, deltas):
    ax2.text(bar.get_x() + bar.get_width()/2,
             bar.get_height() + 0.02 if d > 0 else bar.get_height() - 0.08,
             f"+{d:.2f}°" if d > 0 else f"{d:.2f}°",
             ha="center", fontsize=9, fontweight="bold")
ax2.set_facecolor("white")

# Panel 3 — Global average with trend line
ax3 = axes[2]
ax3.fill_between(df["Year"], df["Global_Avg"], alpha=0.25, color="#e74c3c")
ax3.plot(df["Year"], df["Global_Avg"], color="#e74c3c", linewidth=2, label="Global Avg")
# Trend line using NumPy polyfit
z   = np.polyfit(df["Year"], df["Global_Avg"], 1)
p   = np.poly1d(z)
ax3.plot(df["Year"], p(df["Year"]), "k--", linewidth=1.5, label=f"Trend (+{z[0]*10:.2f}°/decade)")
ax3.set_title("Global Average + Trend", fontweight="bold")
ax3.set_xlabel("Year")
ax3.set_ylabel("Avg Temp (°C)")
ax3.legend(fontsize=9)
ax3.grid(alpha=0.3)
ax3.set_facecolor("white")

plt.tight_layout()
plt.savefig("climate_dashboard.png", dpi=150, bbox_inches="tight")
print("   ✅ Saved: climate_dashboard.png")
plt.show()

# ── STEP 5 — INSIGHTS ────────────────────────────────────────
print("\n" + "=" * 58)
print("📌 DATA INSIGHTS")
print("=" * 58)
fastest_warming = cities[np.argmax(deltas)]
slowest_warming = cities[np.argmin(deltas)]
trend_per_decade = z[0] * 10
print(f"  • Fastest warming city : {fastest_warming} (+{max(deltas):.2f}°C since 1974)")
print(f"  • Slowest warming city : {slowest_warming} (+{min(deltas):.2f}°C since 1974)")
print(f"  • Global trend         : +{trend_per_decade:.2f}°C per decade")
print(f"  • Hottest year on record: {hottest_year}")
print(f"  • This is why AI weather models need historical data like this!")
print("=" * 58)

print("\n💡 CHALLENGE:")
print("  1. Which decade saw the steepest temperature rise?")
print("  2. Add a 6th city of your choice with realistic temperatures.")
print("  3. Find the year where Delhi first crossed 27°C average.")
print()