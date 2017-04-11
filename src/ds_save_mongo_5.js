
import json

doc = {"Persons" : [{"id":"405", "이름":"js1"},{"id":"406", "이름":"js2"},{"id":"301", "이름":"js3"},{"id":"102", "이름":"js4"}]}

use examDB
#db.createCollection("personCol")
db.personColl.insert(doc)
db.personColl.find({"Persons.id" : "405"})