ciphertext = "zkrtwvvvnrkulxhoywoj"



rotor = [ "I", "IV", "V", "II" , "III", "VI", "VII" ,"VIII"]

from enigma.machine import EnigmaMachine

def find_rotor_start(ciphertext, a, rotor):
	from enigma.machine import EnigmaMachine
	alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	machine = EnigmaMachine.from_key_sheet(
		rotors=['Gamma' ,'II' ,'IV', rotor],
		reflector='C',
		ring_settings = [3, 5, a, 20],
		plugboard_settings = 'fv cd hu ik es op yl wq jm')
		
	for rotor3 in alphabets:
		start_pos = 'F' + 'J' + rotor3 + 'O'
		machine.set_display(start_pos)
		plaintext = machine.process_text(ciphertext)
		print(plaintext)

for a in range(26):
	for b in rotor:
		find_rotor_start(ciphertext, a, b)