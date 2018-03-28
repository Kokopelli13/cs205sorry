#code to write save sata to file and load it back

#things to save:
#player: name, position, color, pawn locations, AI setting if computer
#deck: current card, deck order
#current player up


savefile = open("save.txt", "w")
savefile.write("Save files")
savefile.close()
print ("Done")
