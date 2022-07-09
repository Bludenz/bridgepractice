OWNER = input(str("What is your IGN (just for the purpose of the prototype) >>> "))

print("""
/comm help - Shows this page
/comm create [name] - Creates a Community
/comm promote [user] - Promotes a user to the Community Manager
/comm demote [user] - Demotes a user back to a member
/comm disband - Disbans your community
/comm kick [user] - Kicks a user from your community
/comm invite [user] - Invites a user to your community
/comm list - Lists all members in your community
/comm join [comm name] - Request to join a community
==================================================================
[1] Exit
""")

class Community:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

while True:
    command = input(str(""))
    if command == "/comm help":
        print("""
        /comm help - Shows this page
        /comm create [name] - Creates a Community
        /comm promote [user] - Promotes a user to the Community Manager
        /comm demote [user] - Demotes a user back to a member
        /comm disband - Disbans your community
        /comm kick [user] - Kicks a user from your community
        /comm invite [user] - Invites a user to your community
        /comm list - Lists all members in your community
        /comm join [comm name] - Request to join a community
        ==================================================================
        [1] Exit
        """) 
    elif "/comm create" in command:
        raw = command.split(" ")
        raw.remove("/comm")
        raw.remove("create")
        c_name = " ".join(raw)
        community = Community(c_name, OWNER)
        print(f"You have created the {c_name} Community. Use /comm help to view all commands")

    elif "/comm promote" in command:
        raw = command.split(" ")
        raw.remove("/comm")
        raw.remove("promote")
        user = "".join(raw)
        
        print(f"""
===============================================        
{user} has been promoted to Community Manager 
===============================================
        """)

    elif "/comm demote" in command:
        raw = command.split(" ")
        raw.remove("/comm")
        raw.remove("demote")
        user = "".join(raw)
        
        print(f"""
===============================================        
{user} has been demoted to Member
===============================================
        """)
    elif command == "/comm disband":          
        print(f"""
===============================================        
This community was disbanded by the owner.
===============================================
        """)
    elif "/comm kick" in command:
        raw = command.split(" ")
        raw.remove("/comm")
        raw.remove("kick")
        user = "".join(raw)
        
        print(f"""
===============================================        
{user} has been kicked from the Community 
===============================================
        """)
    elif "/comm invite" in command:
        raw = command.split(" ")
        raw.remove("/comm")
        raw.remove("invite")
        user = "".join(raw)
        
        print(f"""
===============================================        
{user} has been invited to the Community
===============================================
        """)

    elif "/comm join" in command:
        raw = command.split(" ")
        raw.remove("/comm")
        raw.remove("join")
        comm = " ".join(raw)
        
        print(f"""
===============================================        
{OWNER} has been requested to join {comm}
===============================================
        """)

    elif command == "1":
        exit()

    
