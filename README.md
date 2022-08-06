# weird_py_game
I'm just testing out how to make one of these text based games in python

I kind of figured out how to set up the files for new story branches (not to be confused with git branches)
Basically, each new story part is a function that I will call in main
Each story function returns the value that the user chose
In main, I use those values to determine what story part should go next

For drastic changes in the story, like a decision takes the user down a different path, I'll make a new file and put all the related story functions in there

This isn't perfect and can probably lead to a lot of spaghetti code, especially in main with a giant if elif chain
But I guess it'll just have to do for now??
