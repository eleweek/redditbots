import praw

r = praw.Reddit(user_agent='self posts from a sub by /u/godlikesme')
submissions = r.get_subreddit('all').get_hot(limit=1000)
for submission in submissions:
    if submission.selftext:
        print "Link:", submission.permalink
        print "Title:", submission.title
        print "Score:", submission.score
        print
        print submission.selftext
        print "======================================"
