# FilterSeedList readme     

## What is FilterSeedList and what is it intended to be used for

GUrlSearcher is the successor of UrlSearcher.

FilterSeedList is a Python application that:
- takes as input a list of urls and a list of undesired domains
- filter out from the list of urls those belonging to one of the domains contained in the list of undesired domains


## How is the project folder made

The FilterSeedList folder contains the following elements:

1) FilterSeedList.py => the source code of the program
2) FilterSeedList.exe => the Windows executable version of the program
3) seed_input.txt => the list of urls to filter
4) domainsToFilterOut.txt => the list of domains to filter out
5) config.cfg => configuration file
6) how_to_create_EXE.txt => instructions to generate the .exe version of the program
7) icon.ico => the icon of the program
8) README.md => this file
9) LICENSE => copy of the EUPL v1.2 license


## How to execute the program on your PC by using the terminal


If you have Python 3.X already installed on your PC you just have to apply the following instruction points:

1) create a folder on your filesystem (let's say "myDir")

2) copy the content of the project directory into "myDir"

3) customize the parameters inside the config.cfg file :
        
        Change the value of the path related parameters according with the position of the files and folders on your filesystem.

4) open a terminal and go into the myDir directory

5) type and execute the following command:
        python FilterSeedList.py config.cfg

6) at the end of execution you should find inside the "myDir" directory:
		- a txt file called filteredSeed_[dateTime].txt containing the urls that passed the filter
                - a txt file called deletedSeed_[dateTime].txt containing the urls filtered out
		- a log file called FilterSeedList_[dateTime].log


## How to execute the program on your PC by double click the EXE version

If you are using a Windows based operating system, alternatively to using the terminal commands described in the previous section, you can simply double-click on the FilterSeedList.exe executable file icon.

In this case, before running the program by double-clicking, you still need to make sure that:
    - the config.cfg file is present in the same folder as the FilterSeedList.exe file


## Licensing

This software is released under the European Union Public License v. 1.2
A copy of the license is included in the project folder.


## Considerations


This program is still a work in progress so be patient if it is not completely fault tolerant; in any case feel free to contact me (donato.summa@istat.it) if you have any questions or comments.