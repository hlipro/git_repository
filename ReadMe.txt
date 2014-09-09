Git Introduction

Directorties: Work; Stage(temperory save); Commit(upload change)

Commmand:
git init: init a repository directory
git add: submit changed file into stage directory
git commit -m "comment": upload change; add version ID & comment
git reset --hard HEAD^ (option: HEAD^ back to previous version
								HEAD^^ second-previous version
			        			HEAD~100 back to 100th version
								version-ID [can go forward or backward])
git log: check previous versions & version id
git status: check work;stage;commit directories
git diff readme.txt: check difference
		 Head -- readme.txt
git reflog: check previous version id if the version is deleted

//Withdraw changes//
git checkout -- readme.txt: delete change in work; go to version in 	                            commit or stage
git reset HEAD readme.txt: delete change in stage; unstage

//Delete files E.g.//
rm test.txt
git rm test.txt
git commit -m 'delete test'

//generate key for github//
$ ssh-keygen -t rsa -C "youremail@example.com": 
                   generate id_rsa id_rsa.pub in Usrs/usrname/.ssh/
                   submit id_rsa.pub in gitpub account setting-ssh key

//remote origin (github repository)//
Create new repositroy on github;
git remote add origin git@github.com:hlipro/git_repository.git
git remote set-url origin https://github.com/hlipro/git_repository
git push -u origin master
git push origin master: push local file to server
git clone git@github.com:hlipro/git_newrespository.git







