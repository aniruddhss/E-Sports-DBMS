import pandas as pd
import streamlit as st
import sqlite3
import matplotlib.pyplot as plt

# Connect to SQLite database
def create_connection():
    return sqlite3.connect('eSports_management.db')

def create_tables():
    conn = sqlite3.connect('eSports_management.db')
    cursor = conn.cursor()

    # Create Registration_Details table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Registration_Details (
            Team_Name TEXT,
            Team_Number INTEGER PRIMARY KEY,
            Registration_ID TEXT,
            Team_origin TEXT,
            Team_email TEXT
        )
    ''')

    # Create Team_Details table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Team_Details (
            Team_Number INTEGER PRIMARY KEY,
            Team_Leader TEXT,
            Team_platform TEXT,
            Team_tier INTEGER,
            Team_strength TEXT,
            Tournaments_played INTEGER,
            Tournaments_won INTEGER,
            Team_Experience INTEGER
        )
    ''')

    # Create Platform_Details table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Platform_Details (
            eSport_Name TEXT PRIMARY KEY,
            Match_type TEXT,
            Number_of_teams INTEGER,
            Match_difficulty INTEGER,
            Participation_amount INTEGER,
            Winning_amount INTEGER,
            Tier_required INTEGER
        )
    ''')

    conn.commit()
    conn.close()

# Call the function to create tables
create_tables()

# def insertvalues():
#     conn = sqlite3.connect('eSports_management.db')
#     cursor = conn.cursor()
#
#     # Create Registration_Details table
#     cursor.execute('''
#            INSERT INTO Registration_Details (Team_Name, Team_Number, Registration_ID, Team_origin, Team_email) VALUES
#            ('Alpha Warriors', '001', 'R001', 'USA', 'alpha@warriors.com'),
#            ('Beta Guardians', '002', 'R002', 'Canada', 'beta@guardians.ca'),
#            ('Gamma Legends', '003', 'R003', 'UK', 'gamma@legends.co.uk'),
#            ('Delta Strikers', '004', 'R004', 'Germany', 'delta@strikers.de'),
#            ('Epsilon Knights', '005', 'R005', 'Australia', 'epsilon@knights.au'),
#            ('Zeta Raiders', '006', 'R006', 'India', 'zeta@raiders.in'),
#            ('Eta Spartans', '007', 'R007', 'South Korea', 'eta@spartans.kr'),
#            ('Theta Invincibles', '008', 'R008', 'Brazil', 'theta@invincibles.br'),
#            ('Iota Defenders', '009', 'R009', 'Japan', 'iota@defenders.jp'),
#            ('Kappa Predators', '010', 'R010', 'Russia', 'kappa@predators.ru');
#
#         ''')
#
#     # Create Team_Details table
#     cursor.execute('''
#             INSERT INTO Team_Details (Team_Number, Team_Leader, Team_platform, Team_tier, Team_strength, Tournaments_played, Tournaments_won, Team_Experience) VALUES
#             ('001', 'John Smith', 'PC', 5, 'High', 50, 20, 500),
#             ('002', 'Emily Brown', 'Console', 4, 'Medium', 40, 10, 300),
#             ('003', 'Robert White', 'Mobile', 3, 'Medium', 30, 5, 200),
#             ('004', 'Anna Green', 'PC', 5, 'Very High', 55, 25, 600),
#             ('005', 'Michael Black', 'Console', 2, 'Low', 20, 2, 100),
#             ('006', 'Sophia Blue', 'Mobile', 4, 'Medium', 45, 15, 400),
#             ('007', 'David Silver', 'PC', 5, 'High', 60, 30, 700),
#             ('008', 'James Gold', 'Console', 3, 'Medium', 35, 8, 250),
#             ('009', 'Mia Red', 'Mobile', 2, 'Low', 25, 3, 150),
#             ('010', 'Lucas Bronze', 'PC', 4, 'Medium-High', 50, 18, 550);
#
#         ''')
#
#     # Create Platform_Details table
#     cursor.execute('''
#             INSERT INTO Platform_Details (eSport_Name, Match_type, Number_of_teams, Match_difficulty, Participation_amount, Winning_amount, Tier_required) VALUES
#             ('League of Legends', '5v5', 16, 8, 200, 1000, 4),
#             ('Dota 2', '5v5', 20, 9, 300, 2000, 5),
#             ('Fortnite', 'Solo', 100, 6, 50, 500, 2),
#             ('PUBG Mobile', 'Squad', 25, 7, 100, 800, 3),
#             ('Call of Duty', '4v4', 32, 8, 150, 1000, 4),
#             ('Overwatch', '6v6', 12, 9, 250, 1500, 5),
#             ('CS:GO', '5v5', 16, 8, 200, 1200, 4),
#             ('Valorant', '5v5', 24, 7, 180, 900, 3),
#             ('Rocket League', '3v3', 8, 5, 100, 600, 2),
#             ('Apex Legends', 'Trio', 20, 7, 150, 1000, 3);
#
#         ''')
#
#     conn.commit()
#     conn.close()
#
# insertvalues() #calling this function to insert the sample initial values directly from the code/ you can comment this out to access the funcionality directly from the software after executing only once


# Function to get table columns
def get_table_columns(table_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [col[1] for col in cursor.fetchall()]
    conn.close()
    return columns

# Function to view all data
def view_all_data(table_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    # Define the column names
    columns=get_table_columns(table_name)

    # Convert the data to a DataFrame
    df = pd.DataFrame(rows, columns=columns)

    # Display the DataFrame using Streamlit
    st.write("View All Records")
    st.dataframe(df)
    conn.close()
    return df

# CRUD operations for Registration_Details
def add_registration_details(team_name, team_number, registration_id, team_origin, team_email):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Registration_Details (Team_Name, Team_Number, Registration_ID, Team_origin, Team_email) VALUES (?,?,?,?,?)",
                   (team_name, team_number, registration_id, team_origin, team_email))
    conn.commit()
    conn.close()

def delete_registration_details(team_number):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Registration_Details WHERE Team_Number = ?", (team_number,))
    conn.commit()
    conn.close()

def update_registration_details(team_number, team_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Registration_Details SET Team_Name = ? WHERE Team_Number = ?", (team_name, team_number))
    conn.commit()
    conn.close()

# CRUD operations for Team_Details
def add_team_details(team_number, team_leader, team_platform, team_tier, team_strength, tournaments_played, tournaments_won, team_experience):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Team_Details (Team_Number, Team_Leader, Team_platform, Team_tier, Team_strength, Tournaments_played, Tournaments_won, Team_Experience) VALUES (?,?,?,?,?,?,?,?)",
                   (team_number, team_leader, team_platform, team_tier, team_strength, tournaments_played, tournaments_won, team_experience))
    conn.commit()
    conn.close()

def delete_team_details(team_number):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Team_Details WHERE Team_Number = ?", (team_number,))
    conn.commit()
    conn.close()

def update_team_details(team_number, team_leader):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Team_Details SET Team_Leader = ? WHERE Team_Number = ?", (team_leader, team_number))
    conn.commit()
    conn.close()

# CRUD operations for Platform_Details
def add_platform_details(esport_name, match_type, number_of_teams, match_difficulty, participation_amount, winning_amount, tier_required):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Platform_Details (eSport_Name, Match_type, Number_of_teams, Match_difficulty, Participation_amount, Winning_amount, Tier_required) VALUES (?,?,?,?,?,?,?)",
                   (esport_name, match_type, number_of_teams, match_difficulty, participation_amount, winning_amount, tier_required))
    conn.commit()
    conn.close()

def delete_platform_details(esport_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Platform_Details WHERE eSport_Name = ?", (esport_name,))
    conn.commit()
    conn.close()

def update_platform_details(esport_name, number_of_teams):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Platform_Details SET Number_of_teams = ? WHERE eSport_Name = ?", (number_of_teams, esport_name))
    conn.commit()
    conn.close()


def fetch_table_names():
    conn = sqlite3.connect('eSports_management.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    conn.close()
    return [table[0] for table in tables]


# Function to fetch all records from a specified table
def fetch_records(table_name):
    conn = sqlite3.connect('eSports_management.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    # Fetch column names
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [info[1] for info in cursor.fetchall()]

    df = pd.DataFrame(rows, columns=columns)
    conn.close()
    return df
# Function to fetch records from all tables
def fetch_all_records():
    records = {}
    tables = fetch_table_names()  # Fetch all table names
    for table in tables:
        records[table] = fetch_records(table)  # Store records from each table
    return records


# Function to display registration records from a selected table
def view_all_records(selected_table):
    st.write(f"View All Records from {selected_table}")
    df = fetch_records(selected_table)
    st.dataframe(df)


# Function to display graphs for a selected table
def view_graphs():

    st.write("Select Graph Type:")

    # Dropdown menu to select the graph type
    graph_type = st.selectbox(
        "Choose Graph Type",
        [
            "Teams vs Team Origin (Country)",
            # "Teams vs Team Platform",
            # "Teams vs Team Tier",
            "Teams vs Team Experience",
            # "Match Type vs Difficulty",
            # "Match Type vs Number of Teams"
        ]
    )

    records = fetch_all_records()
    # Fetch data for all tables

    # Plot graphs based on selection
    if graph_type == "Teams vs Team Origin (Country)":
        plot_team_origin(records['Registration_Details'])
    # elif graph_type == "Teams vs Team Platform":
    #     plot_team_platform(records['Team_Details'])
    # elif graph_type == "Teams vs Team Tier":
    #     plot_team_tier(records['Team_Details'])
    elif graph_type == "Teams vs Team Experience":
        plot_team_experience(records['Team_Details'])
    # elif graph_type == "Match Type vs Difficulty":
    #     plot_match_difficulty(records['Platform_Details'])
    # elif graph_type == "Match Type vs Number of Teams":
    #     plot_match_teams(records['Platform_Details'])


# Functions to plot different graphs using matplotlib
def plot_team_origin(df):

    plt.figure(figsize=(10, 5))
    df['Team_origin'].value_counts().plot(kind='bar')
    plt.title('Teams vs Team Origin (Country)')
    plt.xlabel('Country')
    plt.ylabel('Number of Teams')
    st.pyplot(plt)


# def plot_team_platform(df):
#     plt.figure(figsize=(10, 5))
#     df['Team_Platform'].value_counts().plot(kind='bar')
#     plt.title('Teams vs Team Platform')
#     plt.xlabel('Platform')
#     plt.ylabel('Number of Teams')
#     st.pyplot(plt)


# def plot_team_tier(df):
#     plt.figure(figsize=(10, 5))
#     df['Team_Tier'].value_counts().plot(kind='bar')
#     plt.title('Teams vs Team Tier')
#     plt.xlabel('Tier')
#     plt.ylabel('Number of Teams')
#     st.pyplot(plt)


def plot_team_experience(df):
    plt.figure(figsize=(10, 5))
    df['Team_Experience'].value_counts().plot(kind='bar')
    plt.title('Teams vs Team Experience')
    plt.xlabel('Experience Level')
    plt.ylabel('Number of Teams')
    st.pyplot(plt)


# def plot_match_difficulty(df):
#     plt.figure(figsize=(10, 5))
#     df['Match_Difficulty'].value_counts().plot(kind='bar')
#     plt.title('Match Type vs Difficulty')
#     plt.xlabel('Difficulty Level')
#     plt.ylabel('Number of Matches')
#     st.pyplot(plt)


# def plot_match_teams(df):
#     plt.figure(figsize=(10, 5))
#     df['Match_Type'].value_counts().plot(kind='bar')
#     plt.title('Match Type vs Number of Teams')
#     plt.xlabel('Match Type')
#     plt.ylabel('Number of Teams')
#     st.pyplot(plt)

# Streamlit App
def main():
    st.markdown(
            """
            <style>
            .main .block-container {
                padding-top: 2rem;
                padding-right: 3rem;
                padding-left: 3rem;
                padding-bottom: 5rem;
                max-width: 100%;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    st.title("E-Sports DataBase Management Dashboard")

    # Sidebar for navigation
    menu = ["Registration Details", "Team Details", "Platform Details","View Graphs"]
    choice = st.sidebar.selectbox("Select", menu)

    if choice == "Registration Details":
        st.subheader("Manage Registration Details")

        action = st.selectbox("Choose Action", ["Add Record", "View All Records", "Update Record", "Delete Record"])

        if action == "Add Record":
            st.subheader("Add New Registration Record")
            team_name = st.text_input("Team Name")
            team_number = st.text_input("Team Number")
            registration_id = st.text_input("Registration ID")
            team_origin = st.text_input("Team Origin")
            team_email = st.text_input("Team Email")

            if st.button("Add Record"):
                add_registration_details(team_name, team_number, registration_id, team_origin, team_email)
                st.success("Record added successfully")

        elif action == "View All Records":
            st.subheader("View All Registration Records")
            view_all_data("Registration_Details")


        elif action == "Update Record":
            st.subheader("Update Registration Record")
            team_number = st.text_input("Enter Team Number to Update")
            team_name = st.text_input("Enter New Team Name")

            if st.button("Update Record"):
                update_registration_details(team_number, team_name)
                st.success(f"Record with Team Number {team_number} updated successfully")

        elif action == "Delete Record":
            st.subheader("Delete Registration Record")
            team_number = st.text_input("Enter Team Number to Delete")

            if st.button("Delete Record"):
                delete_registration_details(team_number)
                st.success(f"Record with Team Number {team_number} deleted successfully")

    elif choice == "Team Details":
        st.subheader("Manage Team Details")

        action = st.selectbox("Choose Action", ["Add Record", "View All Records", "Update Record", "Delete Record"])

        if action == "Add Record":
            st.subheader("Add New Team Record")
            team_number = st.text_input("Team Number")
            team_leader = st.text_input("Team Leader")
            team_platform = st.text_input("Team Platform")
            team_tier = st.number_input("Team Tier", min_value=0)
            team_strength = st.text_input("Team Strength")
            tournaments_played = st.number_input("Tournaments Played", min_value=0)
            tournaments_won = st.number_input("Tournaments Won", min_value=0)
            team_experience = st.number_input("Team Experience", min_value=0)

            if st.button("Add Record"):
                add_team_details(team_number, team_leader, team_platform, team_tier, team_strength, tournaments_played, tournaments_won, team_experience)
                st.success("Record added successfully")

        elif action == "View All Records":
            view_all_data("Team_Details")
            # columns = get_table_columns("table_name")
            # st.write(f"Columns: {columns}")
            # st.write(records)

        elif action == "Update Record":
            st.subheader("Update Team Record")
            team_number = st.text_input("Enter Team Number to Update")
            team_leader = st.text_input("Enter New Team Leader")

            if st.button("Update Record"):
                update_team_details(team_number, team_leader)
                st.success(f"Record with Team Number {team_number} updated successfully")

        elif action == "Delete Record":
            st.subheader("Delete Team Record")
            team_number = st.text_input("Enter Team Number to Delete")

            if st.button("Delete Record"):
                delete_team_details(team_number)
                st.success(f"Record with Team Number {team_number} deleted successfully")

    elif choice == "Platform Details":
        st.subheader("Manage Platform Details")

        action = st.selectbox("Choose Action", ["Add Record", "View All Records", "Update Record", "Delete Record"])

        if action == "Add Record":
            st.subheader("Add New Platform Record")
            esport_name = st.text_input("eSport Name")
            match_type = st.text_input("Match Type")
            number_of_teams = st.number_input("Number of Teams", min_value=0)
            match_difficulty = st.number_input("Match Difficulty", min_value=0)
            participation_amount = st.number_input("Participation Amount", min_value=0)
            winning_amount = st.number_input("Winning Amount", min_value=0)
            tier_required = st.number_input("Tier Required", min_value=0)

            if st.button("Add Record"):
                add_platform_details(esport_name, match_type, number_of_teams, match_difficulty, participation_amount, winning_amount, tier_required)
                st.success("Record added successfully")

        elif action == "View All Records":
            st.subheader("View All Platform Records")
            view_all_data("Platform_Details")

        elif action == "Update Record":
            st.subheader("Update Platform Record")
            esport_name = st.text_input("Enter eSport Name to Update")
            number_of_teams = st.number_input("Enter New Number of Teams", min_value=0)

            if st.button("Update Record"):
                update_platform_details(esport_name, number_of_teams)
                st.success(f"Record for {esport_name} updated successfully")

        elif action == "Delete Record":
            st.subheader("Delete Platform Record")
            esport_name = st.text_input("Enter eSport Name to Delete")

            if st.button("Delete Record"):
                delete_platform_details(esport_name)
                st.success(f"Record for {esport_name} deleted successfully")
    elif choice == "View Graphs":
        st.subheader("View Graphs")
        view_graphs()
if __name__ == "__main__":
    main()
