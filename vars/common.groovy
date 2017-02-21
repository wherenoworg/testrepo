def libfunc(){
  echo "I'm a library function"
}

def githubStatus(Map args){
  ghstatus = libraryResource 'ghstatus.py'
  sh ghstatus
}

return this;
