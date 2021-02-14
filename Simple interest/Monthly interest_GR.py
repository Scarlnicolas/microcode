# Python 8.3.5
# Εύρεση τόκου σε μήνες. 

capital = float(input("Κεφάλαιο: "))
months = int(input("Μήνες: "))
interest_rate = float(input("Επιτόκιο: "))
interest = capital * months * interest_rate / 12
print ("Ο τόκος είναι:", round(interest,2), "ευρώ")
