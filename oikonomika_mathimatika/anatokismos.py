# Python 8.3.5
# Εύρεση τελικού κεφαλαίου.
# Σύνθετος τόκος ή ανατοκισμός. 

present_value = float(input("Αρχικό κεφάλαιο: "))
i = float(input("Επιτόκιο (π.χ: 0.06 αντί για 6%): "))
n = float(input("Χρονικά διαστήματα: "))
compount_amount = present_value * (1 + i) ** n
print ("Τελικό κεφάλαιο:", compount_amount)
