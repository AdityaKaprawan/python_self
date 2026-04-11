import pandas as pd
from google.colab import files
files.upload()

FILE = "voting_data.xlsx"

# for loading data 
def load_data():
    voters = pd.read_excel(FILE, sheet_name="Voters")
    candidates = pd.read_excel(FILE, sheet_name="Candidates")
    return voters, candidates

# this is for saving daat
def save_data(voters, candidates):
    with pd.ExcelWriter(FILE, engine="openpyxl", mode="w") as writer:
        voters.to_excel(writer, sheet_name="Voters", index=False)
        candidates.to_excel(writer, sheet_name="Candidates", index=False)

# make for voter login and voting
def voter_panel(voters, candidates):
    aadhaar = input("Enter Aadhaar: ")

    user = voters[voters["Aadhaar"] == int(aadhaar)]

    if user.empty:
        print("Voter not found x")
        return voters, candidates

    if user.iloc[0]["Has_Voted"] == "Yes":
        print("You have already voted x")
        return voters, candidates

    print("\nCandidates:")
    print(candidates[["ID", "Name", "Party"]])

    choice = int(input("Enter candidate ID: "))

    if choice not in candidates["ID"].values:
        print("Invalid choice x")
        return voters, candidates

    # for updating the votes
    candidates.loc[candidates["ID"] == choice, "Votes"] += 1
    voters.loc[voters["Aadhaar"] == int(aadhaar), "Has_Voted"] = "Yes"

    print("Vote cast successfully ✅")

    return voters, candidates

# Admin panel
def admin_panel(voters, candidates):
    password = input("Enter admin password: ")

    if password != "admin123":
        print("Wrong password x")
        return voters, candidates

    while True:
        print("\n--- Admin Panel ---")
        print("1. View Results")
        print("2. View Voters")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("\nResults:")
            print(candidates)

        elif choice == "2":
            print("\nVoters:")
            print(voters)

        elif choice == "3":
            break

        else:
            print("Invalid choice")

    return voters, candidates

# Main program
def main():
    voters, candidates = load_data()

    while True:
        print("\n===== Voting System =====")
        print("1. Voter Login")
        print("2. Admin Panel")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            voters, candidates = voter_panel(voters, candidates)
            save_data(voters, candidates)

        elif choice == "2":
            voters, candidates = admin_panel(voters, candidates)
            save_data(voters, candidates)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()