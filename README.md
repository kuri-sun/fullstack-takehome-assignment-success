# <span style="font-size: 30px;">Full-stack take-home assignment</span> <img src="https://play-lh.googleusercontent.com/pE4AjuQLjUMzulbNL6fjVX4jMTXAtmO4kwHCEaU_0hfGJBIO3HRQ5alMsHwlAajhBa8=w480-h960-rw" alt="instawork-logo" style="height: 30px; width: 30px; margin-left: 10px;" />

<span style='color: gray;'>This is the assignment for Instawork's Fall Internship 2022 position. <br/>The project is to implement a simple team-member management application that allows the
user to view, edit, add, and delete team members. <br/>
Total how much I spent: 4.5 hours. (+2.5 hours to refine)
</span>

<br />

## Project Requirements

<p><span style='margin-right: 10px;'>✅ </span>Create a public repository on your Github account</p>
<p><span style='margin-right: 10px;'>✅ </span>Implement the spec <a href="#implementaion">below</a> and push it to your repository.</p>
<p><span style='margin-right: 10px;'>✅  </span>Create proper documentation for <a href="#building">building</a> and <a href="#testing">testing</a> the project</p>
<p><span style='margin-right: 10px;'>✅ </span>Add <a href="https://github.com/Taqdeer">Taqdeer</a> or <a href="https://github.com/LiJu21">LiJu21</a> as a collaborator to the github project</p>
<p><span style='margin-right: 10px;'>✅ </span>We may leave some comments on the code with suggestions on how to improve the implementation.</p>
<br/>

## <span id="building">Build application</span>

<p style="margin: 15px 0 10px 0;"><span style='margin-right: 10px;'>✅ </span> You already installed Python 3 or above, and Django as well. If you don't want to install it to globally, check <a href="https://docs.python.org/3/library/venv.html">here</a> to set up virtual evironment.</p>

<p style="margin: 15px 0 10px 0;">1. Make sure you're in base directory first, and Go to project directory</p>

```
cd instawork_homework
```

<p style="margin: 15px 0 10px 0;">2. Start application</p>

```
python manage.py runserver
```

<br/>

## <span id="testing">Testing application</span>

<p style="margin: 15px 0 10px 0;"><span style='margin-right: 10px;'>✅ </span> You already installed Python 3 or above, and Django as well. If you don't want to install it to globally, check <a href="https://docs.python.org/3/library/venv.html">here</a> to set up virtual evironment.</p>

<p style="margin: 15px 0 10px 0;">1. Make sure you're in base directory first, and Go to project directory.</p>

```
cd instawork_homework
```

<p style="margin: 15px 0 10px 0;">2. Run test cases. (Testing for views, urls, forms, models)</p>

```
python manage.py test member
```

<br/>

## <span id="testing">Application overview</span>

<h4 id="implementaion" style="margin: 15px 0 8px 0; font-weight: 500;">About</h4>
I used frontend as HTML, CSS and making those up by Bootstrap4, backend as Django and database as SQLite.
using Django features such as model forms and generic class-based views to minimize the amount of code.

<h4 style="margin: 15px 0 8px 0; font-weight: 500;">Technology</h4>
<ul>
  <li>HTML, CSS</li>
  <li>Django</li>
  <li>SQLite</li>
  <li>Bootstrap4, Font Awesome</li>
</ul>

<h4 style="margin: 15px 0 8px 0; font-weight: 500;">Application Looks</h4>
<img src="https://user-images.githubusercontent.com/62743644/178614362-62b7b3c8-0e9c-4647-8ed7-00708b0f3c55.jpeg" alt="looks"/> <br/>
(Figure.1) Home page <br/><br/>

<img src="https://user-images.githubusercontent.com/62743644/178614267-6e5c5c54-1cce-4f5d-9d11-1830c19a09b1.jpeg" alt="looks"/> <br/>
(Figure.2) Add member page <br/><br/>

<img src="https://user-images.githubusercontent.com/62743644/178614312-59600721-2f4c-401d-9cae-2904f9f10bf5.jpeg" alt="looks"/> <br/>
(Figure.3) Edit member page <br/><br/>
