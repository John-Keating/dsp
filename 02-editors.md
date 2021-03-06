# Choose and learn your editor(s)


Computing's interface is text. To work effectively, you need to be fluent with this interface.


### Typing

It may sound silly, but [make sure](http://www.typingtest.com/) you know how to type. You should be comfortable typing with perfect accuracy at 60 words per minute, at least. If you currently can't, practice until you can.

A lot of your work will be done in a text editor. You have to know how to use your editor. Any editor will work, but knowing a powerful editor well will make you faster, more comfortable, and more effective.


### Terminal Editor

Sometimes you will need to use a non-graphical text editor. This means an editor that will run entirely inside a terminal window, without spawning a new window, entirely without mouse input.

Make sure that you know at least one of these well enough to do basic editing in a terminal:

 * Emacs
 * vim
 * nano

You should know at least enough vim to be able to get out of it, because it is the default on many systems and you might find yourself in it even if you didn't mean to be.

If you intend to use a graphical editor that doesn't run in a terminal, nano might be a good choice for you because it is very simple.

Both Emacs and vim have built-in interactive tutorials that you can try.

---

What terminal editor will you use? How did you make your decision?

#Vim:
I like the model interface as, after typing in languages with many diacritics, I want to spare my pinkies further strain.
I think that the steep learning curve will pay off in the end with lightning fast slicing and dicing of text. 
I love the simplicity and I am scared of spending too much time customizing an emacs to be 'just right'.

---


### Graphical Editor

You will probably spend most of your time with access to a graphical interface, where you have more choices in editors and integrated development environments.

Popular editors and IDEs include:

 * Emacs
 * vim
 * Sublime
 * Atom
 * Spyder
 * PyCharm

If you choose Emacs or vim, you will have essentially the same editor experience across graphical and non-graphical environments, which is nice. It's also nice to be able to work without ever having to use a mouse. Emacs and vim have somewhat steep learning curves, but they give you the ability to customize your environment quite a lot to make it exactly what you want.

Sublime is probably the most popular editor for new coders. You can set it up to integrate with Python fairly well. Atom is pretty similar to Sublime but has an interesting open architecture and is developed by folks at GitHub.

Spyder and PyCharm are IDEs for Python. They try to give you a fully configured setup out of the box.

We will also use Jupyter (IPython) notebooks, but this does not remove the need for proficiency in an editor or IDE.

---

What graphical editor will you use? How did you make your decision? What are some interesting features of your editor? What are some useful keyboard shortcuts for your editor? How do you customize your editor?

#vim
It has a model interface, which, after many years of word processing, feels both strange and sublime.

Some useful shortcuts include:
  * q{char} start recording a macro q to end recording
  * xp for when I write 'teh'
  * :q! for when I've made a mess and want to start over.
  * :g/pattern/d to delete pattern from the file (remove the d at the end to highlight pattern)
  * :r !date will retrieve the date, time, and timezone from my computer

I have added *vundle* to handle add ons, *powerline* to give me info on the file I am editing, *NERDTree* to display my files, and *pymode*, which everyone says I should get if I want to work in Python. It does a lot :confused: so I haven't quite figured out all of the bundle yet. Still, if it's good enough for some guys on the internet, it should be good enough for me. :stuck_out_tongue_closed_eyes: 
Wed Aug 26 22:07:25 EDT 2015
_Update_ I'm getting the hang of much of it now. Pymode has a good syntax checker. I added *Fugitive* for quick Git actions.

I have altered the default highlighting, indentation, and line length.

---
