from project import Percolate
import time

start_time = time.time()

parser = Percolate()


if __name__ == '__main__':
    parser.process_entries('data.in')
    parser.jsonify('result.out')

    print time.time() - start_time, 'seconds'
