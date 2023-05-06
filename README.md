# Mafia-Dating-Sim
A silly little Ren'py game about some OCs.

## GAME HELP
All game files are in the `game` directory.

All dialogue is in .rpy files whose names start with `script`. `script.rpy` lays out the overall structure and jumps between other files as scene transitions occur.

All other .rpy files (whose names do NOT start with `script`) control technical aspects of setting up and running the game.

Images are under the `images` directory and audio is under `audio`.

### All the coding you need to know:
Ren'py makes coding dialogue extremely simple. The basics will look like the following:

```
"Character ID" "dialogue"
```

Where the `Character ID` is optional and can be either one of our pre-existing ones or a string of your choosing, and the `dialogue` is whatever you will have the character say. All existing character IDs can be found at the bottom of `definitions.rpy`.

An example snippet of dialogue follows:

```
"You begin to lead the suspects out of the comando stazione."
"Carabiniere" "Where do you think you're taking these prisoners?"
a "To the bar. For a night of chill relaxation. Criminals needs that too, you know?"
```

The first line will be narration, the second line will be said by a character called Carabiniere, and the third line will be said by Angiolo.

To do anything more complicated, Ren'py documentation can be found [here](https://www.renpy.org/doc/html/); but if you're only writing dialogue, you shouldn't need to touch that at all if you don't want to.

## EDITING AND ACCESS
If you have a GitHub account, I will add it to the repository. (GitHub isn't scary, I promise). You can edit directly through GitHub, but using an IDE could prove helpful (it will improve readability by color-coding keywords and will catch typoes and bugs). The most convenient option is an online IDE like the web editor -- to access it, simply press the full stop `.` key on your keyboard when you are on any page in the GitHub repository. You will be able to easily navigate between different files from within the web editor.

### Compiling, committing and pushing:
Once you have reached a point where you would like to save your edits to the repository, you will need to commit your changes and push the code.

When working directly through GitHub, you will find the option to commit at the bottom of the page; in the web editor, you will need to go to the left-hand sidebar and navigate to `Source Control` (beneath the `Search` button). In both environments, there will be a field to add a commit message; the message can be anything (it can even be left blank, and GitHub will automate a message for you), but its intention is to briefly describe the work you have done on the code. Once you are ready, hit `Commit changes` when working directly through GitHub or `Commit & Push` when working in the web editor.

That's it! You can visit the GitHub page to make sure that your edits have gone through if you are unsure. You will need to refresh; it may take a few minutes to appear.

Shoot me a message for any troubleshooting or debugging issues.

## RUNNING THE GAME
For the time being, if you want to run it, you have two options. The first one is to ask me to figure out how to get it packaged in a nice, usable format to send over. The second is to clone this repo to your machine and install Ren'py, which will act as a launcher.

### Second option:
The easiest way to clone this repo onto a Windows machine will be to navigate up to the green `<> Code` button on the GitHub page and hit `Download ZIP`. Extract the files.

Go [here](https://www.renpy.org/latest.html) to install Ren'py (this will also give you a couple of coding tutorial games which, when you launch it, you will see listed as `Tutorial` and `The Question`).

Launch Ren'py, navigate down to `Preferences`, `General`, and then `Projects Directory:`. Update this to wherever you have the repo files saved.

Hit `Return`, and finally `Refresh`. You should now see `Mafia-Dating-Sim` listed on the sidebar. You can run the game by hitting `Launch Project`.
