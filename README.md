
# reFreeze

### Markdown web slides served cold

Freeze and thaw Markdown to HTML with
[Remark](https://github.com/gnab/remark) and
[(Frozen)](http://pythonhosted.org/Frozen-Flask/)
[Flask](http://flask.pocoo.org/)
and serve via [GitHub pages](https://pages.github.com/).

- Licensed under a [three clause BSD License](../master/LICENSE)
- Includes some [Remark](https://github.com/gnab/remark) sources (c) Ole Petter Bang
- Includes some [Springy](https://github.com/dhotson/springy) sources (c) Dennis Hotson
- Example project: https://github.com/scisoft/git-intro/
- Example web slides: http://scisoft.github.io/git-intro/

### Do-it-yourself example

Create an empty repository on GitHub e.g. called "example".

Create an empty directory with the same name as the repository
("example") and in this directory copy-paste the following
to a file called `talk.md`:

```
# Title slide

## Your Name

Your affiliation

---

layout: false

## Second slide

- Hey
- Ho
- Lets
- Go

---

## Third slide

- Example equation (with MathJax): $$ a^2 + b^2 = c^2 $$
```

After that follow these steps:

```shell
git init
git add talk.md
echo "venv/" > .gitignore
git add .gitignore
virtualenv venv
source venv/bin/activate
pip install Flask
pip install Frozen-Flask
git submodule add https://github.com/rbast/refreeze.git refreeze
python refreeze/flask_app.py # serve via http://0.0.0.0:5000/
python refreeze/freeze.py    # create static html
git add index.html           # deploy html to github pages
git commit -m "initial commit"
```

Now create a `gh-pages` branch and push the branch to GitHub
(adapt username and repository name):

```shell
git checkout -b gh-pages
git remote add origin git@github.com:you/example.git
git push -u origin gh-pages
```

Few minutes later marvel at http://you.github.io/example/. Yay!

### Serving images

If you want to use images,
put them under `img/` and reference them like this:
```
![]({{ base }}/img/picture.jpg)
```

The directory does not have to be called `img`.
The placeholder `{{ base }}` is replaced by `freeze.py`.

You can resize images like this:
```
<img src="{{ base }}/img/figure.gif" style="width: 400px;"/>
```
