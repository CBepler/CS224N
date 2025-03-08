# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

import utils
import argparse

argp = argparse.ArgumentParser()
argp.add_argument('eval_corpus_path', help='Path to the evaluation corpus.')
args = argp.parse_args()
num_preds = open(args.eval_corpus_path).read().count('\n')
total, correct = utils.evaluate_places(args.eval_corpus_path, ['London'] * num_preds)
if total > 0:
    print('Correct: {} out of {}: {}%'.format(correct, total, correct/total*100))