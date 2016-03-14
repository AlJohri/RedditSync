import os, errno, csv, collections

def mkdir_p(path):
    # os.makedirs(folder, exist_ok=True) # Python 3
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def parse_input():
    adjacency_list = {}
    with open("input.csv", "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            blog_id, subreddit_names = int(row[0]), row[1].split("|")
            adjacency_list[blog_id] = subreddit_names

    reversed_adjacency_list = collections.defaultdict(list)
    for blog_id, subreddit_names in adjacency_list.items():
        for subreddit_name in subreddit_names:
            reversed_adjacency_list[subreddit_name].append(blog_id)

    unique_subreddit_names = list(reversed_adjacency_list.keys())

    return unique_subreddit_names, reversed_adjacency_list
