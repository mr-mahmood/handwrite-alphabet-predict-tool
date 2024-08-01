from front import gui
# My own codes import
import directory

def english_alphabet():
    address = directory.add()
    info = {}
    info['name'] = 'english_alphabet'
    info['h5'] = address + directory.hand_write_English_alphabet
    a = gui(info)
    a.start()

if __name__ == '__main__':
    english_alphabet()