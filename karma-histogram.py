import praw
import praw.helpers
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='Plot karma distributions of comments in a post')
parser.add_argument('--link', dest='link', required=True, help='Link of the post')
parser.add_argument('--expand_more_comments', dest='expand_more_comments', action='store_true', default=False, help='Expand more comments')
args = parser.parse_args()


def plot_karma(karma):
    # the histogram of the data
    n, bins, patches = plt.hist(karma, 100, facecolor='green', alpha=0.75)

    plt.xlabel('Karma')
    plt.ylabel('Post count')
    plt.gca().set_yscale('log')
    plt.grid(True)

    plt.show()


def get_every_comments_karma(r, submission_link, expand_more_comments):
    submission = praw.objects.Submission.from_url(r, submission_link, comment_limit=None)
    if expand_more_comments:
        submission.replace_more_comments(limit=None, threshold=0)
    return [(comment.score if 'score' in dir(comment) else 0) for comment in praw.helpers.flatten_tree(submission.comments)]

r = praw.Reddit(user_agent='karma distribution a sub by /u/godlikesme')
karma = get_every_comments_karma(r, args.link, args.expand_more_comments)
plot_karma(karma)
