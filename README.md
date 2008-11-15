# Introduction

The IPython Bundle is a collection of commands designed to help you work with IPython form within TextMate. It was started after seeing [UsingIPythonWithTextMate](http://ipython.scipy.org/moin/Cookbook/UsingIPythonWithTextMate "Cookbook/UsingIPythonWithTextMate - IPython"), which contains the core commands on which this bundle is based. Kudos to Barry Wark for writing this page.

Currently all commands are aliases to the shortcut `⌃⇧I` (Shift + Ctrl + I), and will only activate when the scope is `source.python`. The commands `Edit ipythonrc` and `View config directory` are available in all scopes.

Please be aware that this bundle know **nothing** of the state of the running IPython. This means that repeated calls may not have the effect you expected.

Also note that if you have a running IPython instance that you want to be detected, you should switch its tab to front. 

# Configuration

If you wish to specify the arguments with which `ipython` is run, you can set `TM_IPYTHON` in TextMate's preferences. I recommend setting this variable to `ipthon -pylab -wthread`.

A simple language grammar for highlighting `ipythonrc` files in also included.
You can switch the language grammar to the `ipythonrc` type by pressing `⌃⌥⇧I` (Shift + Cmd + Alt + I). A bundle command is also available for easy editing of the file (provided it lives under `~/.ipython`).

# Socket Support

Socket support is very much **work in progress**. 

It is currently possible to connect to the IPYthon vim server extension (`ipy_vimserver`), although support is currently limited to a few test commands. To do this, fire up IPYthon, and enable the server using:

    import ipy_vimserver
    ipy_vimserver.setup('sessionname')

This will create a unix socket in `~/.ipython/` which you can then connect to using the bundle's `Connect to IPYthon server command`.

This command should detect multiple sessions and ask which to connect to. Please note it is not possible to connect to multiple IPYthon servers.

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
  
