import praw
import os
import logging

user_agent = os.environ['REDDIT_USER_AGENT']
reddit_username = os.environ['REDDIT_USERNAME']
reddit_password = os.environ['REDDIT_PASSWORD']


def setup_logging():
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()

    FORMAT = "%(asctime)s:%(levelname)s:%(name)s:%(message)s"
    handler.setFormatter(logging.Formatter(fmt=FORMAT))

    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    return logger

logger = setup_logging()

r = praw.Reddit(user_agent=user_agent)
r.login(reddit_username, reddit_password)


def run_bot():
    for comment in praw.helpers.comment_stream(r, 'test'):
        if u'\xaf\\_(\u30c4)_/\xaf' in comment.body:
            comment.refresh()
            logger.info(u"Found a missing arm: {}, {}".format(comment.id, comment.permalink))
            if reddit_username not in [reply.author.name for reply in comment.replies]:
                logger.info(u"Going to leave a comment to: {}, {}".format(comment.id, comment.permalink))
                comment.reply(r"Here, take this \\")
                logger.info(u"Left a comment to: {}, {}".format(comment.id, comment.permalink))

if __name__ == "__main__":
    run_bot()
