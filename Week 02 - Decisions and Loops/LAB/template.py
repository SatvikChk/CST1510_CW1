


# ==================================================================== INPUT
# 1. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

label = input("Enter the label: ")      # replace with an input() call
value = float(input("Enter the value: "))     # replace with an input() call, converted with float()
limit = float(input("Enter the limit: "))     # replace with an input() call, converted with float()


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

difference = value - limit   # replace with your calculation
percent = (difference / limit) * 100 # replace with your calculation
# 3. Decide a status and store it in a variable called status.
#
#    Threshold : if / else        -> "OVER LIMIT" or "OK"
#    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
#                                     "WARNING" (90% or more), otherwise "OK"

status = percent
if status >= 100:
    print("OVER LIMIT")
elif status >= 90:
    print("WARNING")
else:
    print("OK")


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"  Value:      {value:>10.2f}")
print(f"  Limit:      {limit:>10.2f}")
print(f"  Difference: {difference:>10.2f}")
print(f"  Percent:    {percent:>10.2f}%")
print(f"  Status:     {status:>10}")

print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
