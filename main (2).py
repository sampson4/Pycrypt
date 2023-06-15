import PySimpleGUI as sg
#import time

def file_operation(path, key, operation):
    try:
        gin = open(path, 'rb')

        # Opening and reading file 
        file = gin.read()
        gin.close()

        # converting data into byte array to
        # perform encryption easily on numeric data
        file = bytearray(file)

        # performing XOR operation on each value of bytearray
        for index, values in enumerate(file):
            if operation == "encrypt":
                file[index] = values ^ int(key)
            elif operation == "decrypt":
                file[index] = values ^ int(key)

        # opening file for writing purpose
        gin = open(path, 'wb')

        # writing encrypted/decrypted data in file
        gin.write(file)
        gin.close()

        return "Operation Completed..."
    except:
        return "ERROR!!!"


sg.theme("lightPurple")
layout = [
    [sg.Text("SYSTEM DATA ENCAPSULATION AND DECAPSULATION", size=(100,1), justification='center')],
    [sg.In(key="-FILE_PATH-",font=('Arial Bold', 9)), sg.FileBrowse(),sg.In(background_color="white")],
    [sg.Text("Input Key:"),sg.In(size=(10,10), password_char='*',font=('Arial Bold', 9), k="--key--")],
    #k(variable to signify value when clicked)
    [sg.Button("ENCRYPT/DECRYPT", k="--encrypt--")],
    #[sg.Button('Cancel',k="Cancel")],
    [sg.Text(size=(30,1), key="-OUTPUT-")]
]

window = sg.Window('Py-Crpyt', layout, size=(400,150))
counter=0
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    
    if event == "--encrypt--":
        if counter < 6:
            message = file_operation(values["-FILE_PATH-"], values["--key--"], 'encrypt')
            if message == "Py-Crypt Can not encrypt this system file":
                sg.popup(message)
            else:
                window['-OUTPUT-'].update(message)
                counter += 1
        else:
            sg.popup('You have exhausted your encryption/decryption limit.')
    
    
window.Close()
