def count_vowels(text):
    count = 0
    for char in text:
        if char in "aeiouAEIOU":
            count += 1

    return count

lyrics = "Downtown kinaladkad ang QC kami may ari nito Eleven-o-three Hev Abi stupid tindig mo ako nag-imbento Ako may class kahit galing ghetto chicks salbahe ako ang premyo Siya pumoste sa labas humastle ako yung sumweldo yeah aha"

print(count_vowels(lyrics))

