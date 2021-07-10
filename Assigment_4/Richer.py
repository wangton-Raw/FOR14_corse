richter = 7.1
"""
if richter >= 8.0:
    print("Most structures fall")
else:
    if richter >= 7.0:
        print("Many buildings destroyed")
    else:
        if richter >= 6.0:
            print("Many buildings considerably damaged, some collapse")
        else:
            if richter >= 4.5:
                print("Damage to poorly constructed buildings")
            else:
                print("No destruction of buildings")
"""
"""
if richter >= 8.0:
    print("Most structures fall")
elif richter >= 7.0:
    print("Many buildings destroyed")
elif richter >= 6.0:
    print("Many buildings considerably damaged, some collapse")
elif richter >= 4.5:
    print("Damage to poorly constructed buildings")
else:
    print("No destruction of buildings")

if richter >= 4.5:
    print("Damage to poorly constructed buildings")
elif richter >= 6.0:
    print("Many buildings considerably damaged, some collapse")
elif richter >= 7.0:
    print("Many buildings destroyed")
elif richter >= 8.0:
    print("Most structures fall")
else:
    print("No destruction of buildings")
"""
if richter >= 8.0:
    print("Most structures fall")
if richter >= 7.0:
    print("Many buildings destroyed")
if richter >= 6.0:
    print("Many buildings considerably damaged, some collapse")
elif richter >= 5.0:
    print("Many buildings considerably damaged, some collapse, hei")
if richter >= 4.5:
    print("Damage to poorly constructed buildings")
else:
    print("No destruction of buildings")