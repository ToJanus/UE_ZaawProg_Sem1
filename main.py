import argparse

from utils.utils import run

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Uruchom skrypt bez argumentów, aby uruchomić wszystkie obrazy'
                                                 'z katalogu images lub wpisz argument --obraz i ścieżkę do obrazu.')
    parser.add_argument('--obraz', default=None, help='Ścieżka do pojednyczego obrazu')
    args = parser.parse_args()

    if args.obraz == None:
        run()
    else:
        run(args.obraz)
