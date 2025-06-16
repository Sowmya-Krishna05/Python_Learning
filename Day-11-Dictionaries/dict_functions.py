#: fromkeys() with default values
subjects = ["Math", "English", "Science"]
defaults = dict.fromkeys(subjects, 1)
print(defaults)

# setdefault()
profile = {'name': 'Navya'}
profile.setdefault('city', 'Chennai')
print(profile)
