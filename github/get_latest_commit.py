from github import Github

g = Github("riti1302", "ritika@501")
new_commit = " "
i = 1

while(True):
	branch = g.get_repo("riti1302/CartPole").get_branch("master")
	latest_commit = branch.commit.sha
	if(i == 1):
		first_commit = latest_commit
		new_commit = first_commit
		print("First commit! SH = ", latest_commit)

	elif(new_commit != latest_commit):
		new_commit = latest_commit
		print("New commit! SH = ", new_commit)
	i += 1
