import argparse
import random
from tqdm import tqdm


def read_words(filepath):
    with open(filepath, 'r', encoding='utf-8') as fin:
        return [l.strip() for l in fin.readlines()]


def generate_title(adjectives, nouns, verbs):
    return random.choice(adjectives) + ' ' + random.choice(nouns) + ' ' + random.choice(verbs) + 's'


def generate_iswc():
    return 'T' + ''.join([str(random.randint(0, 9)) for _ in range(11)])


def generate_work_with_duplicates(adjectives, nouns, verbs, contributors):
    n_duplicates = random.randint(1, 10)
    result = []
    title = generate_title(adjectives, nouns, verbs)
    iswc = generate_iswc()
    work_contributors = list(set(random.choices(contributors, k=random.randint(1, 10))))
    for _ in range(n_duplicates):
        record_contruibutors = set(random.choices(work_contributors, k=random.randint(1, len(work_contributors))))
        record_iswc = iswc
        if random.random() > 0.5:
            record_iswc = ''
        result.append((title, '|'.join(record_contruibutors), record_iswc))
    return set(result)


def generate_contributors(N):
    boy_names = read_words('words_lists/boy_names.txt')
    girl_names = read_words('words_lists/girl_names.txt')
    surnames = read_words('words_lists/surnames.txt')
    result = []
    for _ in range(N):
        if random.random() > 0.5:
            names = boy_names
        else:
            names = girl_names
        name = random.choices(names, k=2)
        surname = random.choice(surnames)
        result.append(' '.join([name[0], name[1], surname]))
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generates works metadata")
    parser.add_argument("-n", type=int, help="Number of works to generate")
    parser.add_argument("-s", '--shuffle', action='store_true', help="If results should be shuffled")
    parser.add_argument("output", help="out file")

    args = parser.parse_args()
    N = args.n
    filepath = args.output
    shuffling = args.shuffle

    adjectives = read_words('words_lists/words_adj.txt')
    nouns = read_words('words_lists/words_noun.txt')
    verbs = read_words('words_lists/words_verbs.txt')
    contributors = generate_contributors(max(1, N // 5))

    result = []
    with tqdm(total=N) as pbar:
        while len(result) < N:
            work = generate_work_with_duplicates(adjectives, nouns, verbs, contributors)
            result += work
            pbar.update(len(work))
    result = result[:N]
    if shuffling:
        random.shuffle(result)
    with open(filepath, 'w', encoding='utf-8') as fout:
        print('title', 'contributors', 'iswc', sep=',', file=fout)
        for line in result:
            print(*line, sep=',', file=fout)
