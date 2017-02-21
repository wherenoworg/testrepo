def libfunc(){
  echo "I'm a library function"
}

def githubStatus(Map args){
  ghstatus = libraryRresource 'ghstatus.py'
  sh ghstatus
}

return this;
