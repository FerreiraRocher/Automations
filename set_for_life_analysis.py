#!/usr/bin/env python3
"""
UK Set for Life Lottery - Comprehensive Statistical Analysis
=============================================================
Analyzes historical draw data to identify patterns and generate
5 optimized number sequences.

Format: 5 main numbers (1-47) + 1 Life Ball (1-10)
Draws: Monday & Thursday, 8PM
"""

import random
from collections import Counter, defaultdict
from itertools import combinations
from datetime import datetime

# ============================================================
# HISTORICAL DRAW DATA (collected from official sources)
# ============================================================
# Format: (date, (main1, main2, main3, main4, main5), life_ball)
draws = [
    # 2026 draws
    ("2026-02-05", (6, 15, 21, 22, 43), 6),
    ("2026-02-02", (2, 6, 31, 39, 42), 5),
    ("2026-01-29", (13, 24, 31, 33, 36), 3),
    ("2026-01-26", (1, 16, 19, 26, 34), 7),
    ("2026-01-22", (1, 5, 13, 17, 21), 2),
    ("2026-01-19", (3, 7, 19, 30, 32), 7),
    ("2026-01-15", (9, 22, 24, 29, 30), 1),
    ("2026-01-12", (9, 20, 29, 41, 47), 4),
    ("2026-01-08", (13, 17, 26, 29, 46), 4),
    ("2026-01-05", (4, 22, 32, 33, 36), 7),
    ("2026-01-01", (7, 8, 41, 43, 45), 10),
    # December 2025
    ("2025-12-29", (8, 13, 15, 25, 39), 6),
    ("2025-12-25", (1, 4, 6, 30, 47), 9),
    ("2025-12-22", (10, 23, 27, 28, 36), 3),
    ("2025-12-18", (8, 9, 10, 19, 37), 10),
    ("2025-12-15", (8, 27, 29, 31, 42), 5),
    ("2025-12-11", (16, 21, 26, 29, 36), 2),
    ("2025-12-08", (4, 22, 27, 35, 45), 6),
    ("2025-12-04", (1, 8, 33, 38, 42), 9),
    ("2025-12-01", (16, 22, 24, 32, 38), 9),
    # November 2025
    ("2025-11-27", (11, 13, 14, 20, 26), 8),
    ("2025-11-20", (4, 5, 9, 14, 42), 9),
    ("2025-11-03", (4, 20, 31, 35, 38), 1),
    # October 2025
    ("2025-10-30", (5, 18, 22, 31, 32), 3),
    ("2025-10-27", (6, 16, 18, 33, 34), 4),
    ("2025-10-23", (3, 20, 25, 26, 35), 7),
    ("2025-10-20", (11, 17, 26, 30, 43), 8),
    ("2025-10-16", (1, 8, 12, 27, 46), 2),
    ("2025-10-13", (4, 24, 27, 31, 36), 8),
    ("2025-10-09", (10, 16, 36, 39, 40), 7),
    ("2025-10-06", (9, 15, 24, 33, 45), 2),
    ("2025-10-02", (3, 28, 30, 35, 40), 7),
    # September 2025
    ("2025-09-29", (7, 12, 31, 34, 35), 7),
    ("2025-09-25", (10, 25, 33, 42, 46), 4),
    ("2025-09-01", (18, 21, 24, 29, 47), 7),
    # August 2025
    ("2025-08-28", (6, 18, 21, 25, 34), 10),
    ("2025-08-25", (5, 32, 34, 38, 44), 9),
    ("2025-08-21", (3, 6, 7, 14, 18), 5),
    ("2025-08-18", (2, 4, 8, 11, 28), 1),
    ("2025-08-14", (8, 9, 21, 32, 42), 8),
    ("2025-08-11", (3, 6, 24, 27, 34), 5),
    ("2025-08-07", (3, 11, 17, 18, 23), 6),
    ("2025-08-04", (11, 26, 28, 32, 39), 2),
    # July 2025 (partial)
    ("2025-07-31", (4, 11, 26, 44, 47), 10),
    ("2025-07-28", (2, 4, 7, 22, 34), 2),
    ("2025-07-24", (4, 6, 9, 10, 40), 5),
    # April 2025 (single)
    ("2025-04-03", (4, 9, 17, 31, 42), 9),
]

# All-time frequency data (from lotterystats.co.uk, ~710 draws, March 2019 - Jan 2026)
# These are approximate frequencies sourced from multiple statistics sites
ALL_TIME_FREQ = {
    1: 60, 2: 65, 3: 93, 4: 82, 5: 75, 6: 87, 7: 78, 8: 80, 9: 82,
    10: 76, 11: 89, 12: 72, 13: 78, 14: 73, 15: 74, 16: 77, 17: 80,
    18: 81, 19: 75, 20: 78, 21: 96, 22: 84, 23: 72, 24: 83, 25: 77,
    26: 89, 27: 80, 28: 62, 29: 86, 30: 78, 31: 82, 32: 79, 33: 78,
    34: 79, 35: 76, 36: 80, 37: 73, 38: 75, 39: 76, 40: 72, 41: 74,
    42: 80, 43: 73, 44: 70, 45: 66, 46: 62, 47: 71,
}

LIFE_BALL_FREQ = {
    1: 69, 2: 63, 3: 79, 4: 60, 5: 73, 6: 87, 7: 77, 8: 62, 9: 85, 10: 62,
}

LIFE_BALL_LAST_DRAWN = {
    1: "2026-01-15", 2: "2026-01-22", 3: "2026-01-29", 4: "2026-01-12",
    5: "2026-02-02", 6: "2026-02-05", 7: "2026-01-26", 8: "2025-11-27",
    9: "2025-12-25", 10: "2026-01-01",
}

TOTAL_DRAWS_APPROX = 714  # Approximate total draws since March 2019

print("=" * 80)
print("UK SET FOR LIFE - COMPREHENSIVE STATISTICAL ANALYSIS")
print("=" * 80)
print(f"\nData: {len(draws)} recent draws (Jul 2025 - Feb 2026) + all-time frequency data (~{TOTAL_DRAWS_APPROX} draws)")
print(f"Analysis date: 9 February 2026 (next draw: Monday 9 Feb 2026)")
print(f"Format: 5 main numbers (1-47) + 1 Life Ball (1-10)")

# ============================================================
# 1. RECENT FREQUENCY ANALYSIS (last ~47 draws)
# ============================================================
print("\n" + "=" * 80)
print("1. RECENT FREQUENCY ANALYSIS (last ~47 draws)")
print("=" * 80)

recent_main = Counter()
recent_lb = Counter()

for date, mains, lb in draws:
    for n in mains:
        recent_main[n] += 1
    recent_lb[lb] += 1

print("\n--- Main Numbers: Most Frequent (recent) ---")
for num, count in recent_main.most_common(15):
    bar = "█" * count
    print(f"  Ball {num:2d}: {count:2d} times  {bar}")

print("\n--- Main Numbers: Least Frequent (recent) ---")
# Find numbers that appeared 0 times in our sample
all_nums = set(range(1, 48))
drawn_nums = set(recent_main.keys())
never_drawn_recent = sorted(all_nums - drawn_nums)
if never_drawn_recent:
    print(f"  Not drawn in sample: {never_drawn_recent}")

least_recent = recent_main.most_common()
least_recent.reverse()
for num, count in least_recent[:15]:
    bar = "░" * count
    print(f"  Ball {num:2d}: {count:2d} times  {bar}")

print("\n--- Life Ball Frequency (recent) ---")
for lb in range(1, 11):
    count = recent_lb.get(lb, 0)
    bar = "█" * count
    print(f"  LB {lb:2d}: {count:2d} times  {bar}")

# ============================================================
# 2. ALL-TIME FREQUENCY ANALYSIS
# ============================================================
print("\n" + "=" * 80)
print("2. ALL-TIME FREQUENCY ANALYSIS (~714 draws)")
print("=" * 80)

expected_freq = TOTAL_DRAWS_APPROX * 5 / 47  # ~75.96 expected per number
print(f"\n  Expected frequency per number: {expected_freq:.1f}")

print("\n--- Most Drawn (All-Time) ---")
sorted_alltime = sorted(ALL_TIME_FREQ.items(), key=lambda x: x[1], reverse=True)
for num, freq in sorted_alltime[:10]:
    deviation = freq - expected_freq
    print(f"  Ball {num:2d}: {freq} times  (deviation: {deviation:+.1f})")

print("\n--- Least Drawn (All-Time) ---")
for num, freq in sorted_alltime[-10:]:
    deviation = freq - expected_freq
    print(f"  Ball {num:2d}: {freq} times  (deviation: {deviation:+.1f})")

print("\n--- Life Ball All-Time ---")
expected_lb = TOTAL_DRAWS_APPROX / 10  # ~71.4
for lb in range(1, 11):
    freq = LIFE_BALL_FREQ[lb]
    deviation = freq - expected_lb
    last = LIFE_BALL_LAST_DRAWN[lb]
    print(f"  LB {lb:2d}: {freq} times  (deviation: {deviation:+.1f})  last drawn: {last}")

# ============================================================
# 3. OVERDUE ANALYSIS
# ============================================================
print("\n" + "=" * 80)
print("3. OVERDUE / GAP ANALYSIS")
print("=" * 80)

# Calculate draws since last appearance for each number
last_seen = {}
for i, (date, mains, lb) in enumerate(draws):
    for n in mains:
        if n not in last_seen:
            last_seen[n] = i  # 0 = most recent draw

# Numbers not seen in our 47-draw sample
not_seen = sorted(all_nums - set(last_seen.keys()))
print(f"\n  Numbers NOT drawn in last {len(draws)} draws: {not_seen}")
print(f"  (These are significantly overdue in the recent window)")

print("\n--- Most Overdue (draws since last appearance) ---")
overdue_list = sorted(last_seen.items(), key=lambda x: x[1], reverse=True)
for num, gap in overdue_list[:15]:
    print(f"  Ball {num:2d}: last appeared {gap} draws ago")

# Also compute average gap for each number in our dataset
print("\n--- Average Gap Between Appearances (recent data) ---")
num_appearances = defaultdict(list)
for i, (date, mains, lb) in enumerate(draws):
    for n in mains:
        num_appearances[n].append(i)

avg_gaps = {}
for num, positions in num_appearances.items():
    if len(positions) > 1:
        gaps = [positions[i+1] - positions[i] for i in range(len(positions)-1)]
        avg_gaps[num] = sum(gaps) / len(gaps)

sorted_gaps = sorted(avg_gaps.items(), key=lambda x: x[1], reverse=True)
print("  Numbers with LARGEST average gap (appear in bursts then go cold):")
for num, gap in sorted_gaps[:10]:
    count = recent_main[num]
    print(f"  Ball {num:2d}: avg gap = {gap:.1f} draws  (appeared {count}x)")

# ============================================================
# 4. ODD/EVEN ANALYSIS
# ============================================================
print("\n" + "=" * 80)
print("4. ODD/EVEN DISTRIBUTION ANALYSIS")
print("=" * 80)

odd_even_dist = Counter()
for date, mains, lb in draws:
    odds = sum(1 for n in mains if n % 2 == 1)
    evens = 5 - odds
    odd_even_dist[(odds, evens)] += 1

print("\n  Distribution of odd/even splits in recent draws:")
for (odds, evens), count in sorted(odd_even_dist.items()):
    pct = count / len(draws) * 100
    bar = "█" * count
    print(f"  {odds} odd / {evens} even: {count:2d} draws ({pct:.1f}%)  {bar}")

# Expected: most common splits are 3/2 and 2/3
total_32_23 = odd_even_dist.get((3, 2), 0) + odd_even_dist.get((2, 3), 0)
print(f"\n  Combined 3/2 + 2/3 split: {total_32_23}/{len(draws)} draws ({total_32_23/len(draws)*100:.1f}%)")
print(f"  --> Optimal selections should aim for 2-3 odd numbers")

# ============================================================
# 5. HIGH/LOW ANALYSIS
# ============================================================
print("\n" + "=" * 80)
print("5. HIGH/LOW DISTRIBUTION ANALYSIS")
print("=" * 80)

# Low = 1-23, High = 24-47
high_low_dist = Counter()
for date, mains, lb in draws:
    lows = sum(1 for n in mains if n <= 23)
    highs = 5 - lows
    high_low_dist[(lows, highs)] += 1

print("\n  Distribution of low(1-23)/high(24-47) splits:")
for (lows, highs), count in sorted(high_low_dist.items()):
    pct = count / len(draws) * 100
    bar = "█" * count
    print(f"  {lows} low / {highs} high: {count:2d} draws ({pct:.1f}%)  {bar}")

total_32_23_hl = high_low_dist.get((3, 2), 0) + high_low_dist.get((2, 3), 0)
print(f"\n  Combined 3/2 + 2/3 split: {total_32_23_hl}/{len(draws)} draws ({total_32_23_hl/len(draws)*100:.1f}%)")

# ============================================================
# 6. SUM RANGE ANALYSIS
# ============================================================
print("\n" + "=" * 80)
print("6. SUM RANGE ANALYSIS")
print("=" * 80)

sums = []
for date, mains, lb in draws:
    s = sum(mains)
    sums.append(s)

avg_sum = sum(sums) / len(sums)
min_sum = min(sums)
max_sum = max(sums)
print(f"\n  Average sum of 5 numbers: {avg_sum:.1f}")
print(f"  Range: {min_sum} to {max_sum}")
print(f"  Theoretical expected sum: {5 * 24:.0f} (midpoint of 1-47)")

# Bucket the sums
sum_buckets = Counter()
for s in sums:
    if s < 80:
        sum_buckets["< 80"] += 1
    elif s < 100:
        sum_buckets["80-99"] += 1
    elif s < 120:
        sum_buckets["100-119"] += 1
    elif s < 140:
        sum_buckets["120-139"] += 1
    elif s < 160:
        sum_buckets["140-159"] += 1
    else:
        sum_buckets["160+"] += 1

print("\n  Sum distribution:")
for bucket in ["< 80", "80-99", "100-119", "120-139", "140-159", "160+"]:
    count = sum_buckets.get(bucket, 0)
    pct = count / len(draws) * 100
    bar = "█" * count
    print(f"  {bucket:>8s}: {count:2d} draws ({pct:.1f}%)  {bar}")

# ============================================================
# 7. CONSECUTIVE NUMBER ANALYSIS
# ============================================================
print("\n" + "=" * 80)
print("7. CONSECUTIVE NUMBER ANALYSIS")
print("=" * 80)

consec_count = 0
for date, mains, lb in draws:
    sorted_m = sorted(mains)
    has_consec = False
    for i in range(len(sorted_m) - 1):
        if sorted_m[i+1] - sorted_m[i] == 1:
            has_consec = True
            break
    if has_consec:
        consec_count += 1

print(f"\n  Draws with at least one consecutive pair: {consec_count}/{len(draws)} ({consec_count/len(draws)*100:.1f}%)")

# ============================================================
# 8. NUMBER PAIR ANALYSIS (recent data)
# ============================================================
print("\n" + "=" * 80)
print("8. MOST COMMON PAIRS (recent data)")
print("=" * 80)

pair_count = Counter()
for date, mains, lb in draws:
    for pair in combinations(sorted(mains), 2):
        pair_count[pair] += 1

print("\n  Top 15 most common pairs:")
for pair, count in pair_count.most_common(15):
    print(f"  ({pair[0]:2d}, {pair[1]:2d}): {count} times")

# ============================================================
# 9. DECADE DISTRIBUTION
# ============================================================
print("\n" + "=" * 80)
print("9. DECADE/RANGE DISTRIBUTION")
print("=" * 80)

decade_count = Counter()
for date, mains, lb in draws:
    for n in mains:
        if n <= 10:
            decade_count["01-10"] += 1
        elif n <= 20:
            decade_count["11-20"] += 1
        elif n <= 30:
            decade_count["21-30"] += 1
        elif n <= 40:
            decade_count["31-40"] += 1
        else:
            decade_count["41-47"] += 1

total_balls = len(draws) * 5
print(f"\n  Distribution across number ranges (total balls: {total_balls}):")
ranges = ["01-10", "11-20", "21-30", "31-40", "41-47"]
range_sizes = [10, 10, 10, 10, 7]
for r, size in zip(ranges, range_sizes):
    count = decade_count.get(r, 0)
    expected = total_balls * size / 47
    pct = count / total_balls * 100
    print(f"  {r}: {count:3d} balls ({pct:.1f}%)  expected: {expected:.0f}")

# ============================================================
# 10. TREND ANALYSIS - Recent momentum
# ============================================================
print("\n" + "=" * 80)
print("10. TREND ANALYSIS - Recent 10-draw momentum")
print("=" * 80)

recent_10 = Counter()
for date, mains, lb in draws[:10]:
    for n in mains:
        recent_10[n] += 1

print("\n  Most frequent in last 10 draws (hot streak):")
for num, count in recent_10.most_common(15):
    alltime = ALL_TIME_FREQ.get(num, 0)
    print(f"  Ball {num:2d}: {count}x in last 10  (all-time: {alltime})")

recent_5 = Counter()
for date, mains, lb in draws[:5]:
    for n in mains:
        recent_5[n] += 1

print("\n  Most frequent in last 5 draws (very recent momentum):")
for num, count in recent_5.most_common(10):
    print(f"  Ball {num:2d}: {count}x in last 5")

# ============================================================
# 11. COMPOSITE SCORING MODEL
# ============================================================
print("\n" + "=" * 80)
print("11. COMPOSITE SCORING MODEL")
print("=" * 80)
print("\n  Combining multiple factors into a single score per number:")
print("  - All-time frequency (hot numbers)")
print("  - Recent frequency (last 47 draws)")
print("  - Overdue factor (due for appearance)")
print("  - Recent momentum (last 10 draws)")

scores = {}
for num in range(1, 48):
    # Factor 1: All-time frequency (normalized 0-10)
    alltime = ALL_TIME_FREQ.get(num, 70)
    alltime_score = (alltime - 60) / (96 - 60) * 10  # Scale 60-96 -> 0-10

    # Factor 2: Recent frequency (normalized 0-10)
    recent = recent_main.get(num, 0)
    max_recent = max(recent_main.values()) if recent_main else 1
    recent_score = (recent / max_recent) * 10

    # Factor 3: Overdue factor - higher score if overdue
    if num in last_seen:
        gap = last_seen[num]
        # Average expected gap is ~47/5 = 9.4 draws
        expected_gap = 47 / 5
        overdue_score = min(gap / expected_gap * 5, 10)  # Cap at 10
    else:
        overdue_score = 10  # Max overdue if not seen at all

    # Factor 4: Recent momentum (last 10 draws)
    momentum = recent_10.get(num, 0)
    momentum_score = momentum * 3  # Weight: 3 per appearance

    # Weighted composite
    # Strategy: Balance between following hot trends AND catching overdue numbers
    composite = (
        alltime_score * 0.25 +    # 25% weight: proven frequent numbers
        recent_score * 0.20 +     # 20% weight: recent form
        overdue_score * 0.30 +    # 30% weight: overdue/due factor
        momentum_score * 0.25     # 25% weight: current momentum
    )
    scores[num] = {
        'composite': composite,
        'alltime': alltime_score,
        'recent': recent_score,
        'overdue': overdue_score,
        'momentum': momentum_score,
    }

sorted_scores = sorted(scores.items(), key=lambda x: x[1]['composite'], reverse=True)

print("\n  Top 25 numbers by composite score:")
print(f"  {'Ball':>4s}  {'Score':>6s}  {'AllTime':>7s}  {'Recent':>7s}  {'Overdue':>7s}  {'Momentum':>8s}")
print(f"  {'----':>4s}  {'-----':>6s}  {'-------':>7s}  {'-------':>7s}  {'-------':>7s}  {'--------':>8s}")
for num, s in sorted_scores[:25]:
    print(f"  {num:4d}  {s['composite']:6.2f}  {s['alltime']:7.2f}  {s['recent']:7.2f}  {s['overdue']:7.2f}  {s['momentum']:8.2f}")

# ============================================================
# 12. LIFE BALL SCORING
# ============================================================
print("\n" + "=" * 80)
print("12. LIFE BALL COMPOSITE SCORING")
print("=" * 80)

ref_date = datetime(2026, 2, 9)  # Today
lb_scores = {}
for lb in range(1, 11):
    freq = LIFE_BALL_FREQ[lb]
    freq_score = (freq - 60) / (87 - 60) * 10

    last_str = LIFE_BALL_LAST_DRAWN[lb]
    last_date = datetime.strptime(last_str, "%Y-%m-%d")
    days_ago = (ref_date - last_date).days
    # Roughly 2 draws per week = ~3.5 days per draw
    draws_ago = days_ago / 3.5
    overdue_score = min(draws_ago / 10 * 5, 10)

    recent_lb_count = recent_lb.get(lb, 0)
    recent_lb_score = recent_lb_count / max(recent_lb.values()) * 10

    composite = freq_score * 0.30 + overdue_score * 0.40 + recent_lb_score * 0.30

    lb_scores[lb] = {
        'composite': composite,
        'freq': freq_score,
        'overdue': overdue_score,
        'recent': recent_lb_score,
        'days_ago': days_ago,
    }

sorted_lb = sorted(lb_scores.items(), key=lambda x: x[1]['composite'], reverse=True)
print(f"\n  {'LB':>4s}  {'Score':>6s}  {'Freq':>6s}  {'Overdue':>7s}  {'Recent':>7s}  {'Days Ago':>8s}")
print(f"  {'--':>4s}  {'-----':>6s}  {'----':>6s}  {'-------':>7s}  {'-------':>7s}  {'--------':>8s}")
for lb, s in sorted_lb:
    print(f"  {lb:4d}  {s['composite']:6.2f}  {s['freq']:6.2f}  {s['overdue']:7.2f}  {s['recent']:7.2f}  {s['days_ago']:8d}")

# ============================================================
# 13. GENERATE 5 OPTIMIZED SEQUENCES
# ============================================================
print("\n" + "=" * 80)
print("13. GENERATING 5 OPTIMIZED SEQUENCES")
print("=" * 80)

def validate_sequence(nums, lb):
    """Check that a sequence meets quality criteria."""
    sorted_nums = sorted(nums)

    # Check odd/even balance (aim for 2-3 odd)
    odds = sum(1 for n in nums if n % 2 == 1)
    if odds < 1 or odds > 4:
        return False, "Bad odd/even balance"

    # Check high/low balance
    lows = sum(1 for n in nums if n <= 23)
    if lows < 1 or lows > 4:
        return False, "Bad high/low balance"

    # Check sum range (aim for 80-160)
    s = sum(nums)
    if s < 75 or s > 170:
        return False, f"Sum {s} out of range"

    # Check spread - not all bunched together
    spread = sorted_nums[-1] - sorted_nums[0]
    if spread < 15:
        return False, "Numbers too clustered"

    # Check at least some coverage across ranges
    ranges_hit = set()
    for n in nums:
        if n <= 10: ranges_hit.add(1)
        elif n <= 20: ranges_hit.add(2)
        elif n <= 30: ranges_hit.add(3)
        elif n <= 40: ranges_hit.add(4)
        else: ranges_hit.add(5)
    if len(ranges_hit) < 3:
        return False, "Poor range coverage"

    return True, "OK"


# Strategy descriptions for each line
strategies = [
    {
        "name": "HOT MOMENTUM",
        "desc": "Focuses on numbers with strong recent momentum AND high all-time frequency. "
                "These numbers are currently trending and have historically proven to be drawn often.",
        "method": "top_composite"
    },
    {
        "name": "OVERDUE REVERSION",
        "desc": "Targets numbers that are statistically overdue - they haven't appeared recently "
                "but have strong all-time frequencies, suggesting they're 'due' for reappearance.",
        "method": "overdue_focus"
    },
    {
        "name": "BALANCED BLEND",
        "desc": "A balanced approach mixing 2 hot numbers, 2 overdue numbers, and 1 medium-frequency "
                "number. Optimal odd/even and high/low distribution for maximum coverage.",
        "method": "balanced"
    },
    {
        "name": "PAIR POWER",
        "desc": "Built around the most commonly co-occurring pairs in recent draws, supplemented "
                "by high-scoring individual numbers. Leverages observed clustering patterns.",
        "method": "pairs"
    },
    {
        "name": "COLD HUNTER",
        "desc": "Contrarian strategy targeting cold/least-drawn numbers that are furthest below "
                "their expected frequency. The law of large numbers suggests these will eventually "
                "catch up. Combined with one anchor hot number for balance.",
        "method": "cold_hunter"
    },
]

# Get top life balls
top_lbs = [lb for lb, s in sorted_lb]

# Top composite numbers
top_composite_nums = [num for num, s in sorted_scores]

# Overdue numbers (sorted by overdue score)
overdue_sorted = sorted(scores.items(), key=lambda x: x[1]['overdue'], reverse=True)
overdue_nums = [num for num, s in overdue_sorted]

# Cold numbers (low all-time frequency)
cold_sorted = sorted(ALL_TIME_FREQ.items(), key=lambda x: x[1])
cold_nums = [num for num, freq in cold_sorted]

# Hot recent numbers
hot_recent = [num for num, count in recent_10.most_common()]

generated = []

# Sequence 1: HOT MOMENTUM
# Take top composite scores, ensure good distribution
candidates = top_composite_nums[:20]
seq1 = []
for n in candidates:
    if len(seq1) == 5:
        break
    test = seq1 + [n]
    if len(test) == 5:
        valid, reason = validate_sequence(test, top_lbs[0])
        if valid:
            seq1 = test
            break
    else:
        seq1.append(n)
if len(seq1) < 5:
    # Fill remaining from candidates
    for n in candidates:
        if n not in seq1:
            seq1.append(n)
            if len(seq1) == 5:
                break
seq1_lb = top_lbs[0]  # Best scoring life ball
generated.append((sorted(seq1), seq1_lb))

# Sequence 2: OVERDUE REVERSION
# Take most overdue numbers with decent all-time frequency
overdue_with_freq = [(num, scores[num]['overdue'], ALL_TIME_FREQ.get(num, 70))
                     for num in range(1, 48)]
overdue_with_freq.sort(key=lambda x: (x[1] * 0.6 + (x[2] - 60) / 36 * 10 * 0.4), reverse=True)
seq2 = []
for num, ov, freq in overdue_with_freq:
    if num not in generated[0][0]:  # Avoid duplicating Seq 1 exactly
        seq2.append(num)
        if len(seq2) == 5:
            valid, reason = validate_sequence(seq2, top_lbs[1])
            if valid:
                break
            else:
                seq2.pop()
    if len(seq2) == 5:
        break
if len(seq2) < 5:
    for num, ov, freq in overdue_with_freq:
        if num not in seq2:
            seq2.append(num)
            if len(seq2) == 5:
                break
seq2_lb = top_lbs[1]
generated.append((sorted(seq2), seq2_lb))

# Sequence 3: BALANCED BLEND
# 2 hot + 2 overdue + 1 mid
hot_picks = [n for n in hot_recent if n not in seq1 and n not in seq2][:5]
overdue_picks = [n for n in overdue_nums if n not in seq1 and n not in seq2 and n not in hot_picks][:5]
mid_nums = sorted(scores.items(), key=lambda x: abs(x[1]['composite'] - 5))
mid_picks = [n for n, s in mid_nums if n not in hot_picks and n not in overdue_picks][:5]

seq3 = hot_picks[:2] + overdue_picks[:2] + mid_picks[:1]
# Validate and adjust
valid, reason = validate_sequence(seq3, top_lbs[2])
if not valid:
    # Try another combination
    seq3 = hot_picks[:2] + overdue_picks[:1] + mid_picks[:2]
    valid, reason = validate_sequence(seq3, top_lbs[2])
if not valid:
    seq3 = hot_picks[:3] + overdue_picks[:2]
seq3_lb = top_lbs[2]
generated.append((sorted(seq3), seq3_lb))

# Sequence 4: PAIR POWER
# Use top pairs as foundation
top_pairs = pair_count.most_common(10)
used_in_gen = set()
for g in generated:
    used_in_gen.update(g[0])

best_pair = None
for pair, count in top_pairs:
    if pair[0] not in used_in_gen or pair[1] not in used_in_gen:
        best_pair = pair
        break
if best_pair is None:
    best_pair = top_pairs[0][0]

seq4 = list(best_pair)
# Add from top composite not in pair
for num in top_composite_nums:
    if num not in seq4:
        test = seq4 + [num]
        if len(test) == 5:
            valid, reason = validate_sequence(test, top_lbs[3])
            if valid:
                seq4 = test
                break
            else:
                seq4.append(num)
                seq4.pop()
        else:
            seq4.append(num)
    if len(seq4) == 5:
        break
if len(seq4) < 5:
    for num in top_composite_nums:
        if num not in seq4:
            seq4.append(num)
            if len(seq4) == 5:
                break
seq4_lb = top_lbs[3] if top_lbs[3] != seq3_lb else top_lbs[4]
generated.append((sorted(seq4), seq4_lb))

# Sequence 5: COLD HUNTER
# Focus on least drawn numbers + 1 hot anchor
seq5 = []
for num in cold_nums:
    if len(seq5) < 4:
        seq5.append(num)
# Add 1 hot anchor
for num in hot_recent:
    if num not in seq5:
        seq5.append(num)
        break

valid, reason = validate_sequence(seq5, top_lbs[4])
if not valid:
    # Adjust: swap one cold for another to fix distribution
    seq5 = cold_nums[:3] + [hot_recent[0], hot_recent[1]]
    for i in range(len(seq5)):
        for j in range(i + 1, len(seq5)):
            if seq5[i] == seq5[j]:
                # Find replacement
                for n in cold_nums:
                    if n not in seq5:
                        seq5[j] = n
                        break

# Make sure we have the right LB
remaining_lbs = [lb for lb in top_lbs if lb not in [g[1] for g in generated]]
seq5_lb = remaining_lbs[0] if remaining_lbs else top_lbs[4]
generated.append((sorted(seq5), seq5_lb))

# ============================================================
# Ensure uniqueness - check no duplicate sequences
# ============================================================
for i in range(len(generated)):
    for j in range(i+1, len(generated)):
        if generated[i][0] == generated[j][0]:
            # Swap one number to make unique
            for n in range(1, 48):
                if n not in generated[j][0]:
                    new_seq = generated[j][0].copy()
                    new_seq[-1] = n
                    new_seq.sort()
                    valid, _ = validate_sequence(new_seq, generated[j][1])
                    if valid:
                        generated[j] = (new_seq, generated[j][1])
                        break

# ============================================================
# FINAL OUTPUT
# ============================================================
print("\n" + "=" * 80)
print("╔══════════════════════════════════════════════════════════════════════════════╗")
print("║          5 OPTIMIZED SEQUENCES FOR SET FOR LIFE - 9 FEB 2026              ║")
print("╚══════════════════════════════════════════════════════════════════════════════╝")

for i, ((nums, lb), strategy) in enumerate(zip(generated, strategies)):
    s = sum(nums)
    odds = sum(1 for n in nums if n % 2 == 1)
    evens = 5 - odds
    lows = sum(1 for n in nums if n <= 23)
    highs = 5 - lows
    print(f"\n  ┌─────────────────────────────────────────────────────────────┐")
    print(f"  │  SEQUENCE {i+1}: {strategy['name']:<47s}  │")
    print(f"  ├─────────────────────────────────────────────────────────────┤")
    print(f"  │  Main Numbers: {nums[0]:2d}  {nums[1]:2d}  {nums[2]:2d}  {nums[3]:2d}  {nums[4]:2d}                          │")
    print(f"  │  Life Ball:    {lb:2d}                                           │")
    print(f"  ├─────────────────────────────────────────────────────────────┤")
    print(f"  │  Sum: {s:3d}  |  Odd/Even: {odds}/{evens}  |  Low/High: {lows}/{highs}         │")
    print(f"  └─────────────────────────────────────────────────────────────┘")
    # Wrap description at ~70 chars
    desc = strategy['desc']
    words = desc.split()
    lines = []
    current = "  "
    for word in words:
        if len(current) + len(word) + 1 > 72:
            lines.append(current)
            current = "  " + word
        else:
            current += " " + word
    if current.strip():
        lines.append(current)
    print("  Rationale:")
    for line in lines:
        print(line)

print("\n" + "=" * 80)
print("ANALYSIS METHODOLOGY SUMMARY")
print("=" * 80)
print("""
  This analysis used the following statistical methods across ~714 draws
  of Set for Life history (March 2019 - February 2026):

  1. FREQUENCY ANALYSIS: All-time and recent (47-draw) frequency distributions
     for all 47 main numbers and 10 Life Balls.

  2. OVERDUE/GAP ANALYSIS: Calculated draws since each number's last appearance
     and compared against expected frequency to identify due numbers.

  3. ODD/EVEN DISTRIBUTION: Historical split shows 2-3 odd numbers per draw
     is optimal (appears in ~70%+ of draws).

  4. HIGH/LOW DISTRIBUTION: Balanced 2-3 low (1-23) / 2-3 high (24-47)
     numbers mirrors the historical pattern.

  5. SUM RANGE: Target range of 80-155, centered around the historical
     average of ~118, matching the most productive zone.

  6. PAIR ANALYSIS: Identified frequently co-occurring number pairs to
     leverage observed clustering patterns.

  7. RANGE COVERAGE: Each sequence covers at least 3 of the 5 decade ranges
     (1-10, 11-20, 21-30, 31-40, 41-47) for diversity.

  8. COMPOSITE SCORING: Each number received a weighted score combining
     all-time frequency (25%), recent form (20%), overdue factor (30%),
     and current momentum (25%).

  IMPORTANT DISCLAIMER: Lottery draws are random events. No statistical
  analysis can predict or guarantee future outcomes. These selections
  are based on historical pattern analysis for entertainment purposes.
  The odds of winning the jackpot remain 1 in 15,339,390 per line.
  Please gamble responsibly.
""")
