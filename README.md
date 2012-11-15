#### See [related post](https://dubiousdod.org/go/PasswordGenerators) for [some] vulnerability analysis. Peer review is welcome and needed.

## [Loplop](https://duckduckgo.com/?q=!img+loplop) is longer [Oplop](http://code.google.com/p/oplop/)

This is a variation on Oplop, covering the following implementations:
* CLI (Python)
* Android (PY4A)
* Javascript (contributed by [israellevin](https://github.com/israellevin))

It doesn't cover any other [implementations](https://code.google.com/p/oplop/wiki/Implementations) of oplop, doesn't have tests or setup.py, etc. Just the minimum necessary in order to scratch a specific itch.

### Why?

Oplop generates 8-character long passwords. The range is small enough to enable various brute-force attacks (e.g. rainbow tables).

### Difference from oplop

Loplop is *not* backward compatible with oplop (but it *can* be told to work in "legacy mode"):

 * By default, loplop generates 16-character long passwords. 
 * You can prefix the label with `n*` (where `n` is an integer) in order to change the length (e.g. `12*twitter`). 
 * For backward compatible 8 character passwords, you can omit the `n` (i.e. `8`) and write - for example - `*twitter`. 
 * Maximum password length is 22 (the effective length of a 16-byte md5 hash encoded as base64). You can specify a larger `n`, but `23*skidoo` and `666*skidoo` would be equivalent to `22*skidoo`. 
 * If you need to use an ambiguous label (e.g. `*spangled` or `3*cheers`), you'll need to explicitly prefix it with `16*`.

Misc additions to the CLI implementation:

 * The `-p` command line argument pauses and waits for a carriage-return after execution. Used by `glop` (see below).
 * `glop` (i.e. "gnome loplop") opens a gnome-terminal running `loplop -p` (plus any other args you throw at it).
   The password stays in the clipboad until you hit enter (which closes the window and clears the clipboard).
   If you *don't* hit enter, the window will be closed next time you run `glop` (so that you don't end up
   with many "orphan" `glop` windows to close).

### Installation

CLI on Linux: just symlink `glop` and/or `loplop` to a folder in your path (e.g. `~/bin`).

CLI on other platforms: *you* tell *me* :)

SL4A on Android: See the [README](https://github.com/thedod/loplop/tree/master/android#readme).

Javascript: Just run `index.html` in a browser ( preferably on a computer disconnected from the internet ;) ).

## Original Oplop docs

Project home page: http://code.google.com/p/oplop/

What Oplop is: http://code.google.com/p/oplop/wiki/HowItWorks
