import pandas as pd
import matplotlib.pyplot as plt

FILE = "voting_data.xlsx"

# LOAD DATA 
def load_data():
    voters = pd.read_excel(FILE, sheet_name="Voters")
    candidates = pd.read_excel(FILE, sheet_name="Candidates")

    # Clean column names (VERY IMPORTANT)
    voters.columns = voters.columns.str.strip().str.replace(" ", "_").str.replace("\ufeff", "")
    candidates.columns = candidates.columns.str.strip().str.replace(" ", "_").str.replace("\ufeff", "")

    print("Detected Voters columns:", voters.columns.tolist())

    # Auto-fix Voter_ID column
    if "Voter_ID" not in voters.columns:
        for col in voters.columns:
            if "voter" in col.lower() or "aadhaar" in col.lower():
                voters.rename(columns={col: "Voter_ID"}, inplace=True)
                print(f"Renamed '{col}' → 'Voter_ID'")
                break

    # Convert types
    voters["Voter_ID"] = voters["Voter_ID"].astype(str)
    voters["Has_Voted"] = voters["Has_Voted"].astype(str)
    candidates["Votes"] = candidates["Votes"].astype(int)

    return voters, candidates

#  SAVE DATA 
def save_data(voters, candidates):
    with pd.ExcelWriter(FILE, engine="openpyxl", mode="w") as writer:
        voters.to_excel(writer, sheet_name="Voters", index=False)
        candidates.to_excel(writer, sheet_name="Candidates", index=False)

#  CAST VOTE
def cast_vote(voters, candidates):
    constituency = input("Enter Constituency: ").strip().title()
    voter_id = input("Enter Voter ID: ").strip()

    user = voters[voters["Voter_ID"] == voter_id]

    if user.empty:
        print("❌ Voter not found")
        return voters, candidates

    if user.iloc[0]["Has_Voted"] == "Yes":
        print("❌ Already voted")
        return voters, candidates

    if user.iloc[0]["Constituency"] != constituency:
        print("❌ Constituency mismatch")
        return voters, candidates

    available = candidates[candidates["Constituency"] == constituency]

    print("\nCandidates:")
    print(available[["ID", "Name", "Party"]])

    try:
        choice = int(input("Enter Candidate ID: "))
    except:
        print("❌ Invalid input")
        return voters, candidates

    if choice not in available["ID"].values:
        print("❌ Invalid candidate")
        return voters, candidates

    confirm = input("Confirm vote? (yes/no): ").lower()
    if confirm != "yes":
        print("Vote cancelled")
        return voters, candidates

    candidates.loc[candidates["ID"] == choice, "Votes"] += 1
    voters.loc[voters["Voter_ID"] == voter_id, "Has_Voted"] = "Yes"

    print("✅ Vote cast successfully!")

    return voters, candidates

#  OVERALL RESULTS 
def overall_results(candidates):
    print("\n===== OVERALL RESULTS =====")

    winners = candidates.loc[candidates.groupby("Constituency")["Votes"].idxmax()]
    seats = winners["Party"].value_counts()

    print("\nSeats Won:")
    print(seats)

    # Bar graph
    seats.plot(kind="bar", title="Seats per Party")
    plt.ylabel("Seats")
    plt.show()

    # Pie chart
    vote_share = candidates.groupby("Party")["Votes"].sum()
    vote_share.plot(kind="pie", autopct="%1.1f%%", title="Vote Share")
    plt.ylabel("")
    plt.show()

#  CONSTITUENCY RESULTS 
def constituency_result(candidates):
    constituency = input("Enter Constituency: ").strip().title()

    data = candidates[candidates["Constituency"] == constituency]

    if data.empty:
        print("❌ Invalid constituency")
        return

    print("\nResults:")
    print(data[["Name", "Party", "Votes"]])

    # Pie chart
    data.set_index("Name")["Votes"].plot(
        kind="pie", autopct="%1.1f%%", title=f"{constituency} Vote Share"
    )
    plt.ylabel("")
    plt.show()

    sorted_data = data.sort_values(by="Votes", ascending=False)
    winner = sorted_data.iloc[0]
    runner_up = sorted_data.iloc[1]

    margin = winner["Votes"] - runner_up["Votes"]

    print(f"\n🏆 Winner: {winner['Name']} ({winner['Party']})")
    print(f"📊 Winning Margin: {margin} votes")

#  RESULTS MENU 
def results_menu(candidates):
    while True:
        print("\n----- RESULTS MENU -----")
        print("1. Overall Results")
        print("2. Constituency Results")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            overall_results(candidates)

        elif choice == "2":
            constituency_result(candidates)

        elif choice == "3":
            break

        else:
            print("❌ Invalid choice")

#  MAIN 
def main():
    voters, candidates = load_data()

    while True:
        print("\n========== 🗳️ SMART VOTING SYSTEM ==========")
        print("1. Cast Vote")
        print("2. View Results")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            voters, candidates = cast_vote(voters, candidates)
            save_data(voters, candidates)

        elif choice == "2":
            results_menu(candidates)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()