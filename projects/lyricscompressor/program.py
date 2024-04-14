from .compressor import Compressor

def run(compressor:Compressor, init:bool=False):
    if init:
        print('Please select an option:'
                +'\n[1] -> Compress lyrics into memory'
                +'\n[2] -> Check disk storage for compressed lyrics'
                +'\n[0] -> Terminate program'
            )
    else:
        print('Welcome back to the main menu!')
        print('Please select an option:'
                +'\n[1] -> Compress new lyrics into memory'
                +'\n[2] -> Check disk storage for compressed lyrics'
                +'\n[3] -> Decompress current lyrics from memory'
                +'\n[4] -> Save current lyrics to disk'
                +'\n[5] -> View word positions in current lyrics'
                +'\n[0] -> Terminate program'
            )
    inp = input()
    match inp:
        case '1':
            input_handle = input('Enter name of the file you want to compress: ')
            try:
                compressor.compress(input_handle)
            except FileNotFoundError:
                print('File not found')
                run(compressor, init)
            print('Lyrics compressed successfully!')
            run(compressor)

        case '2':
            if compressor.has_stored_to_disk:
                print(f'The lyrics to {compressor.disk_storage} is in disk storage')
                print('Wour you like to:' 
                      +'\n [m]ove to memory'
                      +'\n [d]elete from disk'
                      +'\n Go [b]ack to the main menu'
                      )
                option = input()
                match option:
                    case 'm':
                        compressor.pop_storage()
                        print('Lyrics moved to memory!')
                        run(compressor)
                    case 'd':
                        compressor.clear_storage()
                        print('Lyrics deleted from disk!')
                        run(compressor, True)
                    case 'b':
                        run(compressor, True)
                    case _:
                        print('Invalid input. Please try again.')
                        run(compressor, init)
            else:
                print('There are no lyrics stored in disk storage.')
                run(compressor, init)

        case '3':
            output_handle:str = input('Enter the name of the file you want to decompress to: ')
            compressor.decompress(output_handle)
            print('Lyrics decompressed successfully!')
            run(compressor)
        case '4':
            song_name:str = input('Enter the name of the song that is in memory: ')
            compressor.store_long_term(song_name)
            print('Lyrics saved to disk successfully!')
            run(compressor)    
        case '5':
            print(compressor.word_positions())
            run(compressor)
        case '0':
            print('Goodbye!')
        case _:
            print('Invalid input. Please try again.')
            run(compressor,init)

if __name__ == '__main__':
    compressor=Compressor()
    print('Welcome to the Lyrics Compressor!')
    run(compressor,True)
        
    
    
