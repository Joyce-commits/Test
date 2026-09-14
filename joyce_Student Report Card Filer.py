# pip install pandas
import pandas as pd

print("=" * 60)
print("         STUDENT REPORT CARD ANALYSER")
print("=" * 60)

# ── DATASET ──────────────────────────────────────────────────
# 20 students, 5 subjects — realistic school marks
data = {
    "Name": [
        "Aarav", "Priya", "Rohan", "Sneha", "Kiran",
        "Meera", "Arjun", "Divya", "Rahul", "Ananya",
        "Vikram", "Pooja", "Siddharth", "Riya", "Aditya",
        "Nisha", "Kabir", "Tanya", "Ishaan", "Simran"
    ],
    "Math":    [87, 45, 72, 91, 38, 65, 88, 54, 76, 93,
                42, 79, 85, 61, 70, 55, 88, 47, 82, 95],
    "Science": [78, 52, 68, 88, 41, 71, 82, 49, 80, 89,
                39, 74, 90, 58, 65, 60, 85, 50, 77, 91],
    "English": [82, 61, 74, 85, 55, 68, 79, 62, 71, 87,
                48, 80, 83, 70, 73, 63, 76, 58, 69, 92],
    "History": [75, 58, 65, 80, 42, 72, 77, 55, 68, 84,
                44, 76, 88, 63, 67, 59, 80, 52, 72, 88],
    "CS":      [91, 48, 80, 94, 35, 63, 95, 57, 85, 96,
                40, 82, 92, 67, 78, 61, 90, 44, 88, 97],
}

df = pd.DataFrame(data)

# ── STEP 1 — CALCULATED COLUMNS ──────────────────────────────
print("\n📐 STEP 1: Computing totals and averages...")
df["Total"]   = df[["Math", "Science", "English", "History", "CS"]].sum(axis=1)

# In pandas, df.sum(axis=1) calculates the sum of values horizontally across the columns for each row
df["Average"] = df["Total"] / 5

print("*" * 100)
#----------------------------------------------------------------------------------------

# ── STEP 2 — GRADE COLUMN ────────────────────────────────────
def assign_grade(avg):
    if avg >= 90: return "A+"
    elif avg >= 80: return "A"
    elif avg >= 70: return "B"
    elif avg >= 60: return "C"
    elif avg >= 50: return "D"
    else: return "F"

df["Grade"] = df["Average"].apply(assign_grade)

print("*" * 100)
#----------------------------------------------------------------------------------------

# ── STEP 3 — PASS/FAIL ───────────────────────────────────────
# A student PASSES only if they score >= 40 in ALL subjects
subjects = ["Math", "Science", "English", "History", "CS"]
df["Passed_All"] = df[subjects].min(axis=1) >= 40
df["Status"]     = df["Passed_All"].map({True: "PASS ✅", False: "FAIL ❌"})

print("*" * 100)
#----------------------------------------------------------------------------------------

# ── FULL REPORT ───────────────────────────────────────────────
print("\n📋 FULL CLASS REPORT")
print("-" * 60)
display_cols = ["Name", "Math", "Science", "English", "History", "CS", "Average", "Grade", "Status"]

# set_option will controls how DataFrames look, how data formats display, and how computations handle memory or plotting

pd.set_option("display.width", 120)
pd.set_option("display.max_columns", 10)


print(df[display_cols].to_string(index=False))

print("*" * 100)
#----------------------------------------------------------------------------------------

# ── STEP 4 — FILTER: PASSED STUDENTS ONLY ────────────────────
passed_df = df[df["Passed_All"] == True].copy()
print(f"\n✅ STUDENTS WHO PASSED ALL SUBJECTS: {len(passed_df)} / {len(df)}")

print("*" * 100)
#----------------------------------------------------------------------------------------

# ── STEP 5 — SORT BY AVERAGE (TOP 5) ─────────────────────────
# head method will take only the first 5 record in the table

top5 = passed_df.sort_values("Average", ascending=False).head(5)
print("\n🏆 TOP 5 STUDENTS (by Average)")
print("-" * 45)
print(top5[["Name", "Average", "Grade", "Status"]].to_string(index=False))

print("*" * 100)
#----------------------------------------------------------------------------------------

# ── STEP 6 — SUBJECT STATISTICS ──────────────────────────────
print("\n📊 SUBJECT-WISE CLASS PERFORMANCE")
print("-" * 45)
for subj in subjects:
    col = df[subj]
    pass_count = (col >= 40).sum()
    print(f"  {subj:<10}: Avg={col.mean():.1f}  High={col.max()}  Low={col.min()}  Pass={pass_count}/20")
    
print("*" * 100)
#----------------------------------------------------------------------------------------

# ── STEP 7 — GRADE DISTRIBUTION ──────────────────────────────
print("\n📈 GRADE DISTRIBUTION")
print("-" * 25)
grade_counts = df["Grade"].value_counts().sort_index()
for grade, count in grade_counts.items():
    bar = "█" * count
    print(f"  {grade:<3}: {bar} ({count})")
    
print("*" * 100)
#----------------------------------------------------------------------------------------


# ── STEP 8 — FAILED STUDENTS BREAKDOWN ───────────────────────
failed_df = df[df["Passed_All"] == False]
print(f"\n❌ FAILED STUDENTS ({len(failed_df)})")
print("-" * 45)
for _, row in failed_df.iterrows():
    failed_subjects = [s for s in subjects if row[s] < 40]
    print(f"  {row['Name']:<12}: Failed in {failed_subjects}")
    
print("*" * 100)
#----------------------------------------------------------------------------------------
    
# ── SUMMARY ──────────────────────────────────────────────────
print("\n" + "=" * 60)
print(f"  Class Average   : {df['Average'].mean():.1f}")

# df.loc will lock the particular row

# idmax() give you the name of the maximum value

print(f"  Highest Scorer  : {df.loc[df['Average'].idxmax(), 'Name']} ({df['Average'].max():.1f})")
print(f"  Lowest Scorer   : {df.loc[df['Average'].idxmin(), 'Name']} ({df['Average'].min():.1f})")
print(f"  Pass Rate       : {len(passed_df)}/{len(df)} ({len(passed_df)/len(df)*100:.0f}%)")
print("=" * 60)


    



    


