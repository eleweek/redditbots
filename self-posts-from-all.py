import praw
import argparse

parser = argparse.ArgumentParser(description='Plot karma distributions of comments in a post')
parser.add_argument('--subreddit', required=True, help='Subreddit name')
parser.add_argument('--submission-limit', type=int, required=True, help='Limit to submission amount')
args = parser.parse_args()


r = praw.Reddit(user_agent='self posts from a sub by /u/godlikesme')
submissions = [s for s in r.get_subreddit(args.subreddit).get_hot(limit=1000) if s.selftext][:args.submission_limit]
for submission in submissions:
    print "Link:", submission.permalink
    print "Title:", submission.title
    print "Score:", submission.score
    print
    print submission.selftext
    print "======================================"
