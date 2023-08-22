from re import*
tweets="What a game , hats @ off to both teams . Well done @benstokes38 @patcummins30 you have bought test cricket back to life. Love test cricket  @TheBarmyArmy @CricketAus @ECB_cricket"
word=tweets.split(" ")
rule="[@][a-zA-Z1-9]+"  #+ indicates atleast
matcher=finditer(rule,tweets)
for m in matcher:
    print(m.group())

