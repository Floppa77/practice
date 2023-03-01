import haydenhomework

Charles = haydenhomework.Dogs("Charles", "Pug", "Digging")
Xavier = haydenhomework.Dogs("Xavier", "Bloodhound", "Sniffing")
Moses = haydenhomework.Dogs("Moses", "Terrier", "Running")

userrequest = input("which dog do you want to see?\nCharles\nXavier\nMoses\n")

if userrequest == "Charles":
    print("Charles is a Pug that likes to digging! What a digger.")
elif userrequest == "Xavier":
    print("Xavier is a Bloodhound that likes sniffing stuff!")
elif userrequest == "Moses":
    print("Moses is a Terrier that likes to run. What is he running from.")
