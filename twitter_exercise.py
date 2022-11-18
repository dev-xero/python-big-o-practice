arr = [
    {
        'tweet': 'hi',
        'date': 2012
    },
    {
        'tweet': 'my',
        'date': 2014
    },
    {
        'tweet': 'teddy',
        'date': 2018
    },
]  # Organized in order of oldest to newest


# Compare the dates of each tweet
# This is in fact an expensive operation as n gets arbitrarily large
# It's time complexity is O(n²)
# Space complexity is O(1)
def compare_dates(l_list: list[dict]):
    i = 0
    while i < len(l_list):  # len() function runs in linear time
        j = 0
        i_date, i_tweet = l_list[i]['date'], l_list[i]['tweet']
        j_date, j_tweet = l_list[j]['date'], l_list[j]['tweet']
        while j < len(l_list):
            if i_date > j_date:
                print(i_tweet, '-', j_tweet, '-', '1st tweet is newer')
            elif i_date == j_date:
                print(i_tweet, '-', j_tweet, '-', 'tweet was made on the same year')
            else:
                print(i_tweet, '-', j_tweet, '-', '1st tweet is older')
            j += 1

        i += 1


compare_dates(arr)
