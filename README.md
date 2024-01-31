# python_financial_tracker
This is a Monthly Financial Expense Tracker made in Python and using SQL.


<img width="697" alt="Screen Shot 2022-06-15 at 8 07 24 AM" src="https://user-images.githubusercontent.com/68754679/173834394-0440e05b-f6da-4c99-ab85-2c808adb4eac.png">
<img width="1115" alt="Screen Shot 2022-06-15 at 8 14 38 AM" src="https://user-images.githubusercontent.com/68754679/173836262-49c8e48b-01bf-4ff8-b8c3-3c15cf959e0f.png">
<img width="1405" alt="Screen Shot 2022-06-15 at 8 15 16 AM" src="https://user-images.githubusercontent.com/68754679/173836275-d1e40413-32ff-44cf-a636-888311675e3d.png">
<img width="950" alt="Screen Shot 2022-06-15 at 8 16 07 AM" src="https://user-images.githubusercontent.com/68754679/173836280-350d8f21-2547-42da-ab95-e97a71835ab9.png">


# Instructions on How To Run Project on Your Own
1. Download python_financial_tracker repository to your computer
2. Edit the following portion of code so that you can use your own SQL database (lines 18-23):
  ```
  # connecting to database
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="1234password",
      database = "expenses"
    )
```
3. Open your terminal and navigate to where you saved the file in your folders
4. Once inside the directory, run the following command:
   ```python3 main.py
  ```
5. If you get any error about not being able to find the mysql.connector, run the following command:
   ```pip install mysql-connector-python
  ```
6. Then try running the python file again


# Check out Demo Video Below:

https://github.com/eknovoa/python_financial_tracker/assets/68754679/fb42bb8a-9da5-4d88-9c6e-3c25c79cd250


