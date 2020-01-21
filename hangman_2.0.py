import time
import random
import os,sys

def welcome():
    os.system("cls")
    print("\t\t****************************************")
    # print("\t\t!!.....Hangman.....!!")
    print('\t\t\t\x1b[3;30;43m' + '!!.....Hangman.....!!' + '\x1b[0m') 
    print("\t\t****************************************")
    
def correct():
    os.system("cls")
    print("\t\t****************************************")
    print("\t\t\t\x1b[3;30;43m" + "!!.....Hangman.....!!" + "\x1b[0m")
    print("\t\t****************************************")
    string = '\n\tCorrect..!!!'
    for c in string + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.1)


movies = {
    'shrek': 'In the story, an ____ finds his swamp overrun by fairy tale creatures who have been banished by the corrupt Lord aspiring to be king.',
    'inside_out': 'It is a film about an 11 year old girl named ____ who moves across the country from Minnesota to San Francisco with her parents. Riley experiences a transformation in her mind and in who she is as a person as she tries to adjust to her new life in San Francisco and to the difficult process of growing up.',
    'minions': "Evolving from single-celled yellow organisms at the dawn of time, they live to serve, but find themselves working for a continual series of unsuccessful masters, from T. Rex to Napoleon. Without a master to grovel for, They fall into a deep depression. But ____, has a plan; accompanied by his pals ____ and ____, ____ sets forth to find a new evil boss for his brethren to follow. Their search leads them to Scarlet Overkill, the world's first-ever super-villainess.",
    'brave': 'Set in Scotland in a rugged and mythical time, this movie features Princess _____, an aspiring archer and impetuous daughter of ____. She makes a reckless choice that unleashes unintended peril and forces her to spring into action to set things right',
    'big_hero_6': 'The special bond that develops between plus-sized inflatable robot _____, and prodigy ____ ____, who team up with a group of friends to form a band of high-tech heroes.',
    'wall_e': 'He is the last _____ left on Earth. He spends his days tidying up the planet, one piece of garbage at a time.',
    'ratatouille': "He dreams of becoming a great French chef despite his family's wishes and the obvious problem of being a ___ in a decidedly rodent-phobic profession. When fate places him in the sewers of Paris, he finds himself ideally situated beneath a restaurant made famous by his culinary hero.",
    'monsters_university': 'the story of two monsters, ____ and ____, and their time studying at college, where they start off as rivals, but slowly become best friends.',
    'how_to_train_your_dragon': 'In a world with ______, this movie takes place on the island of Berk. _____, son of Stoik, wants to be a ______ killer like his dad, but his dad refuses. One night on an invasion of the ______, He catches a ____ ____, the rarest and an unseen _____ of them all to prove to his father he is worthy.'
    }

movie = random.choice(list(movies.keys()))
print(movie)


count = 3

while(count != 0):
    welcome()
    if count != 3:
        print("\n\nTry again..!!\n\n")
    print("Life: ",count)
    print("Movie Description:\n")
    print(movies[movie])
    choice = input("\nEnter your answer: ").lower().replace(" ","_")
    if choice == movie:
        answer = True
        correct()
        break
    else:
        answer = False
        count -= 1

exit_ = input("\n\nEnter to exit")