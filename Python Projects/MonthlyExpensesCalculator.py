# Aaron Williams
# Program: Monthly Budget Tracker
# Description: Tracks your spending for the month


monthly_funds = input("Enter Monthly Funds $")
monthly_funds = float(monthly_funds)
# initialize loop count and total value

loop_count = 0

total_receipt = 0

# loop till 12 times using while type loop

while loop_count < 12:
    # get receipt

    g_receipt = input("Enter amount on Grocery receipt $")

    # add to total_receipt

    total_receipt += float(g_receipt)

    # increment loop counter

    loop_count += 1

    # loop till 8 times using for type loop

for number in range(8):
    m_receipt = input("Enter amount on miscellaneous receipts $")

    total_receipt += float(m_receipt)

# check if total receipt is less than monthly fund

if total_receipt < monthly_funds:

    # inform within budget

    print("You Did it, you stayed within your budget, GREAT JOB controlling your spending!!!",
          "{:.2f}".format(total_receipt))


else:

    # inform exceeded budget

    print("Unfortunately you have exceeded your budget, work on controlling your spending",
          "{:.2f}".format(total_receipt))
