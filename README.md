# Mafia Dating Sim
Shot through the heart. Bang. Visual novel about about a carabiniere getting up-close and personal to investigate suspected members of cosa nostra in fantasy Sicily, 1924, during the rise of fascism and anti-mafia government protocals.

<picture>
  <img alt="Header image of Venisian canals" src="https://github.com/1203-Johnson-Ellis/Mafia-Dating-Sim/blob/main/game/images/backgrounds/bg%20venice%20canals.png">
 </picture>

## GAME HELP
All dialogue is contained in .rpy files whose names start with `script`. `script.rpy` lays out the overall structure and jumps between other files as scene transitions occur.

All other .rpy files (whose names do NOT start with `script`) control technical aspects of setting up and running the game, such as displayables and variable definitions.

### Basics of coding dialogue:
In its most simple form, writing a line of dialogue looks like this:

```
"Character ID" "dialogue"
```

Where the `Character ID` is optional and can be either one of our pre-existing ones (found at the bottom of `definitions.rpy`) or a display name of your choosing, and the `dialogue` is whatever you will have the character say.

An example snippet of coded dialogue follows:

```
"You begin to lead the suspects out of the comando stazione."
"Carabiniere" "Where do you think you're taking these prisoners?"
a "To the bar. For a night of chill relaxation. Criminals needs that too, you know?"
```

The first line will be narration, the second line will be said by a character called Carabiniere, and the third line will be said by Angiolo (per the character definitions).

If you want just a little more detail, the [Quickstart guide](https://www.renpy.org/doc/html/quickstart.html#a-simple-game) is a great place to get started writing scenes (it provides simple examples of images, scene transitions, and use of labels and variables). For even more information, see the full [Ren'py documentation](https://www.renpy.org/doc/html/).

## EDITING AND ACCESS
If you have a GitHub account, I will add it to the repository. (GitHub isn't scary, I promise.)

You can edit directly through GitHub by opening the page for any file and hitting `Edit this file`.

Using an IDE could also prove helpful, as it will improve readability by color-coding keywords, make file navigation easier, and will catch typoes and bugs. GitHub has an online IDE, called the web editor, built in. To access it, simply go to any page in the repository and press the full stop `.` key on your keyboard.

### Committing and pushing:
Once you have reached a point where you would like to save your edits to the repository, you will need to commit your changes and push the code.

When working directly through GitHub, you will find the option to commit at the bottom of the page; in the web editor, you will need to go to the left-hand sidebar and navigate to `Source Control` (beneath the `Search` button).

In both environments, there will be a field to add a commit message; the message can be anything (it can even be left blank, and GitHub will automate a message for you), but its intention is to briefly describe the work you have done on the code.

Once you are ready, hit `Commit changes` when working directly through GitHub or `Commit & Push` when working in the web editor. Any changes should now appear in the repository on refreshing.

Shoot me a message for any troubleshooting or debugging issues.

## RUNNING THE GAME

Mafia is now [up on itch.io](https://becquerelian.itch.io/mafia-dating-sim/download/C0DU0g7RUxx915gQr3L65U1S8e8vGAQobVoioK2B) for your convenience! I'll try to keep it relatively up-to-date on there, but for code access, Github is still the place to go.

```
(Don't be shocked if anything is broken, but do let me know so I can check it out.)
```
