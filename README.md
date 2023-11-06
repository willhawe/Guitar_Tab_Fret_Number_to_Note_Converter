# Guitar Tab Converter
#### Video Demo:  https://youtu.be/24n3SNMPeCA
#### Description:
    My project takes guitar tabs as input in the form of a txt file and outputs a modified version of the file wherein the numbers which represent positions on the guitar fret board have been replaced with letter note values.  As well as this, information is added to the top of the file to tell the user the number of bars in the tab file and weather or not the guitar is in standard tunning.

    The Replace function loads the txt file and stores wach line in a list.  It then loops through each line and replaces the numbers with note values in the form of letters (from A-G with sharps "#" and flats "b"). This function takes three inputs: the filename, a message about weather or not the guitar is in standard tuning and the number of bars.  The later two are printed as messages in the first two lines of the output txt file.

    The IsStandardTuning function determines weather or not the tabs are in the standard (eBGDAE) guitar tuning and feeds the answer into the Replace function.
    The CountBars function counts the instances of "|-" to work out the number of bars in the tabs and feeds this into the Replace function as well.

    The main challange with this project has been ensuring that the code can cope with tabs in carying styles and formats and deal with unique cases. It is a prerequisit that the tabs be in a form similar to thatused on UltimateGuitarTabs.com.

    Another problem was being able to deal with non-standard tuning, i.e. when the strings of the guitar are tuned to notes other than the standard (eBGDAE) I used a dictionary which allowed me to create a sort of map of the guitar fretboard wherein the keys each repressented a fret and the values represented the six strings.