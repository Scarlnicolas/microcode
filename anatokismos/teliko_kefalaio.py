# Python 8.3.5
# Εύρεση τελικού κεφαλαίου σε ακέραιες χρονικές περιόδους.
# Σύνθετος τόκος ή ανατοκισμός. 

present_value = float(input("Αρχικό κεφάλαιο: "))
i = float(input("Επιτόκιο: ")) # Για παράδειγμα, 0.06 αντί για 6%.
n = int(input("Χρονικά διαστήματα: "))
compount_amount = present_value * (1 + i) ** n
print ("Τελικό κεφάλαιο:", compount_amount)
