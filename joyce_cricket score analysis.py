import numpy as np

print("=" * 55)
print("       INDIA vs AUSTRALIA — ODI SERIES ANALYSER")
print("=" * 55)


# 10 ODI match scores (runs scored per match)
india_scores    = np.array([287, 312, 198, 345, 267, 389, 223, 301, 278, 334])
australia_scores = np.array([265, 334, 201, 298, 289, 367, 245, 278, 301, 312])

#-----------------------------------------------------------------------------------


# Winner based on the scores
match_labels    = [f"Match {i}" for i in range(1, 11)]

# match_labels  = ['Match 1', 'Match 2', 'Match 3', 'Match 4', 'Match 5', 'Match 6', 'Match 7', 'Match 8', 'Match 9', 'Match 10']

print("\n📋 RAW SCORECARD")
print(f"{'Match':<10} {'India':>8} {'Australia':>12} {'Winner':>10}")  #spaces between the words
print("-" * 42)

for i in range(len(india_scores)):
    winner = "🇮🇳 India" if india_scores[i] > australia_scores[i] else "🇦🇺 Australia"
    print(f"{match_labels[i]:<10} {india_scores[i]:>8} {australia_scores[i]:>12} {winner:>10}")
    

print("*" * 100)
#----------------------------------------------------------------------------------------

# India Performace Statistics

print("\n📊 INDIA — PERFORMANCE STATS")
print("-" * 35)
print(f"  Average Score    : {np.mean(india_scores):.1f}")  # 1 decimal point of float
print(f"  Highest Score    : {np.max(india_scores)}  (Match {np.argmax(india_scores)+1})")
print(f"  Lowest Score     : {np.min(india_scores)}  (Match {np.argmin(india_scores)+1})")
print(f"  Std Deviation    : {np.std(india_scores):.1f}  (consistency measure)")
print(f"  Total Runs       : {np.sum(india_scores)}")

print("*" * 100)
#----------------------------------------------------------------------------------------

# Top 3 scores using sort + reverse slice
india_top3_scores = np.sort(india_scores)[::-1][:3]
india_top3_idx    = np.argsort(india_scores)[::-1][:3]
print(f"\n  🏆 Top 3 Scores  : {india_top3_scores}")
print(f"  🏆 In Matches    : {[f'Match {i+1}' for i in india_top3_idx]}")

print("*" * 100)
#----------------------------------------------------------------------------------------

# Australia Performace Statistics
print("\n📊 AUSTRALIA — PERFORMANCE STATS")
print("-" * 35)
print(f"  Average Score    : {np.mean(australia_scores):.1f}")
print(f"  Highest Score    : {np.max(australia_scores)}  (Match {np.argmax(australia_scores)+1})")
print(f"  Lowest Score     : {np.min(australia_scores)}  (Match {np.argmin(australia_scores)+1})")
print(f"  Std Deviation    : {np.std(australia_scores):.1f}")
print(f"  Total Runs       : {np.sum(australia_scores)}")

aus_top3_scores = np.sort(australia_scores)[::-1][:3]
aus_top3_idx    = np.argsort(australia_scores)[::-1][:3]
print(f"\n  🏆 Top 3 Scores  : {aus_top3_scores}")
print(f"  🏆 In Matches    : {[f'Match {i+1}' for i in aus_top3_idx]}")

print("*" * 100)
#----------------------------------------------------------------------------------------

# Head to Head result
print("\n🏏 HEAD-TO-HEAD RESULT")
print("-" * 35)
diff          = india_scores - australia_scores        # positive = India won
india_wins    = np.sum(diff > 0)
aus_wins      = np.sum(diff < 0)
biggest_win   = np.max(np.abs(diff))
biggest_match = np.argmax(np.abs(diff)) + 1

print(f"  India Wins       : {india_wins}")
print(f"  Australia Wins   : {aus_wins}")
print(f"  Closest Match    : Match {np.argmin(np.abs(diff))+1} (gap = {np.min(np.abs(diff))} runs)")
print(f"  Biggest Win      : Match {biggest_match} (gap = {biggest_win} runs)")

print("*" * 100)
#----------------------------------------------------------------------------------------


# ── BOOLEAN FILTER — HIGH SCORING MATCHES ────────────────────
threshold = 300
print(f"\n🔥 HIGH SCORING MATCHES (both teams > {threshold})")
print("-" * 35)
high_scoring = (india_scores > threshold) & (australia_scores > threshold)
for i, flag in enumerate(high_scoring):
    if flag:
        print(f"  Match {i+1}: India {india_scores[i]} vs Australia {australia_scores[i]}")
        
print("*" * 100)
#----------------------------------------------------------------------------------------

# ── SERIES WINNER ─────────────────────────────────────────────
print("\n" + "=" * 55)
if india_wins > aus_wins:
    print(f"  🏆 SERIES WINNER: INDIA ({india_wins}-{aus_wins})")
elif aus_wins > india_wins:
    print(f"  🏆 SERIES WINNER: AUSTRALIA ({aus_wins}-{india_wins})")
else:
    print(f"  🤝 SERIES DRAWN ({india_wins}-{aus_wins})")

print("*" * 100)
#----------------------------------------------------------------------------------------

# ── CHALLENGE SECTION ────────────────────────────────────────
print("\n💡 CHALLENGE: Can you find...")
print("  1. The average winning margin across all India wins?")
print("  2. How many matches had scores within 20 runs of each other?")
print("  3. India's score in the top 50th percentile? (Hint: np.percentile)")
print()

india_wins_mask = diff > 0
avg_margin = np.mean(diff[india_wins_mask])
close_matches = np.sum(np.abs(diff) <= 20)
percentile_50 = np.percentile(india_scores, 50)
print(f"  Avg India win margin: {avg_margin:.1f} runs")
print(f"  Close matches: {close_matches}")
print(f"  India 50th percentile: {percentile_50}")

print("*" * 100)
#----------------------------------------------------------------------------------------
    
    




    
    
    
    
    
    
    
    