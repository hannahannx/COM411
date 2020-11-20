#importing output
import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message
import basics.output.escape_characters as escape_characters
import basics.output.asciiArt as asciiArt 
#importing input
import basics.input.ascii_art as ascii_art
import basics.input.data_types as data_types



#importing decisions

#importing functions

#iporting modules

#importing repetitions

def run_block_a():
  print("Which program in 'Block A: Basics' do you wish to run?")
  response = input()
  if (response == "simple_message"):
    simple_message.run()
  elif (response == "multiline_message"):
    multiline_message.run()
  elif (response == "escape_characters"):
    escape_characters.run()
  elif (response == "ascii_art"):
    ascii_art.run()
  elif (response == "asciiArt"):
    asciiArt.run()
  elif (response == 'data_types'):
    data_types.run()
    


def run():
  is_running = True

  while(is_running):
    print("What would you like to do?")
    print("[a] Run 'Block A: Basics' programs")
    print("[b] Run 'Block B: Data' programs ")
    print("[q] Quit")
    response = input()

    if (response == "a"):
      run_block_a()
    elif (response == "q"):
      break
    else:
      print("Invalid option! Please try again.")

run()