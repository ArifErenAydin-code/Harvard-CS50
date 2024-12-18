# To-Do App
#### Video Demo: [Watch the Demo](https://www.youtube.com/watch?v=Vpa6oQvh6PQ)

#### Description:
This project is a simple **To-Do web application** developed as part of the CS50 course, using **Python Flask** as the backend framework. The primary aim of this project is to provide an efficient and intuitive way for users to manage their daily tasks. It includes features like task creation, editing, completion tracking, and history management.

This application is designed with simplicity and usability in mind, ensuring that users can navigate seamlessly through the platform while keeping track of their tasks and productivity.

### Features:
1. **User Authentication:**
   - Users can securely **register** and **log in** to access their tasks.
   - Passwords are stored as hashed values for added security, ensuring that user credentials are protected.

2. **Task Management:**
   - Users can **add** new tasks by providing a task description and a due date.
   - Tasks can be **edited** if any details need to be updated.
   - Tasks can be **deleted** if they are no longer required.
   - Users can **check off** tasks once they are completed.

3. **Task History:**
   - Completed tasks are moved to a **History** section, allowing users to review their past activities.
   - This feature helps users track progress and maintain a record of completed tasks.

4. **Simple and Intuitive Navigation:**
   - The app is divided into three primary pages for ease of use:
     - **Tasks Page**: Displays all active tasks, along with their descriptions and due dates. Users can check, edit, or delete tasks here.
     - **Add Task Page**: Allows users to add new tasks by entering a description and selecting a date.
     - **History Page**: Displays a list of completed tasks for reference and review.

### Technologies Used:
The application utilizes a combination of technologies to deliver a responsive and functional user experience:
- **Python Flask**: Used as the backend framework to handle routing, user authentication, and data management.
- **HTML**: Provides the structure for the user interface.
- **CSS**: Adds styling to enhance the visual appeal of the application.
- **Bootstrap**: Ensures responsive design and makes the app look clean and modern across devices.
- **SQLite**: A lightweight and efficient database to store user information and tasks.
- **Jinja Templates**: Used in Flask for dynamic content rendering.

### Setup Instructions:
Follow these steps to set up the project locally:
1. Clone this repository to your local machine:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd todo-app
   ```
3. Install the required dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```
4. Set the environment variables (if required for Flask):
   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   ```
5. Run the Flask application:
   ```bash
   flask run
   ```
6. Open your web browser and visit `http://127.0.0.1:5000` to access the app.

### How to Use:
1. **Register for an Account:**
   - Visit the registration page and sign up with a username and password.
2. **Log In:**
   - Use your credentials to log in to the application.
3. **Manage Tasks:**
   - Go to the **Tasks** page to view, check, edit, or delete your tasks.
4. **Add New Tasks:**
   - Use the **Add Task** page to create new tasks with descriptions and due dates.
5. **Review Completed Tasks:**
   - Completed tasks are automatically moved to the **History** page, where you can review your progress.

### Future Improvements:
While the current version of the app is fully functional, there are several features that can be added in future updates:
- **Search Functionality**: Allow users to search for specific tasks.
- **Notifications**: Send reminders for tasks nearing their due dates.
- **Task Prioritization**: Enable users to set priorities for their tasks.
- **Improved UI/UX**: Add animations and better styling for an enhanced user experience.
- **User Settings**: Allow users to customize their profiles and preferences.

### Why I Built This Project:
The goal of this project was to apply the concepts I learned in the **CS50 course** and to develop a fully functional web application. This To-Do app demonstrates my understanding of web development, user authentication, and database management. I also wanted to create a practical tool that can help users improve their productivity by efficiently managing their tasks.

---
Thank you for checking out my project! If you have any feedback or suggestions, feel free to reach out. I hope this application helps you stay organized and productive!
