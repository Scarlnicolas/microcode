# Python 3.8.5
# Μετατροπή μισθού (40 ωρών εβδομαδιαίας εργασίας) σε ωρομίσθιο και σε ημερομίσθιο.

monthly_salary = float(input("Δώστε ποσό μισθού: "))
hourly_salary = monthly_salary * 0.006
print ("Το ωρομίσθιο είναι", round(hourly_salary, 2), "ευρώ")
daily_salary_8 = monthly_salary * 0.048
print ("Το ημερομίσθιο 8 ωρών είναι", round(daily_salary_8, 2), "ευρώ")
daily_salary_6_40 = monthly_salary / 25
print ("Το ημερομίσθιο 6 ωρών και 40 λεπτών είναι", round(daily_salary_6_40, 2), "ευρώ")
