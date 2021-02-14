# Python 3.8.5
# Μετατροπή ημερομισθίου (6 ωρών και 40 λεπτών) σε ωρομίσθιο.

daily_salary = float(input("Δώστε ποσό ημερομισθίου: "))
hourly_salary = daily_salary * 0.15
print ("Το ωρομίσθιο είναι", round (hourly_salary, 2), "ευρώ")
