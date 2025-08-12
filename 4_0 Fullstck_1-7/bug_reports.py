bug_reports = ["Ошибка 1 — High", "Ошибка 2 — Low", "Ошибка 3 — High", "Ошибка 4 — Medium", "Ошибка 5 — Medium",
               "Ошибка 33 — Low"]
print(bug_reports)
a = input('Какой баг добавить ? ')
bug_reports.append(a)
print(bug_reports)
bug_reports.sort()
print(bug_reports)
x = input('Какой баг удалить ? (может Low): ')
bug_reports = [r for r in bug_reports if x not in r]
print(bug_reports)
