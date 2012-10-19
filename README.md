## [Loplop](https://duckduckgo.com/?q=!img+loplop) is longer [Oplop](http://code.google.com/p/oplop/)

This is a variation on the CLI implementation of oplop.

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

Misc additions:

 * The `-p` command line argument pauses and waits for a carriage-return after execution. Used by `glop` (see below).
 * `glop` (i.e. "gnome loplop") opens a gnome-terminal running `loplop -p` (plus any other args you throw at it).
   The password stays in the clipboad until you hit enter (which closes the window and clears the clipboard).
   If you *Don't* hit enter, the window will be closed next time you run `glop` (so that you don't end up
   with many "orphan" `glop` windows to close.

### "Installation"

Linux: Just symlink `glop` and/or `oplop` to a folder in your path (e.g. `~/bin`).

Other platforms: *you* tell *me* :)

## Original Oplop README

### CLI (Command Line Interface) and reference implementation of Oplop

Using a single master password and various nicknames, one can create an
infinite number of unique account passwords. These unique account passwords are
commonly called password hashes, domain-specific passwords, or per-site
passwords.

The CLI implementation of Oplop is only one of many implementations. See the
[project home page](http://code.google.com/p/oplop/) for the complete list
of available implementations of Oplop.


#### General

Project home page: http://code.google.com/p/oplop/

What Oplop is: http://code.google.com/p/oplop/wiki/HowItWorks


#### CLI-specific

Release Notes: http://code.google.com/p/oplop/wiki/CLIReleaseNotes

Instructions: http://code.google.com/p/oplop/wiki/CLIInstructions
