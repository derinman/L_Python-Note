import inquirer

options = ['python', 'js', 'ts']

questions = [
    inquirer.List('language',
                  message="What is your favorite language?",
                  choices=options,
                  ),
]
answers = inquirer.prompt(questions)

print(answers)
print(answers['language'])