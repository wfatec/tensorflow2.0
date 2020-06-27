import tensorflow as tf
import os

print(tf.__version__)

parent_dir = "/Users/wfatec/workspace_git2/tensorflow-101-master/experts/code_sample/chapter-2/files"
FILE_NAMES = ['cowper.txt', 'derby.txt', 'butler.txt']


def labeler(example, index):
    return example, tf.cast(index, tf.int64)


labeled_data_sets = []

for i, file_name in enumerate(FILE_NAMES):
    lines_dataset = tf.data.TextLineDataset(os.path.join(parent_dir, file_name))
    print(lines_dataset)
    labeled_dataset = lines_dataset.map(lambda ex: labeler(ex, i))
    print(labeled_dataset)
    labeled_data_sets.append(labeled_dataset)

print(labeled_data_sets)

BUFFER_SIZE = 50000
BATCH_SIZE = 64
TAKE_SIZE = 5000

all_labeled_data = labeled_data_sets[0]
for labeled_dataset in labeled_data_sets[1:]:
    all_labeled_data = all_labeled_data.concatenate(labeled_dataset)

print(all_labeled_data)

all_labeled_data = all_labeled_data.shuffle(
    BUFFER_SIZE, reshuffle_each_iteration=False)

print(all_labeled_data)

for ex in all_labeled_data.take(5):
    print(ex)