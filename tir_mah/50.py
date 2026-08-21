import matplotlib.pyplot as plt
grades = [18, 9, 19, 20]
passed_count = len([g for g in grades if g >= 10])
failed_count = len([g for g in grades if g < 10])

labels = ['Pass', 'Fail']
sizes = [passed_count, failed_count]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Pass vs Fail')
plt.show()