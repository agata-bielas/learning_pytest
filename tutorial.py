# int
lesson_number = 1

print(lesson_number, type(lesson_number))

# string

lesson_number = "python tutorial"

print(lesson_number, type(lesson_number))

# list

tweet_lenghts = [130, 89, 20, 920]
print(tweet_lenghts, type(tweet_lenghts))

# tuple

tweet_lenghts_immutable = (120, 30, 84, 200)
print(tweet_lenghts_immutable, type(tweet_lenghts_immutable))

# dict - slownik
tweets_by_user = {
    "John": [1, 14],
    "Mary": [ 2, 3]
}

print(tweets_by_user, type(tweets_by_user))

print(tweets_by_user["John"])

if 'a':
    print("Yes")
else:
    print("No")
