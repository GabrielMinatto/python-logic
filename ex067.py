words = (
    "aprender",
    "programar",
    "linguagem",
    "python",
    "curso",
    "gratis",
    "estudar",
    "praticar",
    "trabalhar",
    "mercado",
    "programador",
    "futuro",
)

vowels = "aeiou"

for word in words:
    print(f"\nNa palavra {word} temos", end=" ")

    for letter in word:
        if letter in vowels:
            print(letter, end=" ")
