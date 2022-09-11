import argparse

def parse_args():
    parser = argparse.ArgumentParser(prog='argparse_template.py', description='Tutorial') 
    parser.add_argument('--text', '-t', default='test', type=str, required=False, help='Text for repeated')
    parser.add_argument('--nums', '-n', default='10', type=int, required=False, help='Repeated times')

    return parser.parse_args()


def main():
    for i in range(args.nums):
        print(i, args.text)


if __name__ == '__main__':
    args = parse_args()
    main()