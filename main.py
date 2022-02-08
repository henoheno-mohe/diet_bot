import tweepy
import time
import random
from datetime import datetime

# API KEY
CK = "2HqbmdmClAXl5Rpp4vi7dx4VZ"
CS = "zmtyRn5h32guU58IFrXH1hpbbifOF9uGnHO24EG3fvv2Qtc4JX"
AT = "1489078955772559364-i62ZfP82hdCI0s8gGckU7MNlzW1cNn"
AS = "MWYE19LbMaoqinsrwLk2m1I6Oe79AvfblMfCp3WfCR8KC"
BT = "AAAAAAAAAAAAAAAAAAAAALw%2FYwEAAAAAGfEn2zpaGvBAzt2ORXXyj5BWRKw%3DzN7n7yRYR1KDp7SDI37Zjc3Me3bkB1JJRT7WAa4y8EqfqJ90bw"

#tweepyの設定
client = tweepy.Client(BT, CK, CS, AT, AS)


#２）あるキーワードで検索したユーザを指定の件数フォローする



# today = datetime.date.today()
# print(f'{today:%-m月%-d日}')

time_now = datetime.now()
month = time_now.strftime("%m").lstrip("0")
day = time_now.strftime("%d").lstrip("0")

date = "【" + month + "月" + day + "日" +"】"
# print(date)

weight = 66 - 2 * random.random()
weight_text = "✅体重" + str(round(weight, 1)) + "kg"
bmi = round(weight, 1) / (1.57*1.57)
bmi_text = "✅BMI:"+ str(round(bmi, 1))
# print("✅体重" + str(round(weight, 1)) + "kg")
# print("✅BMI:"+ str(round(bmi, 1)))

text = date + "\n" + weight_text + "\n" + bmi_text + "\n" + "\n" + "#ダイエット垢さんと繋がりたい"
client.create_tweet(text=text)

# 検索キーワード
keyword = "#ダイエット垢さんと繋がりたい -is:retweet"

# フォロー数
follow_cnt = 0

# 現在のフォローリストを作成
follow_list = client.get_users_following(id="1475721163594952706",max_results=100)
follow_lists = []

for follow in follow_list[0]:
    follow_lists.append(follow.id)



s_count = 10
results = client.search_recent_tweets(query=keyword, max_results=s_count, user_fields = "name", expansions=["author_id","referenced_tweets.id"],)

for result in results.data: 
    print(result.author_id)
    # print(result.referenced_tweets)


for result in results.data: 
    client.like(tweet_id=result.id)
#フォローリストにこのツイート主がいなければフォローする。
    if result.author_id not in follow_lists:
        client.follow_user(result.author_id)
        print(result.author_id)
#10秒停止する
        time.sleep(60)
