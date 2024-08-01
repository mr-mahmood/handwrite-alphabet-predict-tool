from front import gui
# My own codes import
import directory
   
def persian_alphabet():
    address = directory.add()
    info = {}
    info['name'] = 'persian_alphabet'
    info['h5'] = address + directory.hand_write_persian_alphabet
    a = gui(info)
    a.start()


if __name__ == '__main__':
    persian_alphabet()