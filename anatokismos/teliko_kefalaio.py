# Python 8.3.5
# Εύρεση τελικού κεφαλαίου σε ακέραιες χρονικές περιόδους.
# Σύνθετος τόκος ή ανατοκισμός. 

present_value = float(input("Αρχικό κεφάλαιο: "))
# Παράδειγμα: επιτόκιο 0.06 αντί για 6%.
interest_rate = float(input("Επιτόκιο: ")) 
# Παράδειγμα 1: 5 έτη και 1 εξάμηνο --> 5 * 2 + 1 = 11 εξάμηνα --> Χρονικά διαστήματα: 11.
# Παράδειγμα 2: 4 έτη --> Χρονικά διαστήματα: 4.
time = int(input("Χρονικά διαστήματα: ")) 
capital = present_value * (1 + interest_rate) ** time
print ("Τελικό κεφάλαιο:", capital)
