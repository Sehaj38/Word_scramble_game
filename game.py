import random
import time

def get_words(filename):
    with open(filename, 'r') as file:
        words = [word.strip() for word in file.readlines()]
    return words

def scramble_word(word):
    scrambled = list(word)
    while True:
        random.shuffle(scrambled)
        scrambled_word = ''.join(scrambled)
        if scrambled_word != word:
            return scrambled_word

def play_scramble_game(words_file, total_rounds=5, time_limit=10):
    words = get_words(words_file)
    score = 0

    print("🎉 Welcome to Word Scramble!")
    print(f"You'll be shown {total_rounds} scrambled words.")
    print(f"Unscramble each one within {time_limit} seconds!")
    print("You need to guess at least 4 correctly to win.\n")

    for round_num in range(1, total_rounds + 1):
        word = random.choice(words)
        scrambled = scramble_word(word)

        print(f"🔢 Round {round_num}:")
        print(f"🌀 Scrambled word: {scrambled}")
        start_time = time.time()
        guess = input("Your guess: ").strip().lower()
        end_time = time.time()

        time_taken = end_time - start_time

        if time_taken > time_limit:
            print(f"⏱️ Time's up! You took {int(time_taken)} seconds.")
            print(f"❌ The correct word was: {word}\n")
            continue

        if guess == word:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct word was: {word}")

        print(f"⏲️ You answered in {int(time_taken)} seconds.\n")

    print("🧾 Game Over!")
    print(f"Your Score: {score} / {total_rounds}")

    if score >= 4:
        print("🏆 Congratulations! You won!")
    else:
        print("😢 Better luck next time.")

if __name__ == "__main__":
    play_scramble_game('words.txt')
