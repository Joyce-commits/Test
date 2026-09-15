import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# ── DATA ─────────────────────────────────────────────────────
days      = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
instagram = [12400, 15300, 13800, 16200, 18900, 24100, 21500]
youtube   = [8900,  9200,  11400, 10800, 13200, 17600, 16100]
twitter   = [6700,  7800,  6900,  8400,  9100,  7200,  6500]
tiktok    = [19200, 21400, 18700, 22800, 27300, 31500, 28900]

platforms = {
    "Instagram": (instagram, "#E1306C"),
    "YouTube":   (youtube,   "#FF0000"),
    "Twitter":   (twitter,   "#1DA1F2"),
    "TikTok":    (tiktok,    "#000000"),
}


fig, axes = plt.subplots(2, 2, figsize=(14, 9))
fig.suptitle("Social Media Weekly Trends Dashboard", fontsize=16, fontweight="bold", y=0.98)
fig.patch.set_facecolor("#ffffff")

ax1 = axes[0, 0]
for name, (data, color) in platforms.items():
    ax1.plot(days, data, linewidth=3, marker='o', color=color, label = name)
    
ax1.set_title("Daily Post Trends (All Platforms)", fontweight="bold")
ax1.set_ylabel("Posts")
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x/1000)}K"))
ax1.legend(loc="upper left", fontsize=8, )
ax1.grid(axis="y", alpha=0.3)
ax1.set_facecolor("#fdf8f0")

# ── PANEL 2 — BAR CHART: Total weekly posts ──────────────────

totals = {}
for name, (data, _) in platforms.items():
    total = sum(data)
    totals[name] = total
    
    
ax2 = axes[0, 1]
names  = list(totals.keys())
values = list(totals.values())
colors = [platforms[n][1] for n in names]
bars   = ax2.bar(names, values, color=colors, edgecolor="white", linewidth=1.5)
ax2.set_title("Total Weekly Posts per Platform", fontweight="bold")
ax2.set_ylabel("Total Posts")
ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x/1000)}K"))
for bar, val in zip(bars, values):
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 500,
             f"{val:,}", ha="center", va="bottom", fontsize=9, fontweight="bold")
ax2.set_facecolor("#ffffff")
ax2.grid(axis="y", alpha=0.3)

# ── PANEL 3 — LINE CHART: Weekend vs Weekday ─────────────────
ax3 = axes[1, 0]
weekday_avg = {}
weekend_avg = {}
for name, (data, color) in platforms.items():
    weekday_avg[name] = sum(data[:5]) / 5   # Mon–Fri
    weekend_avg[name] = sum(data[5:]) / 2   # Sat–Sun

x = range(len(names))
width  = 0.35
bars1  = ax3.bar([i - width/2 for i in x], [weekday_avg[n] for n in names],
                 width, label="Weekday Avg", color=[platforms[n][1] for n in names], alpha=0.6)
bars2  = ax3.bar([i + width/2 for i in x], [weekend_avg[n] for n in names],
                 width, label="Weekend Avg", color=[platforms[n][1] for n in names], alpha=1.0)
ax3.set_title("Weekday vs Weekend Average", fontweight="bold")
ax3.set_xticks(list(x))
ax3.set_xticklabels(names)
ax3.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x/1000)}K"))
ax3.legend()
ax3.set_facecolor("#ffffff")
ax3.grid(axis="y", alpha=0.3)

# ── PANEL 4 — AREA CHART: TikTok vs Instagram ────────────────
ax4 = axes[1, 1]
ax4.fill_between(days, tiktok, alpha=0.4, color="#000000", label="TikTok")
ax4.fill_between(days, instagram, alpha=0.4, color="#E1306C", label="Instagram")
ax4.plot(days, tiktok, color="#000000", linewidth=2)
ax4.plot(days, instagram, color="#E1306C", linewidth=2)
ax4.set_title("TikTok vs Instagram — Head to Head", fontweight="bold")
ax4.set_ylabel("Posts")
ax4.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x/1000)}K"))
ax4.legend()
ax4.set_facecolor("#ffffff")
ax4.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("social_media_dashboard.png", dpi=150, bbox_inches="tight")
print("\n✅ Dashboard saved as: social_media_dashboard.png")
plt.show()

