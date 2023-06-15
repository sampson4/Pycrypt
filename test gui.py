import PySimpleGUI as sg
import time

def file_encryption(path, key, time_limit):	
	# print path of the file and encryption key that
	# we are using
	#print('The path of file : ', path)
    #print('Key for encryption : ', key)
	# open file for reading purpose
	fin = open(path, 'rb')
	

	
	# storing image data in variable "image"
	file = fin.read()
	fin.close()
	
	# converting image into byte array to
	# perform encryption easily on numeric data
	file = bytearray(file)

	# performing XOR operation on each value of bytearray
	for index, values in enumerate(file):
		file[index] = values ^ int(key)

	# opening file for writing purpose
	fin = open(path, 'wb')
	
	# writing encrypted data in image
	fin.write(file)
	fin.close()
	#print('Encryption Done...')






 


sg.theme("DarkGreen4")
layout1 = [[sg.Text("SYSTEM DATA ENCAPSULATION AND DECAPSULATION")],
# take path of the file as a input
[sg.In(key="-FILE_PATH-"), sg.FileBrowse()],
# taking encryption key as input
[sg.Text("Input Encryption Key:"),sg.In(size=(10,10), password_char='*', k="--encryptionKey--")],
[sg.Button("ENCRYPT & DECRYPT", k="--decrypt--")]
#[sg.Button("Decrypt", k="--decrypt--")] sg.Text('Enter file path:'), sg.InputText()],
]

window = sg.Window('file encyption', layout1,size=(400,150))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
	
    if event=="--decrypt--" or event == "--encrypt--":
        file_encryption(values["-FILE_PATH-"], values["--encryptionKey--"])
		


    
window.Close()
