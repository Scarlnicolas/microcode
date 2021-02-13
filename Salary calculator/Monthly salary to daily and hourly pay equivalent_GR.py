# Python 3.8.5
# Μετατροπή μισθού (40 ωρών εβδομαδιαίας εργασίας) σε ωρομίσθιο και σε ημερομίσθιο.

monthly_salary = float(input("Δώστε ποσό μισθού: "))
hourly_salary = monthly_salary * 0.006
print ("Το ωρομίσθιο είναι", hourly_salary, "ευρώ")
daily_salary_8 = monthly_salary * 0.048
print ("Το ημερομίσθιο 8 ωρών είναι", daily_salary_8, "ευρώ")
daily_salary_6_40 = monthly_salary / 25
print ("Το ημερομίσθιο 6 ωρών και 40 λεπτών είναι", daily_salary_6_40, "ευρώ")
