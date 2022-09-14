import os

for i in range(365):
    d = str(i) + " days ago"
    with open('text.txt', 'a') as file:
        file.write(d + '\n')
    os.system('git add .')
    os.system('git commit --date="' + d + '" -m "commit"')
os.system('git push')
