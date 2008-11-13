# Introduction

The IPython Bundle is a collection of commands designed to help you work with IPython form within TextMate. It was started after seeing [UsingIPythonWithTextMate](http://ipython.scipy.org/moin/Cookbook/UsingIPythonWithTextMate "Cookbook/UsingIPythonWithTextMate - IPython"), which contains the core commands on which this bundle is based. Kudos to Barry Wark for writing this page.

Currently all commands are aliases to the shortcut `⌃⇧I` (Shift + Ctrl + I), and will only activate when the scope is `source.python`. The commands `Edit ipythonrc` and `View config directory` are available in all scopes.

# Configuration

If you wish to specify the arguments with which `ipython` is run, you can set `TM_IPYTHON` in TextMate's preferences. I recommend setting this variable to `ipthon -pylab -wthread`.

A simple language grammar for highlighting `ipythonrc` files in also included.
You can switch the language grammar to the `ipythonrc` type by pressing `⌃⌥⇧I` (Shift + Cmd + Alt + I). A bundle command is also available for easy editing of the file (provided it lives under `~/.ipython`).

# Installation

This bundle is best installed using GetBundles. You can also clone it from GitHub, or download a tarball.

To install GetBundles:

1. Open a Terminal
2. Type: `cd; svn co http://svn.textmate.org/trunk/Review/Bundles/GetBundles.tmbundle/`
3. Type: `open GetBundles.tmbundle`

To use GetBundles:

1. Switch to TextMate
2. Start a new document
3. Choose `GetBundles` → `Get Bundles` from the `Bundles` menu.
4. Browse or search the list, select `IPython` and hit `Install Bundles`

# Help, Suggestions or Feature Requests

For help, please use the [Google Group](groups.google.com/group/ipython-tmbundle/), for suggestions, feature requests, bug reports or patches, please post to the [IPython-dev mailing list](http://projects.scipy.org/mailman/listinfo/ipython-dev "IPython-dev Info Page"), please prefix the subject line with `[TextMate]`.

# Useful Links

  * [IPython bundle](http://github.com/mattfoster/ipython-tmbundle) on [GitHub](http://github.com/ "Secure Git hosting and collaborative development &mdash; GitHub")
  * [IPython Home](http://ipython.scipy.org "IPython")
  * [Scipy](http://www.scipy.org/ "SciPy")
  
