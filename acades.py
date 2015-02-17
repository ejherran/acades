#!/usr/bin/env python
# -*- coding: utf-8 -*-

import algoritmo.key as key
import algoritmo.des as des
import basico.utils as utils
import basico.numbers as numbers

import sys




def cifrarDES(data, hk):
    
    bk = key.binKey(hk)
    data = utils.stringToBytes(data)
    
    if len(data) < 64:
        data = data + ( '0' * ( 64-len(data) ) )
        
    cif = des.cifrar(data, bk)
    cif = utils.bytesToHex(cif)
    
    return cif




def descifrarDES(data, hk):
    
    bk = key.binKey(hk)
    data = utils.hexToBytes(data)
    
    ori = des.descifrar(data, bk)
    ori = utils.bytesToString(ori)
    
    return ori




def cifrar(path, hk):
    
    if(key.checkKey(hk)):
        
        fichero = open(path, 'r')
        original = fichero.read()
        fichero.close()
        
        adds = numbers.intToHex( 8 - ( len(original) % 8 ) )
        
        if adds == '08':
            adds = '00'
        
        cifrado = []
        
        while len(original) > 0:
            if len(original) >= 8:
                
                cifrado.append( cifrarDES(original[0:8], hk) )
                original = original[8:]
                
            else:
                cifrado.append( cifrarDES( original, hk) )
                original = ''
        
        cifrado = adds + ''.join(cifrado)
        
        fichero = open(path+'.hex', 'w')
        fichero.write(cifrado)
        fichero.close()
        
    else:
        print "\n\tACADES: La DESKEY no es valida!\n"




def descifrar(path, hk):
    
    if(key.checkKey(hk)):
        
        fichero = open(path, 'r')
        cifrado = fichero.read()
        fichero.close()
        
        adds = numbers.hexToInt(cifrado[0:2])
        cifrado = cifrado[2:]
        size = len(cifrado)
        
        if (size % 16 == 0): 
        
            original = []
        
            while len(cifrado) > 0:
                
                    original.append( descifrarDES(cifrado[0:16], hk) )
                    cifrado = cifrado[16:]
            
            original = ''.join(original)
            original = original[0: len(original) - adds]
            
            fichero = open(path+'.txt', 'w')
            fichero.write(original)
            fichero.close()
            
        else:
            print "\n\tACADES: Tamaño de bloque incorrecto, fichero "+path+" corrupto!\n", size
            
    else:
        print "\n\tACADES: La DESKEY no es valida!\n"




def msgUsage():
    
    msg =  "\nUse los siguientes comandos:\n\n"
    msg += "\tpython acades.py -genkey\t\t\t\t#Generar una clave\n"
    msg += "\tpython acades.py -key [DESKEY] -enc [ARCHIVO].txt\t#Cifrar un archivo txt.\n"
    msg += "\tpython acades.py -key [DESKEY] -des [ARCHIVO].hex\t#Descifrar un archivo hex.\n"
    msg += "\nACADES cifra archivos de texto plano (txt) y genera archivos hexadecimales (hex) y descifra en sentido contrario (hex -> txt).\n"
    print msg




def main():
    
    argv = sys.argv
    argc = len(argv)
    
    if(argc == 1):
        msgUsage()
    
    elif argv[1] == '-genkey':
        print '\n\tDESKEY:\t'+key.hexKey(key.genKey())+'\n'
    
    elif argc == 5 and argv[3] == '-enc':
        cifrar(argv[4], argv[2])
    
    elif argc == 5 and argv[3] == '-des':
        descifrar(argv[4], argv[2])
    
    else:
        print "\n\tACADES: Comando incorrecto!\n", argc, argv
    
    return 0

if __name__ == '__main__':
	main()
