# Python 8.3.5
# Εύρεση τόκου σε μέρες.
# Έτος: πολιτικό - μεικτό - εμπορικό.

capital = float(input("Κεφάλαιο: "))
days = int(input("Τοκοφόφες Ημέρες: "))
interest_rate = float(input("Επιτόκιο: "))
days_in_year = int(input("Ημέρες του έτους: "))
while yearly_days != 360 and yearly_days != 365 and yearly_days != 366:
    print ("Προσπαθήστε ξανά!"
"\n" + "Δώστε 360 ή 365 ή 366 ημέρες.")
    days_in_year = int(input("Ημέρες του έτους: "))
interest = capital * days * interest_rate / days_in_year
print ("Ο τόκος είναι:", interest)
