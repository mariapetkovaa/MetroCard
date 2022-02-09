def cards():
    if card_choice == "1":
        print("""1 - Pay-Per-Ride \nCost per swipe: $2.75. 
\n\nYou put a dollar value on the card and pay $2.75 at the beginning of each trip.
The minimum balance for new cards is $5.50, the cost of two swipes.
\nYou can combine time and value on the same MetroCard. Time will always be used first. 
Value will become available the time on your card runs out.
PATH, AirTrain, and Express buses will always deduct from the value on your card.""")

    elif card_choice == "2":
        print("""2 - 7-Day or 30-Day Unlimited \nCost: $33 (7-day) or $127 (30-day). 
        \n\nYou have unlimited swipes on the subway and local buses for either 7 or 30 days. 
\nYour MetroCard can only hold one Unlimited Ride refill at a time. 
You can’t pause an unlimited ride card once you’ve started using it. 
\nYou can combine time and value on the same MetroCard. 
Time will always be used first. Value will become available the time on your card runs out. 
PATH, AirTrain, and Express buses will always deduct from the value on your card.""")

    elif card_choice == "3":
        print("""3 - 7-Day Unlimited Express Bus Plus \nCost: $62. 
\n\nYou have unlimited swipes on express buses, local buses, and the subway for 7 days. 
Your MetroCard can only hold one Unlimited Ride refill at a time. 
You can’t pause an unlimited ride card once you’ve started using it.""")

    elif card_choice == "4":
        print("""4 - Single Ride \nCost: $3. \n\nThese are only available at ticket machines. They aren’t refillable. 
These are useful if you don’t want to put the $5.50 minimum on a pay-per-ride card.  
You cannot transfer between the subway and the bus with this fare. 
If you’re transferring between buses, ask the driver for a paper transfer when you board the first bus.""")

    elif card_choice == "5":
        print("""5 - Student MetroCards
\n\nSchools distribute MetroCards that let eligible students get to and from school and school-related activities. 
As with regular MetroCards, Student MetroCards allow for a free transfer between the subway and 
local/limited/Select Bus services, or a free transfer between buses  
You can use your card for three rides each school day, between 5:30 a.m. and 8:30 p.m. 
Student MetroCards are good for one semester.""")

    elif card_choice == "6":
        print("""6 - Reduced Fare \nCost: 50% of the base fare.  
\nRiders who are 65 or older and riders with qualifying disabilities can apply for a reduced fare card.  
There is also an EasyPay Reduced Fare option for automatic refills.""")

    elif card_choice == "7":
        print("""7 - JFK-AirTrain 30-Day Unlimited Ride \nCost: $40. 
        \n\nThese are good for unlimited JFK-AirTrain trips until midnight, 30 days from first use.  
Your MetroCard can only hold one Unlimited Ride refill at a time. 
You can’t pause an unlimited ride card once you’ve started using it.""")

    elif card_choice == "8":
        print("""8 - JFK-AirTrain 10-Trip \nCost: $25.  
\n\nThese are good for 10 JFK AirTrain trips until midnight, 30 days from first use.  
You can buy these only at MetroCard Vending Machines in Howard Beach and Jamaica Air Train stations.""")

    elif card_choice == "9":
        print("""9 - AAR MetroCard 
\nThe AAR MetroCard gives Paratransit customers four free trips a day using the subways, local buses, 
Select Bus Service (SBS), and Staten Island Railway (SIR).  
\nA day is a 24-hour calendar day, from midnight to 11:59 p.m. 
Like any other MetroCard, you get an automatic free transfer between the subway and a local bus route, 
SIR and a local bus, or between two local bus routes.""")


print("This is your NYC MetroCard Calculator!")
name = input("Enter your name, please: ")
print("Hello, " + name + "!" + """\n\nYou can choose from the following card types: 
\n1 - Pay-Per-Ride;
\n2 - 7-Day or 30-Day Unlimited;
\n3 - 7-Day Unlimited Express Bus Plus;
\n4 - Single Ride;
\n5 - Student MetroCards;
\n6 - Reduced Fare;
\n7 - JFK-AirTrain 30-Day Unlimited Ride;
\n8 - JFK-AirTrain 10-Trip;
\n9 - AAR MetroCard""")
card_choice = input("Choose a card type: ")
cards()
print("\nEnjoy your ride!")
