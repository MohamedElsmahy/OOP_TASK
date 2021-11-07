import random
import webbrowser

webList = ['https://www.google.com', 'https://www.facebook.com', 'https://www.twitter.com', 'https://www.youtube.com']
randomweb = random.choice(webList)
chosenweb = webbrowser.open(randomweb)
# print(chosenweb)