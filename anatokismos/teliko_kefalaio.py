# Python 8.3.5
# Εύρεση τελικού κεφαλαίου σε ακέραιες χρονικές περιόδους.
# Σύνθετος τόκος ή ανατοκισμός. 

present_value = float(input("Αρχικό κεφάλαιο: "))
# Παράδειγμα: επιτόκιο 0.06 αντί για 6%.
epi = float(input("Επιτόκιο: ")) 
# Παράδειγμα 1: 5 έτη και 1 εξάμηνο --> 5 * 2 + 1 = 11 εξάμηνα --> Χρονικά διαστήματα: 11.
# Παράδειγμα 2: 4 έτη --> Χρονικά διαστήματα: 4.
chr = int(input("Χρονικά διαστήματα: ")) 
tel_Kef = present_value * (1 + epi) ** chr
print ("Τελικό κεφάλαιο:", tel_Kef)
