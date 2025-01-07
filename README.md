<h1>Steps to run the project</h1><br>
<h1>Step 1</h1>Create an empty folder<br>
<h1>Step 2</h1><p>Clone this repository in cmd using<br>
<div>
  <button onclick="navigator.clipboard.writeText('git clone https://github.com/manavdevs/dajngo2.git')">Clone</button>
  <pre><code>git clone https://github.com/manavdevs/dajngo2.git</code></pre>
</div><br>
<h1>Step 3</h1>Create a database to store values <br>
<img src="https://github.com/user-attachments/assets/e511c01d-1baf-43e4-ac86-1bb76fcae130"></img>
<br>
<h1>Step 4</h1>Replace the database functionality with your field values in settings of your django project with all required fields such as name of the databse, user, password, host and port<br>
<img src="https://github.com/user-attachments/assets/708b80a4-4342-4a02-aadd-01629b8865c4"></img>
<br>
<h1>Step 5</h1>Change Directory to your project file `cd ecommerce`<br>
<img src="https://github.com/user-attachments/assets/0f5911ed-40d0-4a07-a774-57f6bbcd8405"></img><br>
<h1>Step 5</h1>make all the migrations using the below commands <br>
<div>
  <button onclick="navigator.clipboard.writeText(```'py manage.py makemigrations
                                                 py manage.py migrate'```)">Migrate</button>
  <pre><code>py manage.py makemigrations</code></pre><pre><code>py manage.py migrate</code></pre>
</div><br>
<h1>Step 6</h1>Your schemas(tables) are created <br>
<img src="https://github.com/user-attachments/assets/a17c7061-1d4a-4a78-b855-3cc69c53a35d"></img>
<br>
<h1>Step 7</h1>Run the project using
<button onclick="navigator.clipboard.writeText('python manage.py runserver')">Run Project</button>
  <pre><code>python manage.py runserver</code></pre><br>
<h1>Output Screens</h1>
<h4>Screen 1 Main Page</h4>
<img src="https://github.com/user-attachments/assets/541388c4-e61f-4eda-b584-e4d4c66b2fdd"></img>
<br>
<h4>Screen 2 Products Page</h4>
<img src="https://github.com/user-attachments/assets/cce8eca2-5346-4721-9548-4c1495b5885b"></img>
<br>
<img src="https://github.com/user-attachments/assets/e74e653f-6771-4530-8cd8-b2e6710600ba"></img><br>
<img src="https://github.com/user-attachments/assets/22492046-43bb-4754-8cf3-60b62c2e8947"></img><br>
<h4>Screen 3 Add Page</h4>


<img src="https://github.com/user-attachments/assets/640816f9-8995-4197-9999-08e8f1b5ac38"><br>
Saving will take back to display page while back to list link does not record the data<br>
<h4>Screen 4 Edit Page</h4>
<img src="https://github.com/user-attachments/assets/48a880ed-c4f2-479f-a2d7-1650a3f0ad9a"><br>
Saving will take back to display page while back to list link does not update the data<br>
<h4>Screen 5 Delete Page</h4>
<img src="https://github.com/user-attachments/assets/59ed315e-bbd6-4bc9-8dc8-aac86b9398ba"><br>
Yess will take back to display page with item being deleted while cancel link does affect the data<br>
