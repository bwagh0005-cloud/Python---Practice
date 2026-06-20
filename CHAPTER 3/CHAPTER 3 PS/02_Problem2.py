# write the python program to fill a letter template gives below with and date.
letter = '''
       DEAR <|BUDDHABHUSHAN|
       YOU ARE QUALIFIED  TO GRE EXAM !
       <|DATE|>

'''
print(letter.replace("<|BUDDHABHUSHAN|>","WAGH").replace("<|DATE|>","20/06/2024"))
# you can  say this is the chaining